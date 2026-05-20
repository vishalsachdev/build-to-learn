#!/usr/bin/env python3
"""Assert-based tests for extract.py — no pytest dependency. Run: python3 buildtolearn/test_extract.py"""
import csv, json, shutil, sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
import extract  # noqa: E402

FIX = HERE / "_fixture_export" / "Complete_LinkedInDataExport_01-01-2099.zip"


def _write_fixture():
    if FIX.parent.exists():
        shutil.rmtree(FIX.parent)
    FIX.mkdir(parents=True)
    with open(FIX / "Shares.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["Date", "ShareLink", "ShareCommentary", "SharedUrl", "MediaUrl", "Visibility"])
        # 1. post-couplet, two tags
        w.writerow(["2026-03-12 15:45:35",
                    "https://www.linkedin.com/feed/update/urn%3Ali%3AugcPost%3A111",
                    "#MsbaAtGies students are builders #BuildToLearn and #LearnToBuild",
                    "", "", "MEMBER_NETWORK"])
        # 2. post-couplet, single tag with case variant
        w.writerow(["2025-12-08 00:52:28",
                    "https://www.linkedin.com/feed/update/urn%3Ali%3Ashare%3A222",
                    "#YouCanJustDoThings #TeachersAreBuilders #buildtolearn #LearnToBuild",
                    "", "", "MEMBER_NETWORK"])
        # 3. pre-couplet (no tag yet), but keyword-matched (MicroSim) — should be included
        w.writerow(["2023-05-01 09:00:00",
                    "https://www.linkedin.com/feed/update/urn%3Ali%3Aactivity%3A333",
                    "Students built a MicroSim in BADM 350 today",
                    "", "", "MEMBER_NETWORK"])
        # 4. pre-couplet AND post-couplet boundary: 2025-02-25 — first BTL date, should be post-couplet
        w.writerow(["2025-02-25 18:47:28",
                    "https://www.linkedin.com/feed/update/urn%3Ali%3AugcPost%3A444",
                    "So much to learn! ... #BuildToLearn",
                    "", "", "MEMBER_NETWORK"])
        # 5. completely unrelated — should be excluded
        w.writerow(["2024-01-01 08:00:00",
                    "https://www.linkedin.com/feed/update/urn%3Ali%3AugcPost%3A555",
                    "unrelated post about weather",
                    "", "", "MEMBER_NETWORK"])
        # 6. keyword Canvas MCP — should be included
        w.writerow(["2024-09-15 12:00:00",
                    "https://www.linkedin.com/feed/update/urn%3Ali%3Aactivity%3A666",
                    "Working on the Canvas MCP server for grading workflows",
                    "", "", "MEMBER_NETWORK"])


def main():
    _write_fixture()
    items = extract.collect(FIX)

    # 5 of 6 rows match (row 5 is unrelated)
    assert len(items) == 5, f"expected 5, got {len(items)}"

    # URL cleaning: %3A → :
    p1 = next(it for it in items if "111" in it["url"])
    assert p1["url"] == "https://www.linkedin.com/feed/update/urn:li:ugcPost:111", p1["url"]

    # tags_used populated by the script
    assert sorted(p1["tags_used"]) == ["#BuildToLearn", "#LearnToBuild"], p1["tags_used"]

    p2 = next(it for it in items if "222" in it["url"])
    # case-insensitive matching keeps canonical capitalization
    assert "#BuildToLearn" in p2["tags_used"] and "#LearnToBuild" in p2["tags_used"]
    assert "#TeachersAreBuilders" in p2["tags_used"]
    assert "#YouCanJustDoThings" in p2["tags_used"]

    # era binning
    post_first = next(it for it in items if "444" in it["url"])  # 2025-02-25 — boundary day
    assert post_first["era"] == "post-couplet", post_first["era"]

    pre = next(it for it in items if "333" in it["url"])  # 2023-05-01
    assert pre["era"] == "pre-couplet", pre["era"]

    # keyword-only inclusion (no tag)
    kw_micro = next(it for it in items if "333" in it["url"])
    assert kw_micro["tags_used"] == [], kw_micro["tags_used"]

    kw_canvas = next(it for it in items if "666" in it["url"])
    assert kw_canvas["era"] == "pre-couplet"
    assert kw_canvas["tags_used"] == []

    # themes/artifacts are blank by default
    assert all(it["themes"] == [] and it["artifacts"] == [] for it in items)

    # length_chars present
    assert p1["length_chars"] == len(p1["text"])

    # outputs
    out_dir = HERE / "_fixture_export"
    extract.write_outputs(items, out_dir)
    rows = list(csv.DictReader(open(out_dir / "corpus.csv", encoding="utf-8")))
    assert len(rows) == 5
    j = json.load(open(out_dir / "corpus.json", encoding="utf-8"))
    assert len(j) == 5

    # provenance: emit per-tag first/last/count for the tags that appeared
    prov = extract.provenance(items)
    btl = next(p for p in prov if p["tag"] == "#BuildToLearn")
    assert btl["first_date"].startswith("2025-02-25"), btl
    assert btl["total_uses"] == 3, btl  # rows 1, 2, 4
    extract.write_provenance(prov, out_dir)
    pr_rows = list(csv.DictReader(open(out_dir / "provenance.csv", encoding="utf-8")))
    assert any(r["tag"] == "#BuildToLearn" for r in pr_rows)

    # summary
    summ = extract.summarize(items)
    assert summ["total"] == 5
    assert summ["by_era"] == {"pre-couplet": 2, "post-couplet": 3}, summ["by_era"]

    shutil.rmtree(out_dir)
    print("OK — all extract.py tests passed")


if __name__ == "__main__":
    main()
