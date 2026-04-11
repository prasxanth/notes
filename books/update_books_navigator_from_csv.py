#!/usr/bin/env python3
"""
update_books_navigator_from_csv.py
Reads books_db.csv and injects JSON data into the embeddedData script block
in books_navigator_mobile.html (or any target HTML with that block).
"""
import json
import pathlib
import re
import sys

import pandas as pd

CSV_PATH  = pathlib.Path("books_db.csv")
HTML_PATH = pathlib.Path("books_navigator_mobile.html")

# Allow overrides from the command line:
#   python update_books_navigator_from_csv.py my_books.csv my_nav.html
if len(sys.argv) >= 2:
    CSV_PATH  = pathlib.Path(sys.argv[1])
if len(sys.argv) >= 3:
    HTML_PATH = pathlib.Path(sys.argv[2])


def split_semis(val):
    """Split a semicolon-delimited cell into a clean list."""
    if pd.isna(val):
        return []
    return [x.strip() for x in str(val).split(";") if x.strip()]


def build_records(df: pd.DataFrame) -> list[dict]:
    records = []
    for _, row in df.iterrows():
        themes = split_semis(row.get("Themes", ""))
        rec = {
            "title":    "" if pd.isna(row.get("Title",  "")) else str(row["Title"]).strip(),
            "author":   "" if pd.isna(row.get("Author", "")) else str(row["Author"]).strip(),
            "themes":   themes,
            "theme":    themes[0] if themes else "",
            "optional": {},
        }
        for col in df.columns:
            if col in {"Title", "Author", "Themes"}:
                continue
            val = row.get(col, "")
            if pd.isna(val):
                continue
            sval = str(val).strip()
            if sval:
                rec["optional"][col] = sval
        records.append(rec)
    return records


def main():
    if not CSV_PATH.exists():
        sys.exit(f"ERROR: CSV not found: {CSV_PATH}")
    if not HTML_PATH.exists():
        sys.exit(f"ERROR: HTML not found: {HTML_PATH}")

    df = pd.read_csv(CSV_PATH)
    records = build_records(df)

    html = HTML_PATH.read_text(encoding="utf-8", errors="ignore")
    pattern = r'(<script\s+id="embeddedData"\s+type="application/json">)([\s\S]*?)(</script>)'

    if not re.search(pattern, html, flags=re.DOTALL):
        sys.exit("ERROR: <script id=\"embeddedData\"> block not found in HTML.")

    updated = re.sub(
        pattern,
        lambda m: m.group(1) + json.dumps(records, ensure_ascii=False) + m.group(3),
        html,
        count=1,
        flags=re.DOTALL,
    )

    HTML_PATH.write_text(updated, encoding="utf-8")
    print(f"✓ Updated {HTML_PATH} from {CSV_PATH} — {len(records)} books injected.")


if __name__ == "__main__":
    main()
