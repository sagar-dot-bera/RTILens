"""
Get full text from page 182 (Grand Total of Annexure-1) and pages 183-184 (Annexure-2)
to extract disaggregated revenue breakdown and ministry compliance data.
"""
import pdfplumber

PDF = "data/raw/AR2019-20E.pdf"

with pdfplumber.open(PDF) as pdf:
    # Page 182 = Grand Total row (index 181)
    print("=== PAGE 182 (Grand Total of Annexure-1) ===")
    page = pdf.pages[181]
    text = page.extract_text() or ""
    print(text)
    print("\n--- TABLES ON PAGE 182 ---")
    tables = page.extract_tables()
    for i, t in enumerate(tables):
        print(f"Table {i}:")
        for row in t:
            print(row)

    # Page 183 = Annexure-2 start (index 182)
    print("\n\n=== PAGE 183 (Annexure-2 start) ===")
    page2 = pdf.pages[182]
    text2 = page2.extract_text() or ""
    print(text2)

    # Page 184 = Annexure-2 continued (index 183)
    print("\n\n=== PAGE 184 (Annexure-2 cont.) ===")
    page3 = pdf.pages[183]
    text3 = page3.extract_text() or ""
    print(text3)
