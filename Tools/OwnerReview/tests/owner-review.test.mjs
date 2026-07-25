import test from "node:test";
import assert from "node:assert/strict";
import { acceptanceWarnings, buildSourceUrl, canonicalLf, createEmptyRecordReview, extractSourceCitations, generateMarkdownReport, normalizeSession, parseJsonl, reportFilename, sha256Hex, validateBatchManifest, validateGeneratedReport } from "../core.js";
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
test("canonical LF normalizes CRLF and lone CR", () => assert.equal(canonicalLf("A\r\nB\rC\n"),"A\nB\nC\n"));
test("accepts the original worksheet and matching manifest", () => {
  const records=makeRecords(),manifest=makeManifest(records);assert.equal(validateBatchManifest(manifest,records,"original").fingerprintMatches,true);
});
test("accepts mutable screening changes without changing population identity", () => {
  const records=makeRecords();records[0].screening_status="Ready for Prior-Knowledge Labeling";records[0].screening_observations=["Updated"];
  const validation=validateBatchManifest(makeManifest(makeRecords()),records,"changed");
  assert.equal(validation.fingerprintMatches,false);assert.match(validation.warning,/original batch-planning input/);
});
test("CZCS-B01 remains selectable after screening-field changes", () => {
  const records=makeRecords();records[0].screening_status="Ready for Prior-Knowledge Labeling";
  const manifest=makeManifest(makeRecords());validateBatchManifest(manifest,records,"changed");
  assert.deepEqual(manifest.batches[0].inventory_ids,["CZPOP-0001","CZPOP-0002"]);
});
test("missing and duplicate dataset inventory IDs are rejected", () => {
  const missing=makeRecords();delete missing[0].inventory_id;
  assert.throws(()=>validateBatchManifest(makeManifest(makeRecords()),missing,"original"),/inventory_id/);
  const duplicate=makeRecords();duplicate[1].inventory_id=duplicate[0].inventory_id;
  assert.throws(()=>validateBatchManifest(makeManifest(makeRecords()),duplicate,"original"),/unique/);
});
test("unknown, replaced, or reordered population IDs are rejected", () => {
  const original=makeRecords(),manifest=makeManifest(original);
  const replaced=makeRecords();replaced[1].inventory_id="CZPOP-9999";
  assert.throws(()=>validateBatchManifest(manifest,replaced,"changed"),/differs/);
  const reordered=makeRecords();[reordered[0],reordered[1]]=[reordered[1],reordered[0]];
  assert.throws(()=>validateBatchManifest(manifest,reordered,"changed"),/differs/);
});
test("incomplete and duplicate batch membership are rejected", () => {
  const records=makeRecords(),incomplete=makeManifest(records);incomplete.batches.pop();incomplete.batch_count=1;
  assert.throws(()=>validateBatchManifest(incomplete,records,"original"),/contain 2 records|complete loaded population/);
  const duplicate=makeManifest(records);duplicate.batches[1].inventory_ids[0]="CZPOP-0002";duplicate.batches[1].first_inventory_id="CZPOP-0002";
  assert.throws(()=>validateBatchManifest(duplicate,records,"original"),/duplicate/);
});
test("record count, range, and inventory IDs must agree", () => {
  const records=makeRecords();
  const count=makeManifest(records);count.record_count=3;assert.throws(()=>validateBatchManifest(count,records,"original"),/record_count/);
  const range=makeManifest(records);range.batches[0].last_inventory_id="CZPOP-9999";assert.throws(()=>validateBatchManifest(range,records,"original"),/last_inventory_id/);
  const members=makeManifest(records);members.batches[0].record_count=1;assert.throws(()=>validateBatchManifest(members,records,"original"),/record_count/);
});
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
test("Markdown report contains only the active batch scope", () => {
  const session=makeSession("fp");session.scopeLabel="Batch CZCS-B01";
  for(const id of ["CZPOP-0001","CZPOP-0002","CZPOP-0003"])session.reviews[id]=createEmptyRecordReview();
  const report=generateMarkdownReport(session,["CZPOP-0001","CZPOP-0002"]);
  assert.match(report,/Active scope: Batch CZCS-B01/);assert.match(report,/Records in scope: 2/);assert.doesNotMatch(report,/CZPOP-0003/);
});
test("generated report is governed",()=>{const s=makeSession("fp");s.scopeLabel="Batch CZCS-B01";const r=generateMarkdownReport(s,["CZPOP-0001"]);assert.equal(validateGeneratedReport(r),true);assert.match(r,/evidence: Verified/);assert.equal(reportFilename(s,["CZPOP-0001"]),"BCApps_CZ_Coarse_Screen_Owner_Review_CZCS_B01.md");});

function makeSession(fingerprint){return {dataset:{fileName:"input.jsonl",fingerprint,recordCount:1},bcAppsRef:CONFIG.defaultRef,scopeLabel:"Test data",reviews:{}};}
function makeRecords(){return ["CZPOP-0001","CZPOP-0002","CZPOP-0003","CZPOP-0004"].map(inventory_id=>({inventory_id,screening_status:"Not Screened",screening_observations:[]}));}
function makeManifest(records){
  const batches=[records.slice(0,2),records.slice(2,4)].map((members,index)=>({batch_id:`CZCS-B0${index+1}`,first_inventory_id:members[0].inventory_id,last_inventory_id:members.at(-1).inventory_id,record_count:members.length,inventory_ids:members.map(record=>record.inventory_id)}));
  return {manifest_version:"1.0.0",worksheet_sha256_lf:"original",batch_size:2,record_count:records.length,batch_count:batches.length,batches};
}
