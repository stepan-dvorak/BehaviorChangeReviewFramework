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

export function generateMarkdownReport(session, scopeIds) {
  const reviews = scopeIds.map((id) => [id, session.reviews[id] || createEmptyRecordReview()]);
  const counts = Object.fromEntries(RECORD_RESULTS.map((result) => [result, reviews.filter(([, review]) => review.result === result).length]));
  const done = reviewedIds(session, scopeIds);
  const inconsistentAccepted = reviews.some(([, review]) => acceptanceWarnings(review).length > 0);
  const allAccepted = reviews.length > 0 && counts.Accepted === reviews.length && !inconsistentAccepted;
  const hasCorrection = counts["Correction Required"] > 0;
  const checkpoint = hasCorrection ? "Correction Required" : allAccepted ? "Accepted" : "Incomplete";
  const reviewedList = done.length ? done.join(", ") : "None";
  const lines = [
    "# Owner Review Report", "",
    "> This report records owner-review results only. It does not modify or replace the source coarse-screen records.", "",
    "## Session", "",
    `- Input file: \`${md(session.dataset.fileName)}\``,
    `- Input SHA-256: \`${session.dataset.fingerprint}\``,
    `- Exported at: ${new Date().toISOString()}`,
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
