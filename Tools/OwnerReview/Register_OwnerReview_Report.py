#!/usr/bin/env python3
from __future__ import annotations
import argparse,re,subprocess,sys
from datetime import date
from pathlib import Path
import yaml
ROOT=Path(__file__).resolve().parents[2]
def main():
 p=argparse.ArgumentParser();p.add_argument("report");a=p.parse_args();rp=(ROOT/a.report).resolve();rel=rp.relative_to(ROOT).as_posix();text=rp.read_text(encoding="utf-8");end=text.find("\n---\n",4);data=yaml.safe_load(text[4:end])
 if data.get("metadata_schema")!="1.0" or (data.get("document")or{}).get("type")!="Empirical Study":raise ValueError("invalid report metadata")
 if (data.get("quality")or{}).get("evidence") not in {"Pending","Partial","Verified","N/A"}:raise ValueError("invalid quality.evidence")
 for k in ("method","subject","data_access","reproducibility"):
  if not (data.get("study")or{}).get(k):raise ValueError(f"study.{k} is required")
 ix=ROOT/"Repository_Index.yaml";s=ix.read_text(encoding="utf-8")
 if not re.search(rf"(?m)^  - path: {re.escape(rel)}$",s):
  d=data["document"];c=data["classification"];purpose=" ".join(str(data["purpose"]).split());entry=f"  - path: {rel}\n    document_id: {d['id']}\n    title: {d['title']}\n    profile: governed_document\n    category: empirical_study\n    authority: evidentiary\n    status: {str(d['status']).lower()}\n    maturity: {str(c['maturity']).lower()}\n    version: {d['version']}\n    summary: {purpose}\n    use_for: [owner review, coarse-screen quality control, governed report evidence]\n\n";pos=s.index("\nnon_markdown_artifacts:\n");s=s[:pos]+entry+s[pos:];m=re.search(r"(?m)^  version: (\d+)\.(\d+)\.(\d+)$",s);x,y,z=map(int,m.groups());s=s[:m.start()]+f"  version: {x}.{y}.{z+1}"+s[m.end():];s=re.sub(r"(?m)^  generated_on: \d{4}-\d{2}-\d{2}$",f"  generated_on: {date.today().isoformat()}",s,count=1);ix.write_text(s,encoding="utf-8",newline="\n")
 raise SystemExit(subprocess.run([sys.executable,"Scripts/Validate_Repository_Metadata.py","--strict"],cwd=ROOT).returncode)
if __name__=="__main__":main()
