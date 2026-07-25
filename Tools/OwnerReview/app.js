import { CONFIG } from "./config.js";
import { AREA_DEFINITIONS, AREA_RESULTS, RECORD_RESULTS, acceptanceWarnings, buildSourceUrl, canonicalLf, createEmptyRecordReview, extractSourceCitations, generateMarkdownReport, normalizeSession, parseJsonl, reportFilename, sha256Hex, validateBatchManifest, validateGeneratedReport } from "./core.js";

const $ = (id) => document.getElementById(id);
const state = { records: [], byId: new Map(), fingerprint: "", lfFingerprint: "", fileName: "", session: null, manifest: null, scopeIds: [], currentId: null, filter: "All" };

function showMessage(message = "", kind = "error") { $("message").textContent = message; $("message").className = message ? `message-${kind}` : ""; }
function storageKey() { return `${CONFIG.storagePrefix}${state.fingerprint}`; }
function getReview(id) { return state.session.reviews[id] ||= createEmptyRecordReview(); }
function save() { state.session.updatedAt = new Date().toISOString(); localStorage.setItem(storageKey(), JSON.stringify(state.session)); $("saveState").textContent = `Saved locally · ${new Date().toLocaleTimeString()}`; }
function setControls(enabled) { for (const id of ["batchSelect","rangeInput","applyRange","exportMd","exportJson","sessionFile","clearSession"]) $(id).disabled = !enabled; $("importLabel").classList.toggle("disabled", !enabled); }

async function loadDataset(file) {
  showMessage();
  try {
    const text = await file.text();
    const records = parseJsonl(text);
    const fingerprint = await sha256Hex(text), lfFingerprint = await sha256Hex(canonicalLf(text));
    state.records = records; state.byId = new Map(records.map((record) => [record.inventory_id, record])); state.fingerprint = fingerprint; state.lfFingerprint = lfFingerprint; state.fileName = file.name;
    const stored = localStorage.getItem(`${CONFIG.storagePrefix}${fingerprint}`);
    state.session = stored ? normalizeSession(JSON.parse(stored), fingerprint) : { format: "Orden OwnerReview Session", version: 1, dataset: { fileName: file.name, fingerprint, recordCount: records.length }, bcAppsRef: CONFIG.defaultRef, scopeLabel: "Entire dataset", reviews: {}, createdAt: new Date().toISOString(), updatedAt: null };
    state.scopeIds = records.map((record) => record.inventory_id); state.currentId = state.scopeIds[0];
    $("refSelect").value = state.session.bcAppsRef === "main" ? "main" : CONFIG.defaultRef;
    populateIds(); setControls(true); $("workspace").classList.remove("hidden"); render();
    showMessage(`${records.length} records loaded. SHA-256: ${fingerprint}`, "info"); save();
  } catch (error) { showMessage(error.message); }
}

function populateIds() { $("inventoryIds").replaceChildren(...state.records.map((record) => { const option=document.createElement("option"); option.value=record.inventory_id; return option; })); }

function addLinkedText(container, value) {
  const text = String(value ?? ""); let offset = 0;
  for (const citation of extractSourceCitations(text)) {
    container.append(document.createTextNode(text.slice(offset, citation.index + citation.text.length)));
    const link=document.createElement("a"); link.className="source-link"; link.textContent="Open source ↗"; link.target="_blank"; link.rel="noopener noreferrer"; link.href=buildSourceUrl(citation,state.session.bcAppsRef); container.append(link); offset=citation.index+citation.text.length;
  }
  container.append(document.createTextNode(text.slice(offset)));
}
function valueNode(value) {
  const node=document.createElement("div"); node.className="field-value";
  if (Array.isArray(value)) { const ul=document.createElement("ul"); for(const item of value){const li=document.createElement("li");addLinkedText(li,item);ul.append(li);} node.append(ul); }
  else if(value && typeof value==="object") node.textContent=JSON.stringify(value,null,2); else addLinkedText(node,value===null?"null":value);
  return node;
}
function dataSection(title, entries) {
  const section=document.createElement("section");section.className="data-section";const h=document.createElement("h4");h.textContent=title;section.append(h);
  for(const [name,value] of entries){const row=document.createElement("div");row.className="field";const label=document.createElement("div");label.className="field-name";label.textContent=name.replaceAll("_"," ");row.append(label,valueNode(value));section.append(row);} return section;
}
function renderSource(record) {
  const identity=["inventory_id","context_dataset_sha256","screening_protocol_version","screening_status","screened_by","screened_on"].map(k=>[k,record[k]]);
  const protectedFields=["prior_known","selection_status","trigger_status","checklist_status"].map(k=>[k,record[k]]);
  $("sourceSections").replaceChildren(dataSection("Identity and workflow state",identity),dataSection("Evidence availability",Object.entries(record.evidence_availability||{})),dataSection("Stratum indicators",[["stratum_indicators",record.stratum_indicators||[]]]),dataSection("Screening observations",[["screening_observations",record.screening_observations||[]]]),dataSection("Targeted search questions",[["targeted_search_questions",record.targeted_search_questions||[]],["unavailability_reason",record.unavailability_reason]]),dataSection("Protected downstream fields",protectedFields));
  $("rawJson").textContent=JSON.stringify(record,null,2);
}
function inputField(labelText,value,onInput,textarea=false){const label=document.createElement("label");label.textContent=labelText;const input=document.createElement(textarea?"textarea":"input");if(textarea)input.rows=2;input.value=value||"";input.addEventListener("input",()=>onInput(input.value));label.append(input);return label;}
function renderReview(review) {
  const nodes=AREA_DEFINITIONS.map(([key,label])=>{const area=review.areas[key];const box=document.createElement("section");box.className=`review-area ${area.result.toLowerCase().replaceAll(" ","-")}`;const header=document.createElement("header");const h=document.createElement("h4");h.textContent=label;const select=document.createElement("select");for(const result of AREA_RESULTS){const o=document.createElement("option");o.value=o.textContent=result;select.append(o);}select.value=area.result;select.addEventListener("change",()=>{area.result=select.value;review.updatedAt=new Date().toISOString();save();renderReview(review);renderList();renderWarning(review);});header.append(h,select);box.append(header);if(area.result==="Correction Required"){const fields=document.createElement("div");fields.className="correction-fields";fields.append(inputField("Issue",area.issue,v=>{area.issue=v;save();}),inputField("Expected correction",area.expectedCorrection,v=>{area.expectedCorrection=v;save();}),inputField("Optional note",area.note,v=>{area.note=v;save();},true));box.append(fields);}return box;});$("reviewAreas").replaceChildren(...nodes);
  $("overallResult").value=review.result;$("ownerNotes").value=review.ownerNotes;renderWarning(review);
}
function renderWarning(review){const warnings=acceptanceWarnings(review);const box=$("acceptanceWarning");box.replaceChildren();box.classList.toggle("hidden",!warnings.length);if(warnings.length){box.append(document.createTextNode("Accepted is inconsistent with required area results:"));const ul=document.createElement("ul");for(const warning of warnings){const li=document.createElement("li");li.textContent=warning;ul.append(li);}box.append(ul);}}
function filteredIds(){return state.scopeIds.filter(id=>state.filter==="All"||getReview(id).result===state.filter);}
function renderList(){const nodes=filteredIds().map(id=>{const button=document.createElement("button");button.className=`record-item ${id===state.currentId?"active":""}`;const dot=document.createElement("span");const result=getReview(id).result;dot.className=`status-dot ${result==="Accepted"?"accepted":result==="Correction Required"?"correction":""}`;button.append(dot,document.createTextNode(id));button.addEventListener("click",()=>{state.currentId=id;render();});return button;});$("recordList").replaceChildren(...nodes);}
function render(){if(!state.currentId||!state.byId.has(state.currentId))return;const record=state.byId.get(state.currentId),review=getReview(state.currentId);$("recordId").textContent=state.currentId;const index=state.scopeIds.indexOf(state.currentId);$("position").textContent=`${index+1} / ${state.scopeIds.length} · dataset ${state.records.length}`;renderSource(record);renderReview(review);renderList();$("idSearch").value=state.currentId;$("previous").disabled=index<=0;$("next").disabled=index>=state.scopeIds.length-1;}
function navigate(delta){const ids=filteredIds();let index=ids.indexOf(state.currentId);if(index<0)index=delta>0?-1:ids.length;const target=ids[index+delta];if(target){state.currentId=target;render();}}
function applyScope(ids,label){const valid=ids.filter(id=>state.byId.has(id));if(!valid.length){showMessage("The selected scope contains no records from the loaded dataset.");return;}state.scopeIds=valid;state.session.scopeLabel=label;state.currentId=valid[0];save();render();showMessage(`${label}: ${valid.length} records`,"info");}
function download(name,content,type){const blob=new Blob([content],{type});const url=URL.createObjectURL(blob);const a=document.createElement("a");a.href=url;a.download=name;a.click();setTimeout(()=>URL.revokeObjectURL(url),0);}

$("fixedRefOption").value=CONFIG.defaultRef;$("fixedRefOption").textContent=`fixed commit (${CONFIG.defaultRef.slice(0,12)}…)`;for(const result of RECORD_RESULTS){const o=document.createElement("option");o.value=o.textContent=result;$("overallResult").append(o);}
$("jsonlFile").addEventListener("change",e=>e.target.files[0]&&loadDataset(e.target.files[0]));
$("manifestFile").addEventListener("change",async e=>{try{if(!state.records.length)throw new Error("Load the JSONL dataset first.");const manifest=JSON.parse(await e.target.files[0].text());const validation=validateBatchManifest(manifest,state.records,state.lfFingerprint);state.manifest=manifest;const options=[new Option("Entire dataset","")];for(const b of manifest.batches)options.push(new Option(`${b.batch_id} (${b.record_count})`,b.batch_id));$("batchSelect").replaceChildren(...options);showMessage(validation.warning||`${manifest.batches.length} batches loaded.`,"info");}catch(error){showMessage(`Invalid batch manifest: ${error.message}`);}});
$("batchSelect").addEventListener("change",()=>{const id=$("batchSelect").value;if(!id)return applyScope(state.records.map(r=>r.inventory_id),"Entire dataset");const batch=state.manifest.batches.find(b=>b.batch_id===id);applyScope(batch.inventory_ids,`Batch ${id}`);});
$("applyRange").addEventListener("click",()=>{const [first,last]=$("rangeInput").value.trim().split(/\s*[:–-]\s*(?=CZPOP)/);const a=state.records.findIndex(r=>r.inventory_id===first),b=state.records.findIndex(r=>r.inventory_id===last);if(a<0||b<a)return showMessage("Enter a valid inclusive range, for example CZPOP-0001:CZPOP-0016.");applyScope(state.records.slice(a,b+1).map(r=>r.inventory_id),`Range ${first} through ${last}`);});
$("statusFilter").addEventListener("change",()=>{state.filter=$("statusFilter").value;renderList();});$("idSearch").addEventListener("change",()=>{const id=$("idSearch").value.trim();if(state.scopeIds.includes(id)){state.currentId=id;render();}else showMessage(`${id} is not in the active scope.`);});
$("previous").addEventListener("click",()=>navigate(-1));$("next").addEventListener("click",()=>navigate(1));
$("overallResult").addEventListener("change",()=>{const review=getReview(state.currentId);review.result=$("overallResult").value;review.updatedAt=new Date().toISOString();save();renderWarning(review);renderList();});
$("ownerNotes").addEventListener("input",()=>{getReview(state.currentId).ownerNotes=$("ownerNotes").value;save();});
$("refSelect").addEventListener("change",()=>{state.session.bcAppsRef=$("refSelect").value;save();renderSource(state.byId.get(state.currentId));});
$("exportMd").addEventListener("click",()=>{try{const report=generateMarkdownReport(state.session,state.scopeIds);validateGeneratedReport(report);const name=reportFilename(state.session,state.scopeIds);download(name,report,"text/markdown");showMessage(`${name} exported. Move it into Empirical/ and register it with Register_OwnerReview_Report.bat.`,"info");}catch(error){showMessage(`Report export failed: ${error.message}`);}});
$("exportJson").addEventListener("click",()=>download("OwnerReview_Session.json",JSON.stringify(state.session,null,2)+"\n","application/json"));
$("sessionFile").addEventListener("change",async e=>{try{state.session=normalizeSession(JSON.parse(await e.target.files[0].text()),state.fingerprint);localStorage.setItem(storageKey(),JSON.stringify(state.session));$("refSelect").value=state.session.bcAppsRef==="main"?"main":CONFIG.defaultRef;render();showMessage("Review session imported and saved locally.","info");}catch(error){showMessage(error.message);}});
$("clearSession").addEventListener("click",()=>{if(!confirm("Delete all locally saved review data for this dataset? Export the session first if it may be needed."))return;localStorage.removeItem(storageKey());state.session={format:"Orden OwnerReview Session",version:1,dataset:{fileName:state.fileName,fingerprint:state.fingerprint,recordCount:state.records.length},bcAppsRef:CONFIG.defaultRef,scopeLabel:"Entire dataset",reviews:{},createdAt:new Date().toISOString(),updatedAt:null};state.scopeIds=state.records.map(r=>r.inventory_id);state.currentId=state.scopeIds[0];render();save();showMessage("The local review session was cleared.","info");});
document.addEventListener("keydown",e=>{if(e.target.matches("input,textarea,select")||e.ctrlKey||e.metaKey||e.altKey)return;if(e.key==="ArrowLeft")navigate(-1);if(e.key==="ArrowRight")navigate(1);});
