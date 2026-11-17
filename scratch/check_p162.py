import pdfplumber

with pdfplumber.open('data/raw/AR2018-19E.pdf') as pdf:
    page = pdf.pages[161]
    chars = page.chars
    c_sel = [c for c in chars if c['x0'] > 380 and 450 <= c['top'] <= 485]
    for c in sorted(c_sel, key=lambda c: (round(c['top'], 1), c['x0'])):
        print(f"y={c['top']:.1f}, x={c['x0']:.1f}: char={c['text']!r}")
