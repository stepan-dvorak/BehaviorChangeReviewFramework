# Audit použití IsHandled patternu v AL kódu

Tento dokument shrnuje nálezy z analýzy aktuálního AL codebase v projektu `App`. Zaměření je na `EventSubscriber` metody, které používají `var IsHandled: Boolean` a nastavují `IsHandled := true`.

Cíl není `IsHandled` plošně odstranit. Cíl je převést neřízené override chování na deterministickou a explicitně řízenou extensibility architekturu.

## Shrnutí

Bylo nalezeno 12 relevantních subscriberů:

- 2x dead-end approval override
- 4x validation bypass / side effect
- 2x partial logic modification
- 4x full override

V rámci tohoto workspace nebyl nalezen žádný konkurenční subscriber na stejný event. To znamená, že zde není prokázaný intra-repo `critical risk`, ale několik míst je architektonicky rizikových i bez vnitřní konkurence.

## Klasifikace

- **A) FULL OVERRIDE**: legitimní, ale musí být řízený a obalený bridge vrstvou
- **B) PARTIAL LOGIC MODIFICATION**: anti-pattern misuse, protože jeden subscriber jen částečně modifikuje tok a druhý ho potlačuje
- **C) VALIDATION / SIDE EFFECT**: nepřímé vypínání standardní validace nebo kontroly
- **D) DEAD-END EVENT**: extensibility chain je přerušená a chybí další explicitní hooky

## Finding #1

- **Classification:** D) DEAD-END EVENT
- **Location:** `GeneralDocApprovMgt.Codeunit.al` - `Codeunit "Approvals Management CZL"`, event `OnSetStatusToApproved`
- **Current behavior:** Subscriber mění status `General Doc. Header fKMS` na `Released`, provede `Modify(false)`, naplní `Variant` a nastaví `IsHandled := true`. Business logic je přímo v subscriberu.
- **Problem:** Tento subscriber kidnappuje approval flow pro vlastní tabulku a přerušuje standardní extensibility chain. Chování je deterministické pro tento případ, ale je skryté a těžko rozšiřitelné.
- **Impact:** Hidden coupling, broken extensibility chain, slabší testovatelnost.
- **Proposed solution:** Použij `Strategy + Interface` nebo `IsHandled Bridge Pattern`. Subscriber má být jen tenká adaptace, zatímco vlastní transition logika má být v handler codeunitu s explicitními `OnBefore...` a `OnAfter...` eventy.
- **Code example:**
```al
interface "IApprovalStatusStrategy fKMS"
{
    procedure CanHandle(InputRecordRef: RecordRef): Boolean;
    procedure SetToApproved(InputRecordRef: RecordRef; var Variant: Variant);
    procedure SetToPendingApproval(InputRecordRef: RecordRef; var Variant: Variant);
}

codeunit 70994650 "Approval Status Factory fKMS"
{
    procedure Resolve(InputRecordRef: RecordRef): Interface "IApprovalStatusStrategy fKMS"
    begin
        if InputRecordRef.Number() = Database::"General Doc. Header fKMS" then
            exit(Codeunit::"General Doc Approval Strategy fKMS");
    end;
}

[EventSubscriber(ObjectType::Codeunit, Codeunit::"Approvals Management CZL", OnSetStatusToApproved, '', false, false)]
local procedure SetGeneralDocumentStatusToApproved(InputRecordRef: RecordRef; var Variant: Variant; var IsHandled: Boolean)
var
    Strategy: Interface "IApprovalStatusStrategy fKMS";
begin
    Strategy := ApprovalStatusFactory.Resolve(InputRecordRef);
    if not Strategy.CanHandle(InputRecordRef) then
        exit;

    Strategy.SetToApproved(InputRecordRef, Variant);
    IsHandled := true;
end;
```

## Finding #2

- **Classification:** D) DEAD-END EVENT
- **Location:** `GeneralDocApprovMgt.Codeunit.al` - `Codeunit "Approvals Mgmt."`, event `OnSetStatusToPendingApproval`
- **Current behavior:** Subscriber přepne `General Doc. Header fKMS` na `Pending Approval`, provede `Modify(true)`, naplní `Variant` a nastaví `IsHandled := true`. Business logic je přímo v subscriberu.
- **Problem:** Stejný problém jako ve Finding #1. Standardní approval flow je přepsaný a není zde explicitní orchestrace.
- **Impact:** Dead-end extensibility, hidden coupling, riziko nekonzistentního approval chování.
- **Proposed solution:** Stejný `Strategy + Interface` model jako ve Finding #1, ale pro pending approval transition.
- **Code example:**
```al
[EventSubscriber(ObjectType::Codeunit, Codeunit::"Approvals Mgmt.", OnSetStatusToPendingApproval, '', false, false)]
local procedure ApprovalsMgmtOnSetStatusToPendingApproval(RecRef: RecordRef; var Variant: Variant; var IsHandled: Boolean)
var
    Strategy: Interface "IApprovalStatusStrategy fKMS";
begin
    Strategy := ApprovalStatusFactory.Resolve(RecRef);
    if not Strategy.CanHandle(RecRef) then
        exit;

    Strategy.SetToPendingApproval(RecRef, Variant);
    IsHandled := true;
end;
```

## Finding #3

- **Classification:** C) VALIDATION / SIDE EFFECT
- **Location:** `FinanceHandlers.Codeunit.al` - `Codeunit "Gen. Jnl.-Check Line"`, event `OnBeforeCheckSalesDocNoIsNotUsed`
- **Current behavior:** Když je `Document Allocation Post. fKMS` aktivní, subscriber vypne standardní kontrolu sales document no. pomocí `IsHandled := true`.
- **Problem:** Toto je validation bypass. Standardní kontrola zmizí bez explicitního orchestration modelu. Chování závisí na skrytém flagu uvnitř subscriberu.
- **Impact:** Non-determinism v toku validace, hidden dependency, složité testování.
- **Proposed solution:** Přesuň rozhodnutí do explicitního posting orchestrátoru nebo policy service. Subscriber by neměl vypínat standardní check, ale delegovat na centrální policy.
- **Code example:**
```al
codeunit 70994660 "Document Allocation Policy fKMS"
{
    procedure AssertSalesPostingContext(GenJournalLine: Record "Gen. Journal Line")
    begin
        if not GenJournalLine."Document Allocation Post. fKMS" then
            exit;

        // Explicitní kontrola před postingem.
    end;
}
```

## Finding #4

- **Classification:** C) VALIDATION / SIDE EFFECT
- **Location:** `FinanceHandlers.Codeunit.al` - `Codeunit "Gen. Jnl.-Check Line"`, event `OnBeforeCheckPurchDocNoIsNotUsed`
- **Current behavior:** Purchase varianta Finding #3 vypíná standardní kontrolu document no. při `Document Allocation Post. fKMS`.
- **Problem:** Stejný validation bypass a stejný problém se skrytým řízením toku.
- **Impact:** Hidden coupling, nedeterministické validace, slabší auditovatelnost.
- **Proposed solution:** Stejná policy/orchestrator extrakce jako u sales varianty.
- **Code example:**
```al
codeunit 70994660 "Document Allocation Policy fKMS"
{
    procedure AssertPurchasePostingContext(GenJournalLine: Record "Gen. Journal Line")
    begin
        if not GenJournalLine."Document Allocation Post. fKMS" then
            exit;

        // Explicitní purchase-specific checks.
    end;
}
```

## Finding #5

- **Classification:** C) VALIDATION / SIDE EFFECT
- **Location:** `FinanceHandlers.Codeunit.al` - `Codeunit "Gen. Jnl.-Post Line"`, event `OnBeforeCheckPurchExtDocNoProcedure`
- **Current behavior:** Subscriber vypne purchase external document number procedure pro `Document Allocation Post. fKMS`.
- **Problem:** Standardní posting validation je potlačená implicitně. To je typický anti-pattern misuse, protože determinismus závisí na interním flagu, ne na explicitním rozhodnutí vrstvy orchestrace.
- **Impact:** Non-determinism, hidden dependency, obtížné unit testy.
- **Proposed solution:** Nahraď event subscriber explicitní předpostovací policy službou, která rozhodne, zda se má použít standardní validace nebo custom allocation flow.
- **Code example:**
```al
codeunit 70994662 "Purchase Ext. Doc No. Policy fKMS"
{
    procedure ShouldUseStandardExtDocNoRule(GenJournalLine: Record "Gen. Journal Line"): Boolean
    begin
        exit(not GenJournalLine."Document Allocation Post. fKMS");
    end;
}
```

## Finding #6

- **Classification:** C) VALIDATION / SIDE EFFECT
- **Location:** `FinanceHandlers.Codeunit.al` - `Codeunit "Deferral Utilities"`, event `OnBeforeCheckDeferralConditionForGenJournal`
- **Current behavior:** Subscriber vždy nastaví `IsHandled := true`, tedy trvale vypíná standardní deferral-condition check.
- **Problem:** Toto je unconditional bypass. Chybí zde jakákoliv explicitní náhrada za standardní kontrolu, takže event funguje jako slepá ulička.
- **Impact:** Extensibility break v praxi, ztráta determinismu, slabá testovatelnost.
- **Proposed solution:** Přesuň pravidlo do dedicated policy service a volej ji z orchestration layer před deferral checks. Pokud má mít specializované chování, vyber ho přes factory.
- **Code example:**
```al
codeunit 70994663 "Deferral Policy fKMS"
{
    procedure ShouldBypassGenJournalDeferralCheck(): Boolean
    begin
        exit(false);
    end;

    procedure ApplyDeferralRule(var TotalAmount: Decimal; var AmtToDefer: Decimal)
    begin
        // Explicitní custom rule.
    end;
}
```

## Finding #7

- **Classification:** B) PARTIAL LOGIC MODIFICATION
- **Location:** `FinanceHandlers.Codeunit.al` - `Table "Sales Header"`, event `OnBeforeInitRecord`
- **Current behavior:** Subscriber přeskočí standardní inicializaci Sales Header, pokud jde o order/invoice vytvořený z quote a posting series už existuje.
- **Problem:** Tok je rozdělen mezi `OnBeforeInitRecord` skip gate a `OnAfterInitRecord` series assignment. To vytváří hidden order dependency mezi subscriber logic a standardním code path.
- **Impact:** Nepřehledná orchestrace, risk pořadí, složité testování.
- **Proposed solution:** Odstraň skip gate a konsoliduj series resolution do jednoho deterministic resolver codeunitu. Subscriber v `OnAfterInitRecord` má aplikovat už vyřešený výsledek.
- **Code example:**
```al
codeunit 70994670 "No. Series Resolver fKMS"
{
    procedure ApplySalesPostingSeries(var SalesHeader: Record "Sales Header")
    begin
        // Resolve and apply series in one place.
    end;
}

[EventSubscriber(ObjectType::Table, Database::"Sales Header", OnAfterInitRecord, '', true, false)]
local procedure SelectSalesPostingNoSeriesOnAfterInitRecord(var SalesHeader: Record "Sales Header")
var
    Resolver: Codeunit "No. Series Resolver fKMS";
begin
    Resolver.ApplySalesPostingSeries(SalesHeader);
end;
```

## Finding #8

- **Classification:** B) PARTIAL LOGIC MODIFICATION
- **Location:** `FinanceHandlers.Codeunit.al` - `Table "Purchase Header"`, event `OnBeforeInitRecord`
- **Current behavior:** Purchase varianta Finding #7 používá stejný skip-gate pattern pro init record.
- **Problem:** Stejný hidden dependency pattern jako u sales varianty. Logika je rozdělena mezi více subscriberů a výsledný tok závisí na tom, co se podaří přeskočit.
- **Impact:** Hidden coupling, non-determinism, brittle behavior.
- **Proposed solution:** Stejný deterministic resolver pattern pro `Purchase Header`.
- **Code example:**
```al
codeunit 70994670 "No. Series Resolver fKMS"
{
    procedure ApplyPurchasePostingSeries(var PurchaseHeader: Record "Purchase Header")
    begin
        // Resolve and apply purchase series in one place.
    end;
}

[EventSubscriber(ObjectType::Table, Database::"Purchase Header", OnAfterInitRecord, '', true, false)]
local procedure SelectPurchPostingNoSeriesOnAfterInitRecord(var PurchaseHeader: Record "Purchase Header")
var
    Resolver: Codeunit "No. Series Resolver fKMS";
begin
    Resolver.ApplyPurchasePostingSeries(PurchaseHeader);
end;
```

## Finding #9

- **Classification:** A) FULL OVERRIDE
- **Location:** `FinanceHandlers.Codeunit.al` - `Table "Purchase Header"`, event `OnBeforeInitInsert`
- **Current behavior:** Subscriber explicitně nastaví `Purchase Header."No."` z quote-derived series, vymaže `Posting No. Series` a nastaví `IsHandled := true`.
- **Problem:** Toto je legitimní full override, ale přerušuje standardní init-insert flow. Pokud je to ponecháno jako subscriber, celý override zůstává skrytý a obtížně kompozibilní.
- **Impact:** Controlled override, ale s terminací standardní větve.
- **Proposed solution:** `IsHandled Bridge Pattern`. Přesuň logiku do handler codeunitu s `Execute()`. Subscriber má pouze volat bridge a přepnout `IsHandled`.
- **Code example:**
```al
codeunit 70994671 "Purchase Header Insert Bridge fKMS"
{
    procedure Execute(var PurchaseHeader: Record "Purchase Header"; var xPurchaseHeader: Record "Purchase Header"): Boolean
    begin
        OnBeforeCustomPurchaseInsert(PurchaseHeader, xPurchaseHeader);
        // Apply deterministic quote-to-order number series logic.
        OnAfterCustomPurchaseInsert(PurchaseHeader, xPurchaseHeader);
        exit(true);
    end;

    [IntegrationEvent(false, false)]
    procedure OnBeforeCustomPurchaseInsert(var PurchaseHeader: Record "Purchase Header"; var xPurchaseHeader: Record "Purchase Header")
    begin
    end;

    [IntegrationEvent(false, false)]
    procedure OnAfterCustomPurchaseInsert(var PurchaseHeader: Record "Purchase Header"; var xPurchaseHeader: Record "Purchase Header")
    begin
    end;
}
```

## Finding #10

- **Classification:** A) FULL OVERRIDE
- **Location:** `AdvanceLetterHandler.Codeunit.al` - `Codeunit "Sales Adv. Letter-Post CZZ"`, event `OnBeforePostExchangeRate`
- **Current behavior:** Subscriber rozpozná partial close, přepočítá `Amount` a `VATAmount`, zavolá `SalesAdvLetterPostfKMS.PostExchangeRate(...)` a nastaví `IsHandled := true`.
- **Problem:** Toto je řízený override posting logiky. Je to legitimní, ale stále je to hard fork standardního flow. Pokud custom handler nevystavuje vlastní hooks, chain končí tady.
- **Impact:** Controlled override, ale s terminací standardního chainu.
- **Proposed solution:** Přesuň výpočet do posting bridge codeunitu a přidej explicitní `OnBefore...` / `OnAfter...` events.
- **Code example:**
```al
codeunit 70994672 "Sales Adv. Letter Post Bridge fKMS"
{
    procedure Execute(SalesAdvLetterHeaderCZZ: Record "Sales Adv. Letter Header CZZ"; SalesAdvLetterEntryCZZ: Record "Sales Adv. Letter Entry CZZ"; VATPostingSetup: Record "VAT Posting Setup"; Amount: Decimal; VATAmount: Decimal; RelatedEntryNo: Integer; Correction: Boolean; var GenJnlPostLine: Codeunit "Gen. Jnl.-Post Line"; var AdvancePostingParametersCZZ: Record "Advance Posting Parameters CZZ")
    begin
        OnBeforeExecute(SalesAdvLetterHeaderCZZ, SalesAdvLetterEntryCZZ, VATPostingSetup);
        // Partial-close exchange rate logic.
        OnAfterExecute(SalesAdvLetterHeaderCZZ, SalesAdvLetterEntryCZZ, VATPostingSetup);
    end;

    [IntegrationEvent(false, false)]
    procedure OnBeforeExecute(...)
    begin
    end;

    [IntegrationEvent(false, false)]
    procedure OnAfterExecute(...)
    begin
    end;
}
```

## Finding #11

- **Classification:** A) FULL OVERRIDE
- **Location:** `AdvanceLetterHandler.Codeunit.al` - `Codeunit "Purch. Adv. Letter-Post CZZ"`, event `OnBeforePostExchangeRate`
- **Current behavior:** Purchase varianta Finding #10 provede stejné partial-close přepočty, zavolá custom `PostExchangeRate` a nastaví `IsHandled := true`.
- **Problem:** Stejný controlled override s rizikem, že se standardní chain ukončí bez explicitní bridge vrstvy.
- **Impact:** Controlled override, ale skryté terminační chování.
- **Proposed solution:** Stejný bridge pattern jako u sales varianty.
- **Code example:**
```al
codeunit 70994673 "Purch. Adv. Letter Post Bridge fKMS"
{
    procedure Execute(PurchAdvLetterHeaderCZZ: Record "Purch. Adv. Letter Header CZZ"; PurchAdvLetterEntryCZZ: Record "Purch. Adv. Letter Entry CZZ"; VATPostingSetup: Record "VAT Posting Setup"; ExchRateAmount: Decimal; ExchRateVATAmount: Decimal; UsageEntryNo: Integer; Correction: Boolean; var GenJnlPostLine: Codeunit "Gen. Jnl.-Post Line"; var AdvancePostingParametersCZZ: Record "Advance Posting Parameters CZZ")
    begin
        OnBeforeExecute(PurchAdvLetterHeaderCZZ, PurchAdvLetterEntryCZZ, VATPostingSetup);
        // Partial-close exchange rate logic.
        OnAfterExecute(PurchAdvLetterHeaderCZZ, PurchAdvLetterEntryCZZ, VATPostingSetup);
    end;

    [IntegrationEvent(false, false)]
    procedure OnBeforeExecute(...)
    begin
    end;

    [IntegrationEvent(false, false)]
    procedure OnAfterExecute(...)
    begin
    end;
}
```

## Finding #12

- **Classification:** A) FULL OVERRIDE
- **Location:** `FinanceHandlers.Codeunit.al` - `Codeunit "Gen. Jnl.-Post Preview"`, event `OnBeforeShowAllEntries`
- **Current behavior:** Když je reconciliation aktivní, subscriber otevře custom page `Reconciliation fKMS` a nastaví `IsHandled := true`.
- **Problem:** Toto je oprávněná UI replacement logika, ale je skrytá v subscriberu. Determinističtější je explicitní navigator service.
- **Impact:** Controlled override, hidden orchestration, nižší testovatelnost.
- **Proposed solution:** Vytvoř `Reconciliation Navigator fKMS` codeunit s metodou `Show()`, která encapsuluje page navigation a vystavuje vlastní hooks.
- **Code example:**
```al
codeunit 70994674 "Reconciliation Navigator fKMS"
{
    procedure Show()
    begin
        OnBeforeShowReconciliation();
        // Open the custom reconciliation page here.
        OnAfterShowReconciliation();
    end;

    [IntegrationEvent(false, false)]
    procedure OnBeforeShowReconciliation()
    begin
    end;

    [IntegrationEvent(false, false)]
    procedure OnAfterShowReconciliation()
    begin
    end;
}

[EventSubscriber(ObjectType::Codeunit, Codeunit::"Gen. Jnl.-Post Preview", OnBeforeShowAllEntries, '', false, false)]
local procedure ShowJournalReconcile(var IsHandled: Boolean)
var
    Navigator: Codeunit "Reconciliation Navigator fKMS";
begin
    Navigator.Show();
    IsHandled := true;
end;
```

## Doporučení pro refactoring

1. Všude, kde subscriber jen blokuje standardní flow, přesuň rozhodnutí do explicitní policy nebo orchestrátoru.
2. Všude, kde subscriber plně nahrazuje standardní chování, zaveď bridge codeunit s `Execute()` a vlastními integration events.
3. U approval flows použij explicitní strategy selection místo přímého `IsHandled` override.
4. Pokud má být chování jen doplněno, nepoužívej `IsHandled` a zachovej standardní event chain.

## Závěr

V tomto codebase je `IsHandled` používán převážně jako řízený override mechanismus, ale na několika místech už přechází do anti-patternu kvůli validation bypassu a dead-end approval flow. Největší hodnotu přinese refactoring směrem k explicitní orchestrace, `Strategy + Interface` a `IsHandled Bridge Pattern`.
