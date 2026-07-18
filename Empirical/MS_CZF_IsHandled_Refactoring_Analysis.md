---
metadata_schema: "1.0"
project:
  id: Orden
  name: Behavior Change Review Framework
document:
  id: ES-MS-CZF-001
  title: MS-CZF IsHandled Refactoring Analysis
  type: Empirical Study
  version: 0.1.0
  status: Active
classification:
  domain: Business Central Extensibility
  layer: Study
  maturity: Review
owner: Štěpán Dvořák
purpose: >
  Preserves a preliminary marker-limited analysis of IsHandled subscribers in
  Microsoft Fixed Asset Localization for Czech as case evidence.
quality:
  review: Not Reviewed
  evidence: Partial
  editorial: Draft
audience: [Researchers, Business Central Architects, Business Central Developers, Contributors, AI Assistants]
depends_on: [02_Research_Methodology.md, References/Microsoft_IsHandled_v2.0.md]
related_documents: [Empirical/KMITS_BA4_Finance_IsHandled_Audit.md, Empirical/MS_CZL_IsHandled_Refactoring_Analysis_Report.md]
study:
  method: Repository Code Audit
  subject: BC280 Fixed Asset Localization for Czech
  data_access: Microsoft Localization Source Snapshot
  reproducibility: Restricted
tags: [empirical-study, ishandled, preliminary, marker-limited, microsoft-localization]
---

# MS-CZF IsHandled Refactoring Analysis

## Study Status and Boundaries

This is a preliminary, marker-limited study of subscribers that accept
`var IsHandled: Boolean` and set `IsHandled := true`. The 16 findings comprise
15 subscriber observations plus a separate analytical finding concerning the
discovery-event semantics of one observed subscriber.

The study predates the repository's broader review framework. It does not claim
to identify every behavior-changing or architectural structural change in the
examined application. Its classifications and refactoring proposals are
provisional interpretations that should be reassessed with the completed
methodology, additional implementation markers, and a broader set of quality
attributes.

Datum: 2026-06-03
Repozitář: BC280 Fixed Asset Localization for Czech
MS Learn Link: https://learn.microsoft.com/en-us/dynamics365/business-central/localfunctionality/czech/ui-extensions-fixed-asset-localization-cz

## Cíl
Cílem je převést současný stav z event-driven override chaos na explicitní, řízenou a deterministickou architekturu rozšiřitelnosti.

## Shrnutí nálezu
- Nalezeno EventSubscriber metod s parametrem var IsHandled: Boolean: 15
- Nalezeno metod, kde se nastavuje IsHandled := true: 15
- Duplicitní konkurence na stejný event v rámci této extension: nenalezena
- Důležitá poznámka: mezi více extensions v tenantu zůstává IsHandled pořadí nedeterministické

## Klasifikační model
- A) FULL OVERRIDE (legitimate but needs control)
- B) PARTIAL LOGIC MODIFICATION (anti-pattern misuse)
- C) VALIDATION / SIDE EFFECT (incorrect usage)
- D) DEAD-END EVENT (extensibility broken)

## CRITICAL RISK a EXTENSIBILITY BREAK pravidla
- CRITICAL RISK: více subscriberů soutěží o stejný IsHandled event (v této extension nenalezeno)
- EXTENSIBILITY BREAK: event je unesený přes IsHandled bez re-expozice navazujících hooků

## Nový typ chyby: Discovery misuse of IsHandled
- Popis:
  - Jde o případ, kdy event není určený k override toku, ale k detekci capability nebo feature availability napříč extensions.
  - V takovém scénáři IsHandled vytváří umělý winner-takes-all efekt a dělá výsledek závislý na pořadí subscriberů.
- Proč je to chyba:
  - Discovery dotaz má být akumulační (OR), ne stop-signal.
  - V multi-extension prostředí může být validní více odpovědí současně.
  - IsHandled může způsobit stav, kdy je uživateli prezentováno, že feature bude aktivní, ale jiný subscriber výsledek potlačí.
- Klasifikace:
  - E) OVERUSE / MISUSE OF IsHandled IN DISCOVERY EVENTS
- Řízené doporučení (bez zásahu do Microsoft zdrojového kódu):
  - V analytické rovině označit tento pattern jako governance issue.
  - Při komunikaci do upstream navrhnout přechod z IsHandled na čistý var Boolean akumulátor bez stop semantiky.
  - Zachovat backward compatibility přes paralelní přechodné API, pokud je to nutné.

---

### Finding #1
- Classification: B) PARTIAL LOGIC MODIFICATION
- Location:
  - Object: Codeunit 31247 Calc. Normal Depr. Handler CZF
  - Event: OnAfterCalcSL
  - File: Src/Codeunits/CalcNormalDeprHandlerCZF.Codeunit.al (subscriber kolem řádku 50)
- Current Behavior:
  - Subscriber upravuje RemainingLife a při RemainingLife < 1 nastaví IsHandled := true a ExitValue := -BookValue.
  - Business logika je přímo v subscriberu: ano.
- Problem:
  - Riziko nedeterminismu, pokud jiná extension řeší stejný lifecycle výpočtu depreciation.
  - Potenciální dead-end bez dalších hooků v custom větvi.
- Impact:
  - Hidden coupling na interní algoritmus depreciation.
- Proposed Solution:
  - IsHandled Bridge Pattern: přesunout logiku do orchestrátoru a subscriber ponechat jako tenký adapter.
  - Přidat OnBeforeCustomSLExit a OnAfterCustomSLExit.
- Code Example:
```al
codeunit 71200 "CZF SL Exit Orchestrator"
{
    procedure Execute(var FADepreciationBook: Record "FA Depreciation Book"; BookValue: Decimal; var ExitValue: Decimal; var RemainingLife: Decimal): Boolean
    begin
        OnBeforeCustomSLExit(FADepreciationBook, BookValue, ExitValue, RemainingLife);

        if not FADepreciationBook."Keep Deprec. Ending Date CZF" then
            RemainingLife += CalcDeprBreakDaysBridge(FADepreciationBook);

        if RemainingLife < 1 then begin
            ExitValue := -BookValue;
            OnAfterCustomSLExit(FADepreciationBook, ExitValue, RemainingLife, true);
            exit(true);
        end;

        OnAfterCustomSLExit(FADepreciationBook, ExitValue, RemainingLife, false);
        exit(false);
    end;

    local procedure CalcDeprBreakDaysBridge(FADepreciationBook: Record "FA Depreciation Book"): Decimal
    begin
        // zde volat existující výpočetní službu
        exit(0);
    end;

    [IntegrationEvent(false, false)]
    local procedure OnBeforeCustomSLExit(var FADepreciationBook: Record "FA Depreciation Book"; BookValue: Decimal; var ExitValue: Decimal; var RemainingLife: Decimal)
    begin
    end;

    [IntegrationEvent(false, false)]
    local procedure OnAfterCustomSLExit(var FADepreciationBook: Record "FA Depreciation Book"; var ExitValue: Decimal; RemainingLife: Decimal; Handled: Boolean)
    begin
    end;
}
```

### Finding #2
- Classification: A) FULL OVERRIDE
- Location:
  - Object: Codeunit 31247 Calc. Normal Depr. Handler CZF
  - Event: OnBeforeCalcRounding
  - File: Src/Codeunits/CalcNormalDeprHandlerCZF.Codeunit.al (subscriber kolem řádku 361)
- Current Behavior:
  - Pokud Use Rounding in Periodic Depr. = true, subscriber provede vlastní rounding a nastaví IsHandled := true.
  - Business logika je přímo v subscriberu: ano.
- Problem:
  - Přímé přepsání base rounding flow.
- Impact:
  - Hidden coupling na lokalizační rounding policy.
- Proposed Solution:
  - Strategy + Interface pro rounding policy, explicitní výběr strategie.
- Code Example:
```al
interface 71201 "ICZF Depr Rounding Strategy"
{
    procedure Apply(DeprBook: Record "Depreciation Book"; OrigAmount: Decimal; var Amount: Decimal): Boolean;
}

codeunit 71202 "CZF RoundUp Strategy" implements "ICZF Depr Rounding Strategy"
{
    procedure Apply(DeprBook: Record "Depreciation Book"; OrigAmount: Decimal; var Amount: Decimal): Boolean
    begin
        if not DeprBook."Use Rounding in Periodic Depr." then
            exit(false);
        Amount := Round(Amount, 1, '>');
        exit(true);
    end;
}
```

### Finding #3
- Classification: A) FULL OVERRIDE
- Location:
  - Object: Codeunit 31236 FA Acquisition Handler CZF
  - Event: OnBeforeCheckBalAccountNo
  - File: Src/Codeunits/FAAcquisitionHandlerCZF.Codeunit.al (subscriber kolem řádku 95)
- Current Behavior:
  - Vlastní validační větev pro Custom 2 + nastavení FANo, následně IsHandled := true.
  - Business logika je přímo v subscriberu: ano.
- Problem:
  - Přepis standardní validace přes IsHandled.
- Impact:
  - Nedeterminismus mezi extensions, hidden coupling na setup a posting typy.
- Proposed Solution:
  - Factory Pattern + validator interface, explicitně řízená volba validátoru.
- Code Example:
```al
interface 71210 "ICZF FA Account Validator"
{
    procedure ValidateBalAccount(var GenJournalLine: Record "Gen. Journal Line"; var FANo: Code[20]);
}

codeunit 71211 "CZF Custom2 Account Validator" implements "ICZF FA Account Validator"
{
    procedure ValidateBalAccount(var GenJournalLine: Record "Gen. Journal Line"; var FANo: Code[20])
    begin
        // sem přesunout stávající validaci
        FANo := GenJournalLine."Bal. Account No.";
    end;
}
```

### Finding #4
- Classification: A) FULL OVERRIDE
- Location:
  - Object: Codeunit 31236 FA Acquisition Handler CZF
  - Event: OnBeforeCheckAccountNo
  - File: Src/Codeunits/FAAcquisitionHandlerCZF.Codeunit.al (subscriber kolem řádku 132)
- Current Behavior:
  - Zrcadlově k předchozímu nálezu, ale pro Account No.
  - Business logika je přímo v subscriberu: ano.
- Problem:
  - Duplicitní override pattern.
- Impact:
  - Vyšší riziko driftu logiky mezi dvěma větvemi.
- Proposed Solution:
  - Stejná validator strategie jako ve Finding #3.
- Code Example:
```al
codeunit 71212 "CZF FA Validator Factory"
{
    procedure GetValidator(GenJournalLine: Record "Gen. Journal Line"): Interface "ICZF FA Account Validator"
    begin
        if GenJournalLine."FA Posting Type" = GenJournalLine."FA Posting Type"::"Custom 2" then
            exit(Codeunit "CZF Custom2 Account Validator");
        exit(Codeunit "CZF Default Account Validator");
    end;
}
```

### Finding #5
- Classification: A) FULL OVERRIDE
- Location:
  - Object: Codeunit 31236 FA Acquisition Handler CZF
  - Event: OnBeforeGetFAPostingGroup
  - File: Src/Codeunits/FAAcquisitionHandlerCZF.Codeunit.al (subscriber kolem řádku 205)
- Current Behavior:
  - Subscriber řeší default depreciation book, přepnutí posting type, načtení posting group, VAT/Tax group assignment, následně IsHandled := true.
  - Business logika je přímo v subscriberu: ano.
- Problem:
  - Rozsáhlá orchestrace je uvnitř event subscriberu.
- Impact:
  - EXTENSIBILITY BREAK, vysoká komplexita, obtížné testování.
- Proposed Solution:
  - IsHandled Bridge Pattern: extrahovat do Execute() orchestrátoru a re-exponovat OnBefore/OnAfter eventy.
- Code Example:
```al
codeunit 71220 "CZF Purchase FA PostingGroup Orchestrator"
{
    procedure Execute(var PurchaseLine: Record "Purchase Line"): Boolean
    begin
        OnBeforeCustomGetFAPostingGroup(PurchaseLine);
        ResolveDepreciationBook(PurchaseLine);
        ResolveFAPostingType(PurchaseLine);
        ResolvePostingGroups(PurchaseLine);
        OnAfterCustomGetFAPostingGroup(PurchaseLine);
        exit(true);
    end;

    local procedure ResolveDepreciationBook(var PurchaseLine: Record "Purchase Line")
    begin
    end;

    local procedure ResolveFAPostingType(var PurchaseLine: Record "Purchase Line")
    begin
    end;

    local procedure ResolvePostingGroups(var PurchaseLine: Record "Purchase Line")
    begin
    end;

    [IntegrationEvent(false, false)]
    local procedure OnBeforeCustomGetFAPostingGroup(var PurchaseLine: Record "Purchase Line")
    begin
    end;

    [IntegrationEvent(false, false)]
    local procedure OnAfterCustomGetFAPostingGroup(var PurchaseLine: Record "Purchase Line")
    begin
    end;
}
```

### Finding #6
- Classification: C) VALIDATION / SIDE EFFECT
- Location:
  - Object: Codeunit 31236 FA Acquisition Handler CZF
  - Event: OnBeforeCheckAcquisitionCost
  - File: Src/Codeunits/FAAcquisitionHandlerCZF.Codeunit.al (subscriber kolem řádku 272)
- Current Behavior:
  - Vlastní TestField pro Custom 2, IsHandled := true.
  - Business logika je přímo v subscriberu: ano.
- Problem:
  - IsHandled je použit jen k přesměrování jedné validační podmínky.
- Impact:
  - Potlačení standardního flow bez explicitní orchestrace.
- Proposed Solution:
  - Přesun do explicitní validační služby, případně nahradit standard event usage bez IsHandled.
- Code Example:
```al
codeunit 71221 "CZF Acquisition Validation Service"
{
    procedure ValidateAcquisitionCost(var PurchaseLine: Record "Purchase Line")
    begin
        if IsCustom2Mode() then
            PurchaseLine.TestField("FA Posting Type", PurchaseLine."FA Posting Type"::"Custom 2 CZF");
    end;

    local procedure IsCustom2Mode(): Boolean
    begin
        exit(true);
    end;
}
```

### Finding #7
- Classification: A) FULL OVERRIDE
- Location:
  - Object: Codeunit 31236 FA Acquisition Handler CZF
  - Event: OnIsFAAcquisitionAsCustom2CZL
  - File: Src/Codeunits/FAAcquisitionHandlerCZF.Codeunit.al (subscriber kolem řádku 292)
- Current Behavior:
  - Subscriber vrací feature flag a nastaví IsHandled := true.
  - Business logika je přímo v subscriberu: ano.
- Problem:
  - IsHandled jako mechanismus pro single source of truth.
- Impact:
  - Hidden coupling při multi-app prostředí.
- Proposed Solution:
  - Factory/service pro explicitní získání feature policy.
- Code Example:
```al
codeunit 71222 "CZF Acquisition Mode Service"
{
    procedure IsEnabled(): Boolean
    var
        FASetup: Record "FA Setup";
    begin
        if not FASetup.Get() then
            exit(false);
        exit(FASetup."FA Acquisition As Custom 2 CZF");
    end;
}
```

### Finding #8
- Classification: C) VALIDATION / SIDE EFFECT
- Location:
  - Object: Codeunit 31236 FA Acquisition Handler CZF
  - Event: OnBeforeShowAcquisitionNotification
  - File: Src/Codeunits/FAAcquisitionHandlerCZF.Codeunit.al (subscriber kolem řádku 303)
- Current Behavior:
  - Acquirable := false a IsHandled := true.
  - Business logika je přímo v subscriberu: ano.
- Problem:
  - UI policy je v IsHandled subscriberu.
- Impact:
  - Slabá transparentnost a horší testovatelnost.
- Proposed Solution:
  - Explicitní Notification Policy service (deterministický výsledek).
- Code Example:
```al
interface 71223 "ICZF Acquisition Notification Policy"
{
    procedure CanShowAcquisitionNotification(): Boolean;
}
```

### Finding #9
- Classification: B) PARTIAL LOGIC MODIFICATION
- Location:
  - Object: Codeunit 31239 FA Deprec. Book Handler CZF
  - Event: OnBeforeSetFAJnlTrailCodes
  - File: Src/Codeunits/FADeprecBookHandlerCZF.Codeunit.al (subscriber kolem řádku 187)
- Current Behavior:
  - Subscriber nastaví Source Code podle template a IsHandled := true.
  - Business logika je přímo v subscriberu: ano.
- Problem:
  - Override trail codes v subscriberu bez orchestrátoru.
- Impact:
  - Hidden coupling na disposal reason flow.
- Proposed Solution:
  - IsHandled Bridge + central resolver pro trail codes.
- Code Example:
```al
codeunit 71230 "CZF Trail Code Resolver"
{
    procedure ResolveFA(var FAJnlLine: Record "FA Journal Line"): Boolean
    begin
        if (FAJnlLine."Reason Code" = '') or (FAJnlLine."FA Posting Type" <> FAJnlLine."FA Posting Type"::Disposal) then
            exit(false);
        // zde deterministic assignment
        exit(true);
    end;
}
```

### Finding #10
- Classification: B) PARTIAL LOGIC MODIFICATION
- Location:
  - Object: Codeunit 31239 FA Deprec. Book Handler CZF
  - Event: OnBeforeSetGenJnlTrailCodes
  - File: Src/Codeunits/FADeprecBookHandlerCZF.Codeunit.al (subscriber kolem řádku 203)
- Current Behavior:
  - Analogický override pro Gen. Journal Line, IsHandled := true.
  - Business logika je přímo v subscriberu: ano.
- Problem:
  - Duplikace logiky vůči Finding #9.
- Impact:
  - Vyšší maintenance risk.
- Proposed Solution:
  - Jeden resolver service s dvěma explicitními methodami.
- Code Example:
```al
codeunit 71230 "CZF Trail Code Resolver"
{
    procedure ResolveGen(var GenJnlLine: Record "Gen. Journal Line"): Boolean
    begin
        exit(true);
    end;
}
```

### Finding #11
- Classification: A) FULL OVERRIDE
- Location:
  - Object: Codeunit 31235 FA Disposal Handler CZF
  - Event: OnBeforePostDisposalEntry
  - File: Src/Codeunits/FADisposalHandlerCZF.Codeunit.al (subscriber kolem řádku 239)
- Current Behavior:
  - Masivní disposal posting logika (výpočty, reverse, allocation, correction) v subscriberu, zakončeno IsHandled := true.
  - Business logika je přímo v subscriberu: ano.
- Problem:
  - Kompletní přepsání base posting flow přes IsHandled.
- Impact:
  - EXTENSIBILITY BREAK, upgrade fragility, slabá auditovatelnost flow.
- Proposed Solution:
  - Orchestrator codeunit s explicitními fázemi a IntegrationEvent hooky.
- Code Example:
```al
codeunit 71240 "CZF Disposal Posting Orchestrator"
{
    procedure Execute(var FALedgEntry: Record "FA Ledger Entry"; DeprBook: Record "Depreciation Book"; FANo: Code[20]; ErrorEntryNo: Integer; var FAInsertLedgEntry: Codeunit "FA Insert Ledger Entry")
    begin
        OnBeforeCustomDisposalPosting(FALedgEntry, DeprBook, FANo, ErrorEntryNo);
        InitializeContext(FALedgEntry, DeprBook, FANo, ErrorEntryNo);
        PostDisposalEntries(FALedgEntry, FAInsertLedgEntry);
        PostCorrections(FALedgEntry, FAInsertLedgEntry);
        OnAfterCustomDisposalPosting(FALedgEntry, DeprBook, FANo, ErrorEntryNo);
    end;

    local procedure InitializeContext(var FALedgEntry: Record "FA Ledger Entry"; DeprBook: Record "Depreciation Book"; FANo: Code[20]; ErrorEntryNo: Integer)
    begin
    end;

    local procedure PostDisposalEntries(var FALedgEntry: Record "FA Ledger Entry"; var FAInsertLedgEntry: Codeunit "FA Insert Ledger Entry")
    begin
    end;

    local procedure PostCorrections(var FALedgEntry: Record "FA Ledger Entry"; var FAInsertLedgEntry: Codeunit "FA Insert Ledger Entry")
    begin
    end;

    [IntegrationEvent(false, false)]
    local procedure OnBeforeCustomDisposalPosting(var FALedgEntry: Record "FA Ledger Entry"; DeprBook: Record "Depreciation Book"; FANo: Code[20]; ErrorEntryNo: Integer)
    begin
    end;

    [IntegrationEvent(false, false)]
    local procedure OnAfterCustomDisposalPosting(var FALedgEntry: Record "FA Ledger Entry"; DeprBook: Record "Depreciation Book"; FANo: Code[20]; ErrorEntryNo: Integer)
    begin
    end;
}
```

### Finding #12
- Classification: B) PARTIAL LOGIC MODIFICATION
- Location:
  - Object: Codeunit 31235 FA Disposal Handler CZF
  - Event: OnBeforeGetMaintenanceAccNo
  - File: Src/Codeunits/FADisposalHandlerCZF.Codeunit.al (subscriber kolem řádku 522)
- Current Behavior:
  - Nastavení AccountNo přes custom lookup a IsHandled := true.
  - Business logika je přímo v subscriberu: ano.
- Problem:
  - Přesměrování account resolution přes IsHandled.
- Impact:
  - Riziko konfliktu s jinými account policies.
- Proposed Solution:
  - Strategy + Interface pro maintenance account resolution.
- Code Example:
```al
interface 71241 "ICZF Maintenance Account Strategy"
{
    procedure Resolve(var MaintenanceLedgEntry: Record "Maintenance Ledger Entry"): Code[20];
}
```

### Finding #13
- Classification: A) FULL OVERRIDE
- Location:
  - Object: Codeunit 31235 FA Disposal Handler CZF
  - Event: OnBeforeFAInsertGLAccount
  - File: Src/Codeunits/FADisposalHandlerCZF.Codeunit.al (subscriber kolem řádku 543)
- Current Behavior:
  - Kompletní přepsání části FA Insert G/L Account flow, včetně disposal correction a book value correction, zakončeno IsHandled := true.
  - Business logika je přímo v subscriberu: ano.
- Problem:
  - Full override velmi rozsáhlé posting logiky.
- Impact:
  - EXTENSIBILITY BREAK a vysoké regresní riziko.
- Proposed Solution:
  - Deterministická pipeline (Factory + orchestrace fází).
- Code Example:
```al
codeunit 71242 "CZF FA GL Insert Pipeline"
{
    procedure Execute(var Context: Record "CZF FA GL Insert Context" temporary)
    begin
        ResolveAccountPhase(Context);
        InsertBufferPhase(Context);
        DisposalCorrectionPhase(Context);
        BookValueCorrectionPhase(Context);
        CompletePhase(Context);
    end;

    local procedure ResolveAccountPhase(var Context: Record "CZF FA GL Insert Context" temporary)
    begin
    end;

    local procedure InsertBufferPhase(var Context: Record "CZF FA GL Insert Context" temporary)
    begin
    end;

    local procedure DisposalCorrectionPhase(var Context: Record "CZF FA GL Insert Context" temporary)
    begin
    end;

    local procedure BookValueCorrectionPhase(var Context: Record "CZF FA GL Insert Context" temporary)
    begin
    end;

    local procedure CompletePhase(var Context: Record "CZF FA GL Insert Context" temporary)
    begin
    end;
}
```

### Finding #14
- Classification: B) PARTIAL LOGIC MODIFICATION
- Location:
  - Object: Codeunit 31234 FA Insert G/L Acc. Handler CZF
  - Event: OnBeforeGetGLAccNoFromFAPostingGroup
  - File: Src/Codeunits/FAInsertGLAccHandlerCZF.Codeunit.al (subscriber kolem řádku 23)
- Current Behavior:
  - Subscriber řeší několik account typů přes custom větvení a IsHandled := true.
  - Business logika je přímo v subscriberu: ano.
- Problem:
  - ReasonMaintenanceCode a account-type selection jsou schované v subscriberu.
- Impact:
  - Hidden coupling, obtížné nahrazení/rozšíření.
- Proposed Solution:
  - Factory Pattern pro explicitní volbu GL account strategy.
- Code Example:
```al
codeunit 71243 "CZF GL Account Strategy Factory"
{
    procedure GetStrategy(AccountType: Enum "FA Posting Group Account Type"): Interface "ICZF GL Account Strategy"
    begin
        case AccountType of
            AccountType::Maintenance:
                exit(Codeunit "CZF Maintenance GL Account Strategy");
            AccountType::"Book Value Gain":
                exit(Codeunit "CZF BookValueGain GL Account Strategy");
            AccountType::"Book Value Loss":
                exit(Codeunit "CZF BookValueLoss GL Account Strategy");
        end;

        exit(Codeunit "CZF Default GL Account Strategy");
    end;
}
```

### Finding #15
- Classification: D) DEAD-END EVENT
- Location:
  - Object: Codeunit 31176 Supp. Updt. Source Handler CZF
  - Event: OnBeforeUpdateSource
  - File: Src/Codeunits/SuppUpdtSourceHandlerCZF.Codeunit.al (subscriber kolem řádku 7)
- Current Behavior:
  - Subscriber bez doménové logiky pouze nastaví IsHandled := true.
  - Business logika je přímo v subscriberu: ne, ale standardní flow je umlčen.
- Problem:
  - Typický event kidnapping.
- Impact:
  - EXTENSIBILITY BREAK.
- Proposed Solution:
  - Explicitní policy service + re-expozice OnBefore/OnAfter rozhodnutí.
- Code Example:
```al
codeunit 71250 "CZF Source Update Policy"
{
    procedure ShouldSuppress(var GenJournalLine: Record "Gen. Journal Line"): Boolean
    begin
        OnBeforeDecideSourceUpdate(GenJournalLine);
        exit(true);
    end;

    [IntegrationEvent(false, false)]
    local procedure OnBeforeDecideSourceUpdate(var GenJournalLine: Record "Gen. Journal Line")
    begin
    end;
}
```

### Finding #16
- Classification: E) OVERUSE / MISUSE OF IsHandled IN DISCOVERY EVENTS
- Location:
  - Object: Codeunit 31236 FA Acquisition Handler CZF
  - Event: OnIsFAAcquisitionAsCustom2CZL
  - File: Src/Codeunits/FAAcquisitionHandlerCZF.Codeunit.al (subscriber kolem řádku 292)
- Current Behavior:
  - Subscriber odpovídá na discovery otázku přes var FAAcquisitionAsCustom2: Boolean, ale zároveň používá IsHandled jako stop mechaniku.
  - Business logika je přímo v subscriberu: minimální, ale mechanismus řízení je nevhodný.
- Problem:
  - Discovery scénář je akumulační problém, nikoli override problém.
  - IsHandled zde zavádí pořadím řízenou nekonzistenci.
- Impact:
  - Hypotetický nesoulad mezi nastavením a runtime behavior při více současných subscriber odpovědích.
  - Těžko auditovatelný výsledek při multi-extension kombinacích.
- Proposed Solution:
  - Discovery pattern bez IsHandled (čistá akumulace Boolean výsledku).
  - Z pohledu tohoto repozitáře pouze evidovat nález a eskalovat do upstream návrhu, bez lokálních úprav Microsoft source.
- Code Example:
```al
// Koncepční vzor pro upstream návrh
[IntegrationEvent(false, false)]
local procedure OnDiscoverFAAcquisitionAsCustom2(var Enabled: Boolean)
begin
end;

// Subscriber v rozšíření capability pouze OR-akumuluje odpověď
Enabled := Enabled or SetupValue;
```

---

## Priorita refactoringu
1. OnBeforePostDisposalEntry a OnBeforeFAInsertGLAccount (nejvyšší dopad na posting a účetní konzistenci)
2. OnBeforeGetFAPostingGroup + OnBeforeCheckAccountNo/OnBeforeCheckBalAccountNo (akvizice a validace)
3. OnBeforeUpdateSource + trail code eventy (stabilizace dead-end a side effect oblastí)

## Doporučený migrační přístup
1. Fáze 1: Extract orchestration codeunit bez změny funkčního chování
2. Fáze 2: Subscriber ztenčit na adapter + explicit Execute() call
3. Fáze 3: Přidat OnBeforeCustomX/OnAfterCustomX hooky
4. Fáze 4: Nahradit IsHandled větve přes Strategy/Factory tam, kde je to možné
5. Fáze 5: Doplnit automatizované testy pro deterministické scénáře

## Závěr
V tomto codebase je IsHandled pattern použit konzistentně jako override mechanismus, zejména v posting a disposal logice. Funkčně to řeší lokalizační požadavky, ale architektonicky jde o vysoké riziko pro determinismus, rozšiřitelnost a testovatelnost. Největší přínos přinese postupná migrace na explicitní orchestraci + Strategy/Factory model s minimálním subscriber adapterem.
