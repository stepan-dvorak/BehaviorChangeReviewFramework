import test from "node:test";
import assert from "node:assert/strict";
import { acceptanceWarnings, buildSourceUrl, createEmptyRecordReview, extractSourceCitations, generateMarkdownReport, normalizeSession, parseJsonl, sha256Hex } from "../core.js";
import { CONFIG } from "../config.js";

const line = (id) => JSON.stringify({ inventory_id: id, screening_observations: [] });

test("loads valid JSONL, ignores blank lines, and preserves order", () => {
  assert.deepEqual(parseJsonl(`${line("CZPOP-0002")}\n\n${line("CZPOP-0001")}\n`).map(r => r.inventory_id), ["CZPOP-0002", "CZPOP-0001"]);
});
test("reports the exact invalid line", () => assert.throws(() => parseJsonl(`${line("CZPOP-0001")}\n\n{"bad"`), /line 3/));
test("inventory IDs can be indexed without reordering", () => {
  const records=parseJsonl(`${line("A")}\n${line("B")}`), index=new Map(records.map(r=>[r.inventory_id,r])); assert.equal(index.get("B").inventory_id,"B");
});
test("recognizes ranges, strips punctuation, and finds multiple citations", () => {
  const text="Subscriber body: src/Apps/A.Codeunit.al:19-36. Established: src/Layers/B.Codeunit.al:700-846).";
  assert.deepEqual(extractSourceCitations(text).map(x=>[x.path,x.startLine,x.endLine]),[["src/Apps/A.Codeunit.al",19,36],["src/Layers/B.Codeunit.al",700,846]]);
});
test("generates fixed-commit and main GitHub links", () => {
  const citation=extractSourceCitations("src/Apps/A.Codeunit.al:19-36.")[0];
  assert.equal(buildSourceUrl(citation),`https://github.com/microsoft/BCApps/blob/${CONFIG.defaultRef}/src/Apps/A.Codeunit.al#L19-L36`);
  assert.equal(buildSourceUrl(citation,"main"),"https://github.com/microsoft/BCApps/blob/main/src/Apps/A.Codeunit.al#L19-L36");
});
test("rejects unsafe citation paths and refs", () => {
  assert.throws(()=>buildSourceUrl({path:"src/../secret",startLine:1,endLine:null}),/Unsafe/);
  const citation={path:"src/A.al",startLine:1,endLine:null};assert.match(buildSourceUrl(citation,"javascript:alert(1)"),new RegExp(CONFIG.defaultRef));
});
test("HTML and script input remains plain data in parsing and Markdown", () => {
  const payload="<script>alert(1)</script>"; const record=parseJsonl(JSON.stringify({inventory_id:"X",value:payload}))[0];assert.equal(record.value,payload);
  const session=makeSession("fp");session.reviews.X=createEmptyRecordReview();session.reviews.X.result="Accepted";session.reviews.X.ownerNotes=payload;
  assert.match(generateMarkdownReport(session,["X"]),/<script>alert\(1\)<\/script>/);
});
test("fingerprint binds imported sessions to the dataset", () => assert.throws(()=>normalizeSession(makeSession("other"),"expected"),/fingerprint/));
test("import replaces an unsafe BCApps ref with the fixed commit", () => {
  const session=makeSession("fp");session.bcAppsRef="javascript:alert(1)";assert.equal(normalizeSession(session,"fp").bcAppsRef,CONFIG.defaultRef);
});
test("session exports and imports without losing review data", () => {
  const original=makeSession("fp");original.reviews.X=createEmptyRecordReview();original.reviews.X.ownerNotes="retained";
  const imported=normalizeSession(JSON.parse(JSON.stringify(original)),"fp");assert.equal(imported.reviews.X.ownerNotes,"retained");
});
test("SHA-256 fingerprint is stable", async () => assert.equal(await sha256Hex("abc"),"ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"));
test("Markdown report never claims that Not Reviewed records were reviewed", () => {
  const report=generateMarkdownReport(makeSession("fp"),["A"]);assert.match(report,/Reviewed inventory IDs: None/);assert.match(report,/Owner review: Incomplete/);assert.doesNotMatch(report,/Owner review: Accepted/);
});
test("Accepted with incomplete required areas produces warnings", () => {
  const review=createEmptyRecordReview();review.result="Accepted";assert.ok(acceptanceWarnings(review).length>0);review.areas.subscriber_identity.result="Correction Required";assert.match(acceptanceWarnings(review).join("\n"),/Correction Required/);
});
test("inconsistent Accepted record cannot produce an accepted checkpoint", () => {
  const session=makeSession("fp");session.reviews.A=createEmptyRecordReview();session.reviews.A.result="Accepted";
  const report=generateMarkdownReport(session,["A"]);assert.match(report,/Owner review: Incomplete/);assert.doesNotMatch(report,/Owner review: Accepted/);
});
test("complete accepted report has required checkpoint wording", () => {
  const session=makeSession("fp"),review=createEmptyRecordReview();review.result="Accepted";for(const area of Object.values(review.areas))area.result="Correct";session.reviews.A=review;
  const report=generateMarkdownReport(session,["A"]);assert.match(report,/Owner review: Accepted/);assert.match(report,/Workflow fields unchanged: Yes/);assert.match(report,/Additional notes: None/);
});

function makeSession(fingerprint){return {dataset:{fileName:"input.jsonl",fingerprint,recordCount:1},bcAppsRef:CONFIG.defaultRef,scopeLabel:"Test data",reviews:{}};}
