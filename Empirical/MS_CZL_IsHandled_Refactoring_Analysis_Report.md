---
metadata_schema: "1.0"
project:
  id: Orden
  name: Behavior Change Review Framework
document:
  id: ES-MS-CZL-001
  title: MS-CZL IsHandled Refactoring Analysis Report
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
  Microsoft Core Localization Pack for Czech as case evidence.
quality:
  review: Not Reviewed
  evidence: Partial
  editorial: Draft
audience: [Researchers, Business Central Architects, Business Central Developers, Contributors, AI Assistants]
depends_on: [02_Research_Methodology.md, References/Microsoft_IsHandled_v2.0.md]
related_documents: [Empirical/KMITS_BA4_Finance_IsHandled_Audit.md, Empirical/MS_CZF_IsHandled_Refactoring_Analysis.md]
study:
  method: Repository Code Audit
  subject: BC280 Core Localization Pack for Czech
  data_access: Microsoft Localization Source Snapshot
  reproducibility: Restricted
tags: [empirical-study, ishandled, preliminary, marker-limited, microsoft-localization]
---

# MS-CZL IsHandled Refactoring Analysis Report

## Study Status and Boundaries

This is a preliminary, marker-limited study of subscribers that accept
`var IsHandled: Boolean` and set `IsHandled := true`. It records evidence about
one behavior-changing mechanism and the extensibility risks identified during
the original review; it is not a complete assessment of behavior-changing or
architectural structural changes in the examined application.

The study predates the repository's broader review framework. Its classifications
and refactoring proposals are provisional analytical interpretations. A future
reassessment should apply the completed methodology, consider additional
implementation markers, and evaluate quality attributes and architectural
effects beyond termination of an extensibility chain.

Datum: 2026-06-03
Repozitář: BC280 Core Localization Pack for Czech
MS Learn Link: https://learn.microsoft.com/en-us/dynamics365/business-central/localfunctionality/czech/ui-extensions-core-localization-pack-cz

## Scope a metodika

Byla provedena systematická analýza AL kódu s filtrem:

1. EventSubscriber metody s parametrem `var IsHandled: Boolean`
2. V těle metody je nastavováno `IsHandled := true`

Výsledek:

- 44 unikátních EventSubscriber metod splňuje obě podmínky.
- 3 skutečné CRITICAL kolize (stejný publisher objekt + stejný event) v posting logice Inventory Posting To G/L.

## Classification Summary

- A) FULL OVERRIDE: 7
- B) PARTIAL LOGIC MODIFICATION: 21
- C) VALIDATION / SIDE EFFECT: 8
- D) DEAD-END EVENT (EXTENSIBILITY BREAK): 8

These totals are derived from the classifications assigned to the 44 individual
findings. Category D identifies cases in which a subscriber takes control of the
standard flow without re-exposing downstream extension hooks.

---

## CRITICAL RISK: konkurenční subscribery na stejný event

### 1) Inventory Posting To G/L.OnBeforeBufferPurchPosting

- Src/Codeunits/CorrectionsPostingMgtCZL.Codeunit.al:139
- Src/Codeunits/InventoryPostingHandlerCZL.Codeunit.al:227

Riziko:

- Nedeterminismus podle pořadí subscriberů
- Hidden coupling mezi exp.cost correction a rounding scénáři
- Potenciální přeskočení části logiky při `IsHandled := true`

### 2) Inventory Posting To G/L.OnBeforeBufferSalesPosting

- Src/Codeunits/CorrectionsPostingMgtCZL.Codeunit.al:183
- Src/Codeunits/InventoryPostingHandlerCZL.Codeunit.al:138

Riziko:

- Stejný typ order-dependent chování
- Variabilní výsledky účetních zápisů

### 3) Inventory Posting To G/L.OnBeforeBufferOutputPosting

- Src/Codeunits/CorrectionsPostingMgtCZL.Codeunit.al:225
- Src/Codeunits/InventoryPostingHandlerCZL.Codeunit.al:87

Riziko:

- Kolize correction vs rounding orchestrace
- Vysoké riziko dead-end větvení

---

## Detaily nálezů

### Finding #1

- Classification: A) FULL OVERRIDE
- Location: Codeunit AccScheduleManagementCZL, event Financial Report Mgt.OnBeforePrint
- Current Behavior: Subscriber přebírá tisk podle typu reportu. Business logika je přímo v subscriberu.
- Problem: Implicitní úplné nahrazení standardního flow, bez explicitní orchestrace.
- Impact: Nedeterminismus při více rozšířeních.
- Proposed Solution: IsHandled Bridge Pattern + explicitní výběr strategie tisku.
- Code Example:

```al
codeunit 70030 "Financial Report Print Bridge CZL"
{
    procedure Execute(var FinancialReport: Record "Financial Report"; var IsHandled: Boolean)
    begin
        OnBeforeExecute(FinancialReport, IsHandled);
        if IsHandled then
            exit;

        case SelectStrategy(FinancialReport) of
            1:
                RunBalanceSheet(FinancialReport, IsHandled);
            2:
                RunIncomeStatement(FinancialReport, IsHandled);
        end;

        OnAfterExecute(FinancialReport, IsHandled);
    end;

    [IntegrationEvent(false, false)]
    local procedure OnBeforeExecute(var FinancialReport: Record "Financial Report"; var IsHandled: Boolean)
    begin
    end;

    [IntegrationEvent(false, false)]
    local procedure OnAfterExecute(var FinancialReport: Record "Financial Report"; IsHandled: Boolean)
    begin
    end;
}
```

### Finding #2

- Classification: A) FULL OVERRIDE
- Location: Codeunit AccScheduleManagementCZL, event Acc. Schedule Overview.OnBeforePrint
- Current Behavior: Přepisuje standardní tisk overview.
- Problem: Stejný anti-pattern jako #1, s implicitní kontrolou flow přes IsHandled.
- Impact: Kolizní chování při dalších custom print subscriberech.
- Proposed Solution: Factory Pattern pro volbu print strategy.
- Code Example: Použít stejný bridge jako #1, pouze jiný selector větve.

### Finding #3

- Classification: B) PARTIAL LOGIC MODIFICATION
- Location: Codeunit AccScheduleManagementCZL, event AccSchedManagement.OnBeforeDrillDownOnGLAccount
- Current Behavior: Podmíněný override drilldown cesty.
- Problem: IsHandled jako business switch, nikoli jako čisté stop-signal.
- Impact: Extensibility dead-end pro další drilldown úpravy.
- Proposed Solution: Strategy + Interface pro resolver drilldown.
- Code Example:

```al
interface "IDrilldown Strategy CZL"
{
    procedure Execute(var AccScheduleLine: Record "Acc. Schedule Line"; var IsHandled: Boolean);
}
```

### Finding #4

- Classification: B) PARTIAL LOGIC MODIFICATION
- Location: Codeunit AccScheduleManagementCZL, event AccSchedManagement.OnCalcCellValueInAccSchedLinesOnBeforeShowError
- Current Behavior: Přesměrování výpočtu hodnot buněk.
- Problem: Výpočtová logika ukryta v subscriberu.
- Impact: Slabá testovatelnost a transparentnost výpočtového řetězce.
- Proposed Solution: IsHandled Bridge Pattern + OnBeforeCustomCalc / OnAfterCustomCalc.
- Code Example: Extract do handler codeunitu s metodou Execute().

### Finding #5

- Classification: B) PARTIAL LOGIC MODIFICATION
- Location: Codeunit AccScheduleManagementCZL, event AccSchedManagement.OnBeforeDrillDownFromOverviewPage
- Current Behavior: Custom branch pro drilldown z overview.
- Problem: IsHandled ukončí chain bez re-expozice.
- Impact: Skrytá závislost na konkrétním pořadí extension logiky.
- Proposed Solution: Bridge + nové integrační eventy před/po custom větvi.

### Finding #6

- Classification: A) FULL OVERRIDE
- Location: Codeunit AccScheduleManagementCZL, event Categ. Generate Acc. Schedules.OnCreateIncomeStatementOnAfterCreateCOGSGroup
- Current Behavior: Přepisuje generování části income statement.
- Problem: Lokalizační override bez deterministické orchestrace.
- Impact: Vysoké riziko konfliktů v reporting customizacích.
- Proposed Solution: Strategy + Factory (IIncomeStatementBuilder).

### Finding #7

- Classification: B) PARTIAL LOGIC MODIFICATION
- Location: Codeunit CorrectionsPostingMgtCZL, event Gen. Jnl.-Post Batch.OnBeforeUpdateRecurringAmt
- Current Behavior: Modifikuje recurring amount flow.
- Problem: Mutace posting flow přes subscriber branch.
- Impact: Hidden coupling na interní posting kontext.
- Proposed Solution: Bridge + policy service pro recurring amount.

### Finding #8

- Classification: A) FULL OVERRIDE
- Location: Codeunit CorrectionsPostingMgtCZL, event Inventory Posting To G/L.OnBeforeBufferPurchPosting
- Current Behavior: Kompletní custom purchase buffer posting.
- Problem: CRITICAL kolize s Finding #25.
- Impact: Nedeterministický posting výsledek.
- Proposed Solution: Jediný orchestrátor (Factory + Strategy), žádné konkurenční subscribery.

### Finding #9

- Classification: A) FULL OVERRIDE
- Location: Codeunit CorrectionsPostingMgtCZL, event Inventory Posting To G/L.OnBeforeBufferSalesPosting
- Current Behavior: Kompletní custom sales buffer posting.
- Problem: CRITICAL kolize s Finding #23.
- Impact: Order-dependent behavior.
- Proposed Solution: Sloučit rozhodování do central posting factory.

### Finding #10

- Classification: A) FULL OVERRIDE
- Location: Codeunit CorrectionsPostingMgtCZL, event Inventory Posting To G/L.OnBeforeBufferOutputPosting
- Current Behavior: Kompletní custom output posting.
- Problem: CRITICAL kolize s Finding #22.
- Impact: Přeskakování větví podle pořadí subscriberů.
- Proposed Solution: Deterministická pipeline uvnitř 1 orchestrátoru.

### Finding #11

- Classification: C) VALIDATION / SIDE EFFECT
- Location: Codeunit DimensionMgtHandlerCZL, event DimensionManagement.OnCheckDimValuePostingOnBeforeExit
- Current Behavior: Validation branch končí IsHandled.
- Problem: Validation suppression přes IsHandled anti-pattern.
- Impact: Horší composability validačního řetězce.
- Proposed Solution: Validation strategy chain bez implicitního hijacku.

### Finding #12

- Classification: C) VALIDATION / SIDE EFFECT
- Location: Codeunit GenJnlPostLineHandlerCZL, event Gen. Jnl.-Post Line.OnInitVATOnBeforeVATPostingSetupCheck
- Current Behavior: Přeskakuje VAT setup check pro VAT LCY correction source code.
- Problem: Validation bypass.
- Impact: Riziko nekonzistence VAT kontrol.
- Proposed Solution: Explicitní IVATValidationStrategy místo IsHandled bypass.

### Finding #13

- Classification: B) PARTIAL LOGIC MODIFICATION
- Location: Codeunit GenJnlPostLineHandlerCZL, event Gen. Jnl.-Post Line.OnBeforePostDtldCVLedgEntry
- Current Behavior: Custom G/L entry branch pro multiple posting groups.
- Problem: Hluboká účetní logika přímo v subscriberu.
- Impact: Hidden coupling + obtížné testy.
- Proposed Solution: Extract do handleru + interface pro account resolution.

### Finding #14

- Classification: C) VALIDATION / SIDE EFFECT
- Location: Codeunit GenJournalBatchHandlerCZL, event Gen. Jnl.-Post Batch.OnBeforeIfCheckBalance
- Current Behavior: Podmíněné přeskočení balance check.
- Problem: Validace přes IsHandled.
- Impact: Potenciální drift integrity journalu.
- Proposed Solution: Explicitní balance policy service.

### Finding #15

- Classification: A) FULL OVERRIDE
- Location: Codeunit GLAccountCategoryMgtCZL, event G/L Account Category Mgt.OnBeforeInitializeAccountCategories
- Current Behavior: Kompletní custom inicializace kategorií.
- Problem: Monolitický override bez blending modelu.
- Impact: Konflikty při multilocalizačním stacku.
- Proposed Solution: Template method + factory-based initializer.

### Finding #16

- Classification: B) PARTIAL LOGIC MODIFICATION
- Location: Codeunit GLAccountCategoryMgtCZL, event G/L Account Category Mgt.OnBeforeLookupGLAccount
- Current Behavior: Custom lookup branch.
- Problem: Implicitní override lookupu přes IsHandled.
- Impact: UI lookup nedeterminismus při více rozšířeních.
- Proposed Solution: IGLAccountLookupStrategy.

### Finding #17

- Classification: B) PARTIAL LOGIC MODIFICATION
- Location: Codeunit GLAccountCategoryMgtCZL, event G/L Account Category.OnBeforeUpdatePresentationOrder
- Current Behavior: Přepis pořadí prezentace.
- Problem: Algorithm hijack bez explicitní orchestrace.
- Impact: Konflikty s jinými ordering customizacemi.
- Proposed Solution: ICategoryOrderStrategy + central orchestrator.

### Finding #18

- Classification: D) DEAD-END EVENT (EXTENSIBILITY BREAK)
- Location: Codeunit InstallApplicationsMgtCZL, event GlobalTriggerManagement.OnBeforeOnDatabaseInsert
- Current Behavior: Okamžitě `IsHandled := true`.
- Problem: Unesení globálního trigger flow.
- Impact: EXTENSIBILITY BREAK.
- Proposed Solution: Scoped suppression policy (setup-only, table whitelist).

### Finding #19

- Classification: D) DEAD-END EVENT (EXTENSIBILITY BREAK)
- Location: Codeunit InstallApplicationsMgtCZL, event GlobalTriggerManagement.OnBeforeOnDatabaseModify
- Current Behavior: Okamžitě handled.
- Problem: Totéž jako #18.
- Impact: EXTENSIBILITY BREAK.
- Proposed Solution: Policy service pro operation-level suppression.

### Finding #20

- Classification: D) DEAD-END EVENT (EXTENSIBILITY BREAK)
- Location: Codeunit InstallApplicationsMgtCZL, event GlobalTriggerManagement.OnBeforeOnDatabaseDelete
- Current Behavior: Okamžitě handled.
- Problem: Totéž jako #18.
- Impact: EXTENSIBILITY BREAK.
- Proposed Solution: Scoped suppression místo blanket disable.

### Finding #21

- Classification: D) DEAD-END EVENT (EXTENSIBILITY BREAK)
- Location: Codeunit InstallApplicationsMgtCZL, event GlobalTriggerManagement.OnBeforeOnDatabaseRename
- Current Behavior: Okamžitě handled.
- Problem: Totéž jako #18.
- Impact: EXTENSIBILITY BREAK.
- Proposed Solution: Scoped suppression místo blanket disable.

### Finding #22

- Classification: B) PARTIAL LOGIC MODIFICATION
- Location: Codeunit InventoryPostingHandlerCZL, event Inventory Posting To G/L.OnBeforeBufferOutputPosting
- Current Behavior: Rounding + CZ output branch.
- Problem: CRITICAL kolize s #10.
- Impact: Nedeterminismus posting pipeline.
- Proposed Solution: Sloučit do jednoho orchestrátoru.

### Finding #23

- Classification: B) PARTIAL LOGIC MODIFICATION
- Location: Codeunit InventoryPostingHandlerCZL, event Inventory Posting To G/L.OnBeforeBufferSalesPosting
- Current Behavior: Rounding sales branch.
- Problem: CRITICAL kolize s #9.
- Impact: Order-dependent postings.
- Proposed Solution: Jedna factory, jedna subscriber vstupní brána.

### Finding #24

- Classification: B) PARTIAL LOGIC MODIFICATION
- Location: Codeunit InventoryPostingHandlerCZL, event Inventory Posting To G/L.OnBeforeBufferConsumpPosting
- Current Behavior: Custom consump + WIP adjust.
- Problem: Komplexní logika přímo v subscriberu.
- Impact: Nízká testovatelnost a composability.
- Proposed Solution: IInvtConsumpPostingStrategy.

### Finding #25

- Classification: B) PARTIAL LOGIC MODIFICATION
- Location: Codeunit InventoryPostingHandlerCZL, event Inventory Posting To G/L.OnBeforeBufferPurchPosting
- Current Behavior: Rounding purchase branch.
- Problem: CRITICAL kolize s #8.
- Impact: Nedeterminismus.
- Proposed Solution: Merge do centrální deterministic bridge.

### Finding #26

- Classification: B) PARTIAL LOGIC MODIFICATION
- Location: Codeunit InventoryPostingHandlerCZL, event Inventory Posting To G/L.OnBeforeBufferAsmOutputPosting
- Current Behavior: Assembly output rounding override.
- Problem: IsHandled jako business branch killer.
- Impact: Dead-end pro další assembly customizace.
- Proposed Solution: IAsmPostingStrategy.ExecuteOutput.

### Finding #27

- Classification: B) PARTIAL LOGIC MODIFICATION
- Location: Codeunit InventoryPostingHandlerCZL, event Inventory Posting To G/L.OnBeforeBufferAsmConsumpPosting
- Current Behavior: Assembly consump rounding override.
- Problem: Totéž jako #26.
- Impact: Totéž.
- Proposed Solution: IAsmPostingStrategy.ExecuteConsumption.

### Finding #28

- Classification: B) PARTIAL LOGIC MODIFICATION
- Location: Codeunit InventoryPostingHandlerCZL, event Inventory Posting To G/L.OnBeforeBufferAdjmtPosting
- Current Behavior: Adjustment rounding override.
- Problem: IsHandled branch dead-end.
- Impact: Blokuje další adjustment extension logiku.
- Proposed Solution: IInvtAdjustmentStrategy.

### Finding #29

- Classification: D) DEAD-END EVENT (EXTENSIBILITY BREAK)
- Location: Codeunit NavigateHandlerCZL, event Navigate.OnBeforeShowRecords
- Current Behavior: Přepis zobrazení záznamů a handled.
- Problem: Event kidnapped bez dalších hooků.
- Impact: EXTENSIBILITY BREAK.
- Proposed Solution: Bridge + OnBeforeCustomNavigate/OnAfterCustomNavigate.

### Finding #30

- Classification: B) PARTIAL LOGIC MODIFICATION
- Location: Codeunit NonDeductibleVATHandlerCZL, event Non-Deductible VAT.OnBeforeGetNonDeductibleVATPctForPurchLine
- Current Behavior: Custom retrieval non-deductible VAT %.
- Problem: Implicitní override přes IsHandled.
- Impact: Hidden coupling na lokalizační pravidla.
- Proposed Solution: INonDedVATPctStrategy.

### Finding #31

- Classification: B) PARTIAL LOGIC MODIFICATION
- Location: Codeunit NonDeductibleVATHandlerCZL, event Non-Deductible VAT.OnBeforeGetNonDedVATPctForGenJnlLine
- Current Behavior: Custom retrieval pro journal.
- Problem: Totéž jako #30.
- Impact: Totéž.
- Proposed Solution: INonDedVATPctStrategy.

### Finding #32

- Classification: C) VALIDATION / SIDE EFFECT
- Location: Codeunit PurchasePostingHandlerCZL, event Purch.-Post.OnBeforeTestPurchLineItemCharge
- Current Behavior: Podmíněné přeskočení item charge validace.
- Problem: Validation bypass.
- Impact: Potenciální datová nekonzistence.
- Proposed Solution: Explicitní ItemChargeValidationPolicy service.

### Finding #33

- Classification: D) DEAD-END EVENT (EXTENSIBILITY BREAK)
- Location: Codeunit PurchInvHeaderEditCZL, event Vend. Entry-Edit.OnBeforeOnRun
- Current Behavior: Okamžité handled.
- Problem: Unesení flow.
- Impact: EXTENSIBILITY BREAK.
- Proposed Solution: Explicitní edit mode strategy, ne implicitní IsHandled.

### Finding #34

- Classification: D) DEAD-END EVENT (EXTENSIBILITY BREAK)
- Location: Codeunit ReconciliationHandlerCZL, event Reconciliation.OnBeforeSaveNetChange
- Current Behavior: Okamžité handled.
- Problem: Unesení save flow.
- Impact: EXTENSIBILITY BREAK.
- Proposed Solution: Save policy service + integrační eventy.

### Finding #35

- Classification: C) VALIDATION / SIDE EFFECT
- Location: Codeunit SalesPostingHandlerCZL, event Sales-Post.OnBeforeTestSalesLineItemCharge
- Current Behavior: Podmíněné přeskočení item charge validace.
- Problem: Validation bypass.
- Impact: Nekonzistentní behavior oproti jiným extension pravidlům.
- Proposed Solution: Sdílená purchase/sales validation policy.

### Finding #36

- Classification: D) DEAD-END EVENT (EXTENSIBILITY BREAK)
- Location: Codeunit UserSetupHandlerCZL, event Error Message.OnDrillDownSource
- Current Behavior: Custom drilldown a handled.
- Problem: Neexistuje re-expozice hooků.
- Impact: EXTENSIBILITY BREAK.
- Proposed Solution: Drilldown bridge + before/after events.

### Finding #37

- Classification: B) PARTIAL LOGIC MODIFICATION
- Location: Codeunit VATCorrNotifHandlerCZL, event Purchase Invoice.OnPostDocumentBeforeNavigateAfterPosting
- Current Behavior: Notification flow + handled.
- Problem: Hijack navigate-after-posting flow.
- Impact: Potlačení dalších post-posting rozšíření.
- Proposed Solution: PostNavigateBridge bez tvrdého ukončení base flow.

### Finding #38

- Classification: B) PARTIAL LOGIC MODIFICATION
- Location: Codeunit VATCorrNotifHandlerCZL, event Purchase Credit Memo.OnPostDocumentBeforeNavigateAfterPosting
- Current Behavior: Stejný pattern jako #37.
- Problem: Totéž.
- Impact: Totéž.
- Proposed Solution: Sdílený deterministic bridge.

### Finding #39

- Classification: B) PARTIAL LOGIC MODIFICATION
- Location: Codeunit VATCorrNotifHandlerCZL, event Sales Invoice.OnPostDocumentBeforeNavigateAfterPosting
- Current Behavior: Stejný pattern pro sales invoice.
- Problem: Totéž.
- Impact: Totéž.
- Proposed Solution: Sdílený deterministic bridge.

### Finding #40

- Classification: B) PARTIAL LOGIC MODIFICATION
- Location: Codeunit VATCorrNotifHandlerCZL, event Sales Credit Memo.OnPostDocumentBeforeNavigateAfterPosting
- Current Behavior: Stejný pattern pro sales credit memo.
- Problem: Totéž.
- Impact: Totéž.
- Proposed Solution: Sdílený deterministic bridge.

### Finding #41

- Classification: C) VALIDATION / SIDE EFFECT
- Location: Codeunit VATRegLogSuppressionCZL, event Customer.OnBeforeVATRegistrationValidation
- Current Behavior: Nahrazuje standardní validation flow.
- Problem: Validation hijack + coupling na custom log.
- Impact: Nízká transparentnost validačního výsledku.
- Proposed Solution: IVATValidationStrategy + result object.

### Finding #42

- Classification: C) VALIDATION / SIDE EFFECT
- Location: Codeunit VATRegLogSuppressionCZL, event Vendor.OnBeforeVATRegistrationValidation
- Current Behavior: Stejný pattern jako #41.
- Problem: Totéž.
- Impact: Totéž.
- Proposed Solution: Sdílená validator orchestrace.

### Finding #43

- Classification: C) VALIDATION / SIDE EFFECT
- Location: Codeunit VATRegLogSuppressionCZL, event Contact.OnBeforeVATRegistrationValidation
- Current Behavior: Stejný pattern jako #41.
- Problem: Totéž.
- Impact: Totéž.
- Proposed Solution: Sdílená validator orchestrace.

### Finding #44

- Classification: B) PARTIAL LOGIC MODIFICATION
- Location: Codeunit VATStatementHandlerCZL, event VAT Statement.OnBeforeCalcLineTotalWithBase
- Current Behavior: Přepis výpočtu total/base.
- Problem: IsHandled používán jako implicitní přepínač výpočtové větve.
- Impact: Dead-end pro další výpočetní extension body.
- Proposed Solution: IVATStatementCalcStrategy + deterministic selector.

---

## Referenční deterministic adapter pattern (subscriber bez business logiky)

```al
codeunit 70010 "Subscriber Adapter CZL"
{
    [EventSubscriber(ObjectType::Codeunit, Codeunit::"Gen. Jnl.-Post Line", 'OnInitVATOnBeforeVATPostingSetupCheck', '', false, false)]
    local procedure OnInitVATOnBeforeVATPostingSetupCheck(var GenJournalLine: Record "Gen. Journal Line"; var GLEntry: Record "G/L Entry"; var VATPostingSetup: Record "VAT Posting Setup"; var IsHandled: Boolean)
    var
        Bridge: Codeunit "VAT Posting Bridge CZL";
    begin
        Bridge.Execute(GenJournalLine, GLEntry, VATPostingSetup, IsHandled);
    end;
}
```

## Doporučené pořadí refaktoringu

1. Inventory Posting kolize (#8/#9/#10 + #22/#23/#25) jako první
2. GlobalTriggerManagement hard dead-endy (#18-#21)
3. VAT validation bypassy (#12, #41-#43)
4. Reporting a navigation overrides (#1, #2, #37-#40, #44)

## Cílový stav

Transformace z:

- implicit event override chaos

na:

- explicit deterministic orchestration
- jeden subscriber vstup na doménu
- business logika mimo subscriber
- re-expozice extension hooků přes OnBeforeCustomX / OnAfterCustomX
