import { CONFIG } from "./config.js";

export const AREA_DEFINITIONS = Object.freeze([
  ["subscriber_identity", "Subscriber identity", true],
  ["subscriber_body", "Subscriber body", true],
  ["publisher_or_platform_evidence", "Publisher or platform evidence", true],
  ["raise_or_trigger_evidence", "Raise or trigger evidence", true],
  ["bounded_established_activity", "Bounded established activity", true],
  ["evidence_availability_values", "Evidence-availability values", true],
  ["screening_status", "Screening status", true],
  ["screening_observations", "Screening observations", true],
  ["targeted_questions_and_unavailability_reason", "Targeted questions and unavailability reason", true],
  ["protected_workflow_fields", "Protected workflow fields", true],
]);

export const AREA_RESULTS = ["Not Reviewed", "Correct", "Correction Required", "Not Applicable"];
export const RECORD_RESULTS = ["Not Reviewed", "Accepted", "Correction Required"];

export function parseJsonl(text) {
  const records = [];
  const ids = new Set();
  text.split(/\r?\n/).forEach((line, index) => {
    if (!line.trim()) return;
    let record;
    try { record = JSON.parse(line); }
    catch (error) { throw new Error(`Invalid JSON on line ${index + 1}: ${error.message}`); }
    if (!record || Array.isArray(record) || typeof record !== "object") {
      throw new Error(`Invalid record on line ${index + 1}: expected a JSON object.`);
    }
    if (typeof record.inventory_id !== "string" || !record.inventory_id.trim()) {
      throw new Error(`Invalid record on line ${index + 1}: inventory_id is required.`);
    }
    if (ids.has(record.inventory_id)) throw new Error(`Duplicate inventory_id on line ${index + 1}: ${record.inventory_id}.`);
    ids.add(record.inventory_id);
    records.push(record);
  });
  if (!records.length) throw new Error("The selected file contains no JSON records.");
  return records;
}

export async function sha256Hex(text) {
  const bytes = new TextEncoder().encode(text);
  const digest = await crypto.subtle.digest("SHA-256", bytes);
  return [...new Uint8Array(digest)].map((byte) => byte.toString(16).padStart(2, "0")).join("");
}

export function canonicalLf(text) {
  return String(text).replace(/\r\n?/g, "\n");
}

export function validateBatchManifest(manifest, records, worksheetLfFingerprint) {
  if (!manifest || Array.isArray(manifest) || typeof manifest !== "object") {
    throw new Error("Batch manifest must be a JSON object.");
  }
  if (!Array.isArray(manifest.batches) || !manifest.batches.length) {
    throw new Error("Batch manifest must contain a non-empty batches array.");
  }
  if (!Number.isInteger(manifest.record_count) || manifest.record_count !== records.length) {
    throw new Error(`Manifest record_count must equal the loaded dataset count (${records.length}).`);
  }
  if (!Number.isInteger(manifest.batch_count) || manifest.batch_count !== manifest.batches.length) {
    throw new Error(`Manifest batch_count must equal the number of batches (${manifest.batches.length}).`);
  }
  if (!Number.isInteger(manifest.batch_size) || manifest.batch_size < 1) {
    throw new Error("Manifest batch_size must be a positive integer.");
  }

  const datasetIds = records.map((record) => record.inventory_id);
  if (datasetIds.some((id) => typeof id !== "string" || !id.trim())) {
    throw new Error("Every loaded record must have an inventory_id.");
  }
  if (new Set(datasetIds).size !== datasetIds.length) {
    throw new Error("Loaded dataset inventory_id values must be unique.");
  }

  const batchIds = new Set();
  const manifestIds = [];
  let remaining = records.length;
  for (const [index, batch] of manifest.batches.entries()) {
    if (!batch || Array.isArray(batch) || typeof batch !== "object") {
      throw new Error(`Batch ${index + 1} must be a JSON object.`);
    }
    if (typeof batch.batch_id !== "string" || !batch.batch_id.trim()) {
      throw new Error(`Batch ${index + 1} must have a batch_id.`);
    }
    if (batchIds.has(batch.batch_id)) throw new Error(`Duplicate batch_id: ${batch.batch_id}.`);
    batchIds.add(batch.batch_id);
    if (!Array.isArray(batch.inventory_ids) || !batch.inventory_ids.length) {
      throw new Error(`${batch.batch_id} must contain a non-empty inventory_ids array.`);
    }

    const expectedSize = Math.min(manifest.batch_size, remaining);
    if (batch.inventory_ids.length !== expectedSize) {
      throw new Error(`${batch.batch_id} inventory_ids must contain ${expectedSize} records.`);
    }
    if (batch.record_count !== batch.inventory_ids.length) {
      throw new Error(`${batch.batch_id} record_count does not match inventory_ids.`);
    }
    if (batch.first_inventory_id !== batch.inventory_ids[0]) {
      throw new Error(`${batch.batch_id} first_inventory_id does not match inventory_ids.`);
    }
    if (batch.last_inventory_id !== batch.inventory_ids.at(-1)) {
      throw new Error(`${batch.batch_id} last_inventory_id does not match inventory_ids.`);
    }
    manifestIds.push(...batch.inventory_ids);
    remaining -= batch.inventory_ids.length;
  }

  if (remaining !== 0 || manifestIds.length !== datasetIds.length) {
    throw new Error("Batch membership does not cover the complete loaded population.");
  }
  if (new Set(manifestIds).size !== manifestIds.length) {
    throw new Error("Batch membership contains duplicate inventory_id values.");
  }
  const mismatch = datasetIds.findIndex((id, index) => manifestIds[index] !== id);
  if (mismatch !== -1) {
    throw new Error(`Batch population differs from the loaded dataset at position ${mismatch + 1}.`);
  }

  const fingerprintMatches = !manifest.worksheet_sha256_lf
    || manifest.worksheet_sha256_lf === worksheetLfFingerprint;
  return {
    fingerprintMatches,
    warning: fingerprintMatches
      ? ""
      : "The current worksheet fingerprint differs from the original batch-planning input; population identity and batch structure are valid.",
  };
}

const citationPattern = /\bsrc\/[A-Za-z0-9_./+() -]+?\.[A-Za-z0-9]+:\d+(?:-\d+)?(?=$|[\s,;.!?)}\]])/g;

export function extractSourceCitations(text) {
  const matches = [];
  for (const match of String(text).matchAll(citationPattern)) {
    const value = match[0];
    const parts = value.match(/^(src\/.+):(\d+)(?:-(\d+))?$/);
    if (!parts || parts[1].includes("..")) continue;
    matches.push({ index: match.index, text: value, path: parts[1], startLine: Number(parts[2]), endLine: parts[3] ? Number(parts[3]) : null });
  }
  return matches;
}

export function buildSourceUrl(citation, ref = CONFIG.defaultRef) {
  const safeRef = ref === "main" ? ref : /^[0-9a-f]{40}$/i.test(ref) ? ref : CONFIG.defaultRef;
  if (!citation.path.startsWith("src/") || citation.path.includes("..") || citation.startLine < 1) throw new Error("Unsafe source citation.");
  const encodedPath = citation.path.split("/").map(encodeURIComponent).join("/");
  const end = citation.endLine && citation.endLine >= citation.startLine ? `-L${citation.endLine}` : "";
  return `https://github.com/${CONFIG.repository}/blob/${safeRef}/${encodedPath}#L${citation.startLine}${end}`;
}

export function createEmptyRecordReview() {
  return {
    result: "Not Reviewed",
    ownerNotes: "",
    areas: Object.fromEntries(AREA_DEFINITIONS.map(([key]) => [key, { result: "Not Reviewed", issue: "", expectedCorrection: "", note: "" }])),
    updatedAt: null,
  };
}

export function acceptanceWarnings(review) {
  if (review.result !== "Accepted") return [];
  return AREA_DEFINITIONS.filter(([, , required]) => required).flatMap(([key, label]) => {
    const result = review.areas?.[key]?.result || "Not Reviewed";
    return result === "Not Reviewed" || result === "Correction Required" ? [`${label}: ${result}`] : [];
  });
}

export function normalizeSession(candidate, fingerprint) {
  if (!candidate || candidate.dataset?.fingerprint !== fingerprint) throw new Error("Session fingerprint does not match the loaded dataset.");
  const reviews = {};
  for (const [id, value] of Object.entries(candidate.reviews || {})) {
    const base = createEmptyRecordReview();
    reviews[id] = { ...base, ...value, areas: Object.fromEntries(AREA_DEFINITIONS.map(([key]) => [key, { ...base.areas[key], ...(value.areas?.[key] || {}) }])) };
  }
  const bcAppsRef = candidate.bcAppsRef === "main" || /^[0-9a-f]{40}$/i.test(candidate.bcAppsRef || "") ? candidate.bcAppsRef : CONFIG.defaultRef;
  return { ...candidate, bcAppsRef, reviews };
}

function md(value) { return String(value ?? "").replace(/\|/g, "\\|").replace(/\r?\n/g, " "); }
function reviewedIds(session, scopeIds) { return scopeIds.filter((id) => (session.reviews[id]?.result || "Not Reviewed") !== "Not Reviewed"); }
function scopeToken(session,scopeIds){const m=String(session.scopeLabel||"").match(/\bCZCS-B(\d+)\b/i);if(m)return `CZCS-B${m[1].padStart(2,"0")}`;return scopeIds.length?`${scopeIds[0]}-${scopeIds.at(-1)}`:"EMPTY-SCOPE";}
function reportMetadata(session,scopeIds){const token=scopeToken(session,scopeIds),m=token.match(/^CZCS-B(\d+)$/),id=m?`ES-BCAPPS-CZ-CLP-COARSE-SCREEN-OWNER-REVIEW-B${m[1]}-001`:`ES-BCAPPS-CZ-CLP-COARSE-SCREEN-OWNER-REVIEW-${token.replace(/[^A-Z0-9]+/gi,"-").toUpperCase()}-001`;const first=scopeIds[0]||"None",last=scopeIds.at(-1)||"None";return ["---",'metadata_schema: "1.0"',"","project:","  id: Orden","  name: Behavior Change Review Framework","","document:",`  id: ${id}`,`  title: BCApps Czech Coarse Screen Owner Review — ${token}`,"  type: Empirical Study","  version: 0.1.0","  status: Active","","classification:","  domain: Empirical Research","  layer: Evidence","  maturity: Review","","owner: Štěpán Dvořák","","purpose: >","  Records the repository owner's review of prepared BCApps Czech coarse-screen evidence","  without changing source records, screening classifications, or research conclusions.","","quality:","  review: Approved","  evidence: Verified","  editorial: Reviewed","","audience:","  - Researchers","  - Reviewers","  - AI Assistants","","depends_on:","  - Empirical/BCApps_CZ_Coarse_Screen_Execution_Protocol.md","  - Empirical/Data/BCApps_CZ_Coarse_Screen.jsonl","","study:","  method: Structured Owner Review of Prepared Coarse-Screen Evidence",`  subject: Coarse-screen scope ${token} (${first} through ${last})`,"  data_access: Retained Repository Dataset and Fixed BCApps Source Revision","  reproducibility: Generated Owner Review Report and Automated Regression Checks","","tags:","  - empirical","  - coarse-screen","  - owner-review","  - BCApps","---",""]; }
export function reportFilename(session,scopeIds){return `BCApps_CZ_Coarse_Screen_Owner_Review_${scopeToken(session,scopeIds).replace("-","_")}.md`;}
export function validateGeneratedReport(report){const required=[/^---\nmetadata_schema: "1\.0"/,/\ndocument:\n[\s\S]*?\n  type: Empirical Study\n/,/\nquality:\n  review: Approved\n  evidence: Verified\n  editorial: Reviewed\n/,/\nstudy:\n  method: .+\n  subject: .+\n  data_access: .+\n  reproducibility: .+\n/,/\n# Owner Review Report\n/,/\n## Checkpoint\n/];const failed=required.find(p=>!p.test(report));if(failed)throw new Error(`Generated report failed structural validation: ${failed}`);return true;}

export function generateMarkdownReport(session, scopeIds) {
  const reviews = scopeIds.map((id) => [id, session.reviews[id] || createEmptyRecordReview()]);
  const counts = Object.fromEntries(RECORD_RESULTS.map((result) => [result, reviews.filter(([, review]) => review.result === result).length]));
  const done = reviewedIds(session, scopeIds);
  const inconsistentAccepted = reviews.some(([, review]) => acceptanceWarnings(review).length > 0);
  const allAccepted = reviews.length > 0 && counts.Accepted === reviews.length && !inconsistentAccepted;
  const hasCorrection = counts["Correction Required"] > 0;
  const checkpoint = hasCorrection ? "Correction Required" : allAccepted ? "Accepted" : "Incomplete";
  const reviewedList = done.length ? done.join(", ") : "None";
  const exportedAt = new Date().toISOString();
  const lines = [
    ...reportMetadata(session, scopeIds),
    "# Owner Review Report", "",
    "> This report records owner-review results only. It does not modify or replace the source coarse-screen records.", "",
    "## Session", "",
    `- Input file: \`${md(session.dataset.fileName)}\``,
    `- Input SHA-256: \`${session.dataset.fingerprint}\``,
    `- Exported at: ${exportedAt}`,
    `- BCApps ref: \`${md(session.bcAppsRef)}\``,
    `- Active scope: ${md(session.scopeLabel || "Entire dataset")}`,
    `- Records in scope: ${scopeIds.length}`,
    `- Reviewed inventory IDs: ${reviewedList}`, "",
    "## Summary", "",
    `- Accepted: ${counts.Accepted}`,
    `- Correction Required: ${counts["Correction Required"]}`,
    `- Not Reviewed: ${counts["Not Reviewed"]}`, "",
    "## Results", "",
    "| Inventory ID | Owner-review result | Owner notes |",
    "|---|---|---|",
    ...reviews.map(([id, review]) => `| ${md(id)} | ${md(review.result)} | ${md(review.ownerNotes || "")} |`), "",
  ];
  const issues = [];
  for (const [id, review] of reviews) for (const [key, label] of AREA_DEFINITIONS) {
    const area = review.areas?.[key];
    if (area?.result === "Correction Required") issues.push([id, label, area.issue, area.expectedCorrection, area.note]);
  }
  if (issues.length) lines.push("## Required Corrections", "", "| Inventory ID | Area | Issue | Expected correction | Note |", "|---|---|---|---|---|", ...issues.map((row) => `| ${row.map(md).join(" | ")} |`), "");
  lines.push("## Checkpoint", "", `Owner review: ${checkpoint}`);
  if (allAccepted) {
    const workflowConfirmed = reviews.every(([, review]) => review.areas?.protected_workflow_fields?.result === "Correct");
    lines.push(`Workflow fields unchanged: ${workflowConfirmed ? "Yes" : "Not confirmed"}`, `Additional notes: ${reviews.some(([, r]) => r.ownerNotes.trim()) ? "See results table." : "None"}`);
  } else if (checkpoint === "Incomplete") lines.push(`The checkpoint is incomplete because ${inconsistentAccepted ? "one or more Accepted records have incomplete or contradictory required-area results" : "one or more records remain Not Reviewed"}.`);
  lines.push("");
  return lines.join("\n");
}

export function safeText(value) { return document.createTextNode(String(value ?? "")); }
