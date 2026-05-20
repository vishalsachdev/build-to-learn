#!/usr/bin/env python3
"""Extract #BuildToLearn / #LearnToBuild and related posts from a Complete LinkedIn export.

Usage:
    python3 extract.py [--export PATH] [--out DIR]

Defaults: newest ./Complete_LinkedInDataExport_*/ in the repo root; outputs into this
script's own directory (buildtolearn/).
"""
import argparse
import csv
import glob
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
COUPLET_DATE = "2025-02-25"  # first public use of #BuildToLearn

# Tags to detect; canonical capitalization is what we record in tags_used.
TAGS = [
    "#BuildToLearn", "#LearnToBuild",
    "#BuilderProf", "#BuilderProfs",
    "#TeachersAreBuilders", "#TeachByBuilding",
    "#PersonalSoftware",
    "#YouCanJustBuildThings", "#YouCanJustDoThings",
    "#WeAreBuilders",
    "#DigitalMaking",
    "#ClaudeCodeIsAllYouNeed",
]

# Compile case-insensitive matchers; tag is preserved in canonical form on match.
TAG_RES = [(t, re.compile(re.escape(t), re.IGNORECASE)) for t in TAGS]

# Substring keywords (case-insensitive) — include posts even without one of the tags above.
KEYWORDS = [
    "MicroSim", "MakerLab", "Canvas MCP",
    "AgentLab", "MindForum",
    "BADM 350", "BADM 372", "BADM 554",
    "build-a-thon", "buildathon",
    "vibe coding",
    "intelligent textbook",
    "productive struggle",
    "Grit-CART",
]
KEYWORD_RES = [re.compile(re.escape(k), re.IGNORECASE) for k in KEYWORDS]

URN_RE = re.compile(r"urn(?:%3A|:)li(?:%3A|:)(ugcPost|share|activity)(?:%3A|:)(\d+)", re.IGNORECASE)


def _clean_url(raw):
    m = URN_RE.search(raw or "")
    if not m:
        return (raw or "").strip()
    kind = m.group(1).lower()
    num = m.group(2)
    kind_norm = {"ugcpost": "ugcPost", "share": "share", "activity": "activity"}[kind]
    return f"https://www.linkedin.com/feed/update/urn:li:{kind_norm}:{num}"


def _detect_tags(text):
    return [canon for canon, rx in TAG_RES if rx.search(text or "")]


def _matches(text):
    if any(rx.search(text or "") for _, rx in TAG_RES):
        return True
    if any(rx.search(text or "") for rx in KEYWORD_RES):
        return True
    return False


def _record(date, url, text):
    date = (date or "").strip()
    year = int(date[:4]) if date[:4].isdigit() else 0
    text = (text or "").strip()
    return {
        "date": date,
        "year": year,
        "era": "post-couplet" if date >= COUPLET_DATE else "pre-couplet",
        "kind": "post",
        "url": _clean_url(url),
        "text": text,
        "length_chars": len(text),
        "tags_used": _detect_tags(text),
        "themes": [],
        "artifacts": [],
    }


def _newest_complete_export():
    cands = sorted(glob.glob(str(REPO_ROOT / "Complete_LinkedInDataExport_*")))
    if not cands:
        sys.exit("No Complete_LinkedInDataExport_* directory found in the repo root. "
                 "Unzip one there or pass --export PATH.")
    return Path(cands[-1])


def collect(export_dir):
    export_dir = Path(export_dir)
    items = []
    shares = export_dir / "Shares.csv"
    if shares.exists():
        with open(shares, newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                text = row.get("ShareCommentary", "")
                if _matches(text):
                    items.append(_record(row.get("Date"), row.get("ShareLink"), text))
    items.sort(key=lambda it: it["date"], reverse=True)
    return items


FIELDS = ["date", "year", "era", "kind", "url", "text", "length_chars",
          "tags_used", "themes", "artifacts"]


def write_outputs(items, out_dir):
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "corpus.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        for it in items:
            row = dict(it)
            for k in ("tags_used", "themes", "artifacts"):
                row[k] = "; ".join(row[k])
            w.writerow(row)
    with open(out_dir / "corpus.json", "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2, ensure_ascii=False)


def provenance(items):
    # one row per tag that appears at least once; sorted by total_uses desc.
    by_tag = {}
    for it in items:
        for tag in it["tags_used"]:
            by_tag.setdefault(tag, []).append(it)
    rows = []
    for tag, lst in by_tag.items():
        lst.sort(key=lambda it: it["date"])
        first, last = lst[0], lst[-1]
        rows.append({
            "tag": tag,
            "first_date": first["date"],
            "first_url": first["url"],
            "first_text_snippet": first["text"][:200],
            "total_uses": len(lst),
            "last_date": last["date"],
        })
    rows.sort(key=lambda r: -r["total_uses"])
    return rows


PROV_FIELDS = ["tag", "first_date", "first_url", "first_text_snippet", "total_uses", "last_date"]


def write_provenance(rows, out_dir):
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "provenance.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=PROV_FIELDS)
        w.writeheader()
        w.writerows(rows)


def summarize(items):
    by_era = {"pre-couplet": 0, "post-couplet": 0}
    by_year, by_tag = {}, {}
    for it in items:
        by_era[it["era"]] = by_era.get(it["era"], 0) + 1
        by_year[it["year"]] = by_year.get(it["year"], 0) + 1
        for t in it["tags_used"]:
            by_tag[t] = by_tag.get(t, 0) + 1
    dates = [it["date"] for it in items if it["date"]]
    return {
        "total": len(items),
        "by_era": by_era,
        "by_year": dict(sorted(by_year.items())),
        "by_tag": dict(sorted(by_tag.items(), key=lambda kv: -kv[1])),
        "date_span": (min(dates), max(dates)) if dates else (None, None),
    }


def _print_summary(summ):
    print(f"total relevant items: {summ['total']}")
    print(f"  by era: {summ['by_era']}")
    print(f"  by year: {summ['by_year']}")
    print(f"  by tag: {summ['by_tag']}")
    print(f"  date span: {summ['date_span'][0]} .. {summ['date_span'][1]}")


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--export", help="path to a Complete_LinkedInDataExport_* dir")
    p.add_argument("--out", help="output dir (default: this script's dir)")
    args = p.parse_args(argv)
    export_dir = Path(args.export) if args.export else _newest_complete_export()
    out_dir = Path(args.out) if args.out else Path(__file__).resolve().parent
    items = collect(export_dir)
    write_outputs(items, out_dir)
    prov = provenance(items)
    write_provenance(prov, out_dir)
    print(f"export: {export_dir}")
    print(f"wrote: {out_dir / 'corpus.csv'}, {out_dir / 'corpus.json'}, {out_dir / 'provenance.csv'}")
    _print_summary(summarize(items))


if __name__ == "__main__":
    main()
