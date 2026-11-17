"""
Scan PDF pages to find:
1. Grand Total row of Annexure-1 (disaggregated revenue: Fee, Addl Charges, Section 20 penalty)
2. Annexure-2 (ministry-wise compliance)
"""
import pdfplumber

PDF = "data/raw/AR2019-20E.pdf"

with pdfplumber.open(PDF) as pdf:
    total_pages = len(pdf.pages)
    print(f"Total pages: {total_pages}")

    # Scan from page 180 onwards (Annexure-1 ends somewhere here)
    # Also scan last ~20 pages for Annexure-2
    pages_to_scan = list(range(180, total_pages))

    for p_idx in pages_to_scan:
        page = pdf.pages[p_idx]
        text = page.extract_text() or ""
        # Look for Grand Total, Annexure-2, or revenue-related keywords
        lower = text.lower()
        keywords = [
            "grand total", "total amount", "fee collected", "additional charges",
            "section 20", "penalty collected", "annexure-2", "annexure 2",
            "quarterly return", "status report", "submission"
        ]
        matched = [kw for kw in keywords if kw in lower]
        if matched:
            print(f"\n=== PAGE {p_idx+1} (keywords: {matched}) ===")
            print(text[:600])
            print("---")
        elif p_idx >= total_pages - 15:
            # Always print last 15 pages regardless
            print(f"\n=== PAGE {p_idx+1} [last pages] ===")
            print(text[:300])
            print("---")
