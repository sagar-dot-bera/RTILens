"""
Extract cleaned datasets for AR 2019-20 (CIC Annual Report)
RTI Lens Project | Anistina

Outputs (all to data/cleaned/2019-20/):
  national_statistics.csv
  ministry_statistics.csv
  rejection_grounds.csv
  appeals_statistics.csv
  accountability_statistics.csv
  institutional_compliance.csv
  data_discrepancies.csv
"""

import csv
import os
from pathlib import Path

PROJECT_ROOT = Path("C:/Users/hp/OneDrive/Documents/Desktop/new/RTILens")
CLEANED_DIR = PROJECT_ROOT / "data" / "cleaned" / "2019-20"
CLEANED_DIR.mkdir(parents=True, exist_ok=True)

SOURCE_FILE = "AR2019-20E.pdf"
YEAR = "2019-20"


def write_csv(filename, fieldnames, rows):
    path = CLEANED_DIR / filename
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"  Written: {filename} ({len(rows)} rows)")


# ─────────────────────────────────────────────────────────
# 1. national_statistics.csv
# ─────────────────────────────────────────────────────────
def generate_national_statistics():
    """
    Table 2.4 (p.19): 15-year time series 2005-06 to 2019-20
    Table 2.9 (pp.29-30): 2019-20 supplementary details
    Section 3.2.2 (p.32): CIC 2nd appeals
    Annexure-1 Grand Total (p.182): Disaggregated revenue
    """
    fieldnames = [
        "financial_year", "pa_registered", "opening_balance",
        "requests_received", "total_requests", "requests_transferred",
        "requests_rejected", "rejection_pct_reported",
        "first_appeals_received", "first_appeals_disposed",
        "second_appeals_registered", "second_appeals_disposed",
        "second_appeals_pending", "disciplinary_actions",
        "fee_collected_rs", "addl_charges_collected_rs",
        "section20_penalty_collected_rs", "total_amount_collected_rs",
        "capios", "cpios", "faas", "total_officers",
        "source_file", "pdf_page", "table_number", "source_table", "notes"
    ]

    # Time series from Table 2.4 (p.19)
    # Columns: year, pa_reg, opening_bal, received, total, rejected, rejection_pct
    # Note: rejection_pct = rejected/received*100 (not total)
    ts_data = [
        ("2005-06",  938,       0,      24436,   24436,  3387,  13.9),
        ("2006-07",  1412,  12026,     171398,  183424, 15388,   9.0),
        ("2007-08",  1597,  23926,     263261,  287187, 18966,   7.2),
        ("2008-09",  1770,  32792,     329728,  362520, 23954,   7.26),
        ("2009-10",  1847,  97474,     529274,  626748, 34057,   6.43),
        ("2010-11",  2149, 137771,     417955,  555726, 21413,   5.1),
        ("2011-12",  2314,  76016,     629960,  705976, 52313,   8.3),
        ("2012-13",  2333,  75331,     811350,  886681, 62231,   7.7),
        ("2013-14",  2276, 128447,     834183,  962630, 60127,   7.21),
        ("2014-15",  2030,  89785,     755247,  845032, 63351,   8.39),
        ("2015-16",  2024, 188538,     976679, 1165217, 64666,   6.62),
        ("2016-17",  2092, 212430,     915749, 1128179, 60428,   6.59),
        ("2017-18",  2079, 215466,    1233207, 1448673, 63206,   5.13),
        ("2018-19",  2145, 259919,    1370129, 1630048, 64344,   4.7),
        ("2019-20",  2193, 310110,    1374315, 1684425, 58634,   4.27),
    ]

    rows = []
    for i, (yr, pa, ob, recv, tot, rej, rej_pct) in enumerate(ts_data):
        is_2019_20 = (yr == "2019-20")
        notes_parts = []
        if yr == "2017-18":
            notes_parts.append("Rejection% reported as 5.13%; footnote: 4% when opening balance included in denominator")
        if is_2019_20:
            notes_parts.append(
                "2019-20 details from Table 2.9 (pp.29-30), Sec 3.2.2 (p.32), Sec 3.3.1 (p.33), "
                "Annexure-1 Grand Total (p.182). Fee=5718102.20, Addl.Charges=3395856, Penalty=194576."
            )

        row = {
            "financial_year": yr,
            "pa_registered": pa,
            "opening_balance": ob,
            "requests_received": recv,
            "total_requests": tot,
            "requests_transferred": 182988 if is_2019_20 else "NA",
            "requests_rejected": rej,
            "rejection_pct_reported": rej_pct,
            "first_appeals_received": 152354 if is_2019_20 else "NA",
            "first_appeals_disposed": 96812 if is_2019_20 else "NA",
            "second_appeals_registered": 22243 if is_2019_20 else "NA",
            "second_appeals_disposed": 16720 if is_2019_20 else "NA",
            "second_appeals_pending": 35178 if is_2019_20 else "NA",
            "disciplinary_actions": 23 if is_2019_20 else "NA",
            "fee_collected_rs": 5718102.20 if is_2019_20 else "NA",
            "addl_charges_collected_rs": 3395856 if is_2019_20 else "NA",
            "section20_penalty_collected_rs": 194576 if is_2019_20 else "NA",
            "total_amount_collected_rs": 9308534 if is_2019_20 else "NA",
            "capios": 60432 if is_2019_20 else "NA",
            "cpios": 21756 if is_2019_20 else "NA",
            "faas": 8923 if is_2019_20 else "NA",
            "total_officers": 91111 if is_2019_20 else "NA",
            "source_file": SOURCE_FILE,
            "pdf_page": "19;29-30;32;33;182" if is_2019_20 else "19",
            "table_number": "Table_2.4;Table_2.9;Section_3.2.2;Section_3.3.1;Annexure-1_GrandTotal" if is_2019_20 else "Table_2.4",
            "source_table": "Table_2.4" if not is_2019_20 else "Table_2.4;Table_2.9;Section_3.2.2;Section_3.3.1;Annexure-1_GrandTotal",
            "notes": "; ".join(notes_parts) if notes_parts else "",
        }
        rows.append(row)

    write_csv("national_statistics.csv", fieldnames, rows)


# ─────────────────────────────────────────────────────────
# 2. ministry_statistics.csv
# ─────────────────────────────────────────────────────────
def generate_ministry_statistics():
    """
    Table 2.5 (p.22): 8 category-type rows
    Table 2.6 (p.23): Top 20 ministries by volume
    Table 2.8 (p.26): Top 20 ministries by appeals (merged with Table 2.6 for overlap)
    """
    fieldnames = [
        "financial_year", "entity_name", "entity_type",
        "rank_by_volume", "rank_by_rejection_pct",
        "requests_received", "requests_rejected", "rejection_pct_reported",
        "first_appeals_received", "second_appeals_received",
        "source_file", "pdf_page", "table_number", "source_table", "notes"
    ]

    rows = []

    # --- Category rows from Table 2.5 (p.22) ---
    categories = [
        ("Independent Ministry/Department",        293933, 4908, 1.67),
        ("Department Under Ministry",              242782, 4429, 1.82),
        ("Attached Office",                        125926, 1156, 0.92),
        ("Subordinate Office",                     361362,29653, 8.21),
        ("Corporation",                             32363, 1072, 3.31),
        ("Govt. Autonomous Body",                  215030,13387, 6.23),
        ("Govt. Company Under Companies Act",       20311, 1504, 7.40),
        ("Others",                                  82608, 2525, 3.06),
    ]
    # Category total (computed): 1,374,315 received, 58,634 rejected
    # Note: total row was absent from p.22; taken from Table 2.4/2.9

    for name, recv, rej, rej_pct in categories:
        rows.append({
            "financial_year": YEAR,
            "entity_name": name,
            "entity_type": "Category",
            "rank_by_volume": "NA",
            "rank_by_rejection_pct": "NA",
            "requests_received": recv,
            "requests_rejected": rej,
            "rejection_pct_reported": rej_pct,
            "first_appeals_received": "NA",
            "second_appeals_received": "NA",
            "source_file": SOURCE_FILE,
            "pdf_page": "22",
            "table_number": "Table_2.5",
            "source_table": "Table_2.5",
            "notes": "Total row absent from p.22; category total (1374315 recv, 58634 rej) sourced from Table 2.4/Table 2.9",
        })

    # --- Top 20 Ministries by Volume (Table 2.6 p.23) + Appeals (Table 2.8 p.26) ---
    # Combined data for 20 ministries
    top20 = [
        (1,  "Ministry of Finance",                                  192204, 23995, 12.48, 23574, 5422),
        (2,  "Ministry of Railways",                                 141499,  1663,  1.18, 16443, 1780),
        (3,  "Ministry of Communications",                           122949,  2078,  1.69,  9815, 1427),
        (4,  "UT of Delhi",                                          108009,  1513,  1.40, 10910, 2491),
        (5,  "Ministry of Human Resource Development",                94306,   950,  1.01, 18002, 1852),
        (6,  "Ministry of Corporate Affairs",                         83602,   454,  0.54,  3539,  162),
        (7,  "Ministry of Labour and Employment",                     80978,  2284,  2.82,  6188,  584),
        (8,  "Ministry of Defence",                                   70934,  3901,  5.50, 14369, 1286),
        (9,  "Ministry of Personnel, Public Grievances and Pensions", 65234,  1892,  2.90,  4973,  570),
        (10, "Ministry of Home Affairs",                              44453,  9095, 20.46,  7332,  985),
        (11, "Ministry of Road Transport and Highways",               36839,   137,  0.37,  1331,  188),
        (12, "Ministry of Health and Family Welfare",                 33738,   409,  1.21,  4551,  418),
        (13, "Ministry of Petroleum and Natural Gas",                 20903,  1092,  5.22,  2420,  438),
        (14, "Ministry of Housing and Urban Affairs",                 20716,   264,  1.27,  4096,  501),
        (15, "UT of Chandigarh",                                      17289,   283,  1.64,   902,  138),
        (16, "Ministry of Coal",                                      12650,   639,  5.05,  1932,  325),
        (17, "Prime Minister's Office",                               12238,   735,  6.01,  1576,  173),
        (18, "Ministry of Consumer Affairs, Food and Public Distribution", 11075, 92, 0.83, 1542,  153),
        (19, "Ministry of Agriculture & Farmers Welfare",             10288,   361,  3.51,  1054,  244),
        (20, "Ministry of Civil Aviation",                            10215,   175,  1.71,   983,  139),
    ]

    for rank, name, recv, rej, rej_pct, fa_recv, sa_recv in top20:
        rows.append({
            "financial_year": YEAR,
            "entity_name": name,
            "entity_type": "Ministry",
            "rank_by_volume": rank,
            "rank_by_rejection_pct": "NA",
            "requests_received": recv,
            "requests_rejected": rej,
            "rejection_pct_reported": rej_pct,
            "first_appeals_received": fa_recv,
            "second_appeals_received": sa_recv,
            "source_file": SOURCE_FILE,
            "pdf_page": "23;26",
            "table_number": "Table_2.6;Table_2.8",
            "source_table": "Table_2.6;Table_2.8",
            "notes": "Top 20 by RTI request volume; first_appeals and second_appeals from Table 2.8 (p.26)",
        })

    write_csv("ministry_statistics.csv", fieldnames, rows)


# ─────────────────────────────────────────────────────────
# 3. rejection_grounds.csv
# ─────────────────────────────────────────────────────────
def generate_rejection_grounds():
    """
    Table 2.7 (p.24): Section-level aggregates
    Table 2.9 rows 18+ (p.30): Section 8(1) sub-clause breakdown
    """
    fieldnames = [
        "financial_year", "provision", "provision_detail",
        "invocations_count", "invocations_pct_of_total",
        "reporting_period",
        "source_file", "pdf_page", "table_number", "source_table", "notes"
    ]

    # Section 8(1) sub-clauses (from Table 2.9 p.30)
    sub_clauses = [
        ("8(1)(a)", "Sovereignty, integrity, security, strategic, scientific, economic interests of the State; relation with foreign states; leading to incitement of an offence", 557,  None),
        ("8(1)(b)", "Expression prohibited by court or would constitute contempt of court",                                                                                      193,  None),
        ("8(1)(c)", "Breach of privilege of Parliament or State Legislature",                                                                                                      65,  None),
        ("8(1)(d)", "Commercial confidence, trade secrets, intellectual property rights",                                                                                        5190, None),
        ("8(1)(e)", "Information available to person in fiduciary relationship",                                                                                                 4828, None),
        ("8(1)(f)", "Received in confidence from foreign government",                                                                                                             418, None),
        ("8(1)(g)", "Endangerment to life or physical safety of person; identify source of information",                                                                          943, None),
        ("8(1)(h)", "Impede the process of investigation, apprehension or prosecution of offenders",                                                                            2734, None),
        ("8(1)(i)", "Cabinet papers including deliberations of Council of Ministers",                                                                                              695, None),
        ("8(1)(j)", "Personal information unrelated to public activity or interest / invasion of privacy",                                                                      12962, None),
    ]

    # Aggregate provisions (from Table 2.7 p.24)
    # Grand total invocations = 62123
    grand_total = 62123
    aggregates = [
        ("8(1)",  "Any sub-clause of Section 8(1) — exemption from disclosure",                 28585, round(28585/grand_total*100, 2)),
        ("9",     "Information which would involve infringement of copyright of any person",       258, round(258/grand_total*100, 2)),
        ("11",    "Third-party information treated as confidential",                               717, round(717/grand_total*100, 2)),
        ("24",    "Security and intelligence organisations specified in Second Schedule",          8504, round(8504/grand_total*100, 2)),
        ("Others","Other sections not explicitly categorised above",                             24059, round(24059/grand_total*100, 2)),
    ]

    rows = []

    # Sub-clauses
    section_8_1_total = 28585
    for provision, detail, count, _ in sub_clauses:
        pct = round(count / grand_total * 100, 2)
        rows.append({
            "financial_year": YEAR,
            "provision": provision,
            "provision_detail": detail,
            "invocations_count": count,
            "invocations_pct_of_total": pct,
            "reporting_period": YEAR,
            "source_file": SOURCE_FILE,
            "pdf_page": "30",
            "table_number": "Table_2.9",
            "source_table": "Table_2.9",
            "notes": f"Sub-clause of Section 8(1); sum of all sub-clauses={section_8_1_total}; grand total invocations={grand_total}; invocations can exceed rejections (58634) as multiple sections may be cited per rejection",
        })

    # Aggregates
    for provision, detail, count, pct in aggregates:
        rows.append({
            "financial_year": YEAR,
            "provision": provision,
            "provision_detail": detail,
            "invocations_count": count,
            "invocations_pct_of_total": pct,
            "reporting_period": YEAR,
            "source_file": SOURCE_FILE,
            "pdf_page": "24",
            "table_number": "Table_2.7",
            "source_table": "Table_2.7",
            "notes": f"Aggregate section-level count; total invocations={grand_total}; exceeds rejections (58634) as multiple sections may be cited per rejection",
        })

    write_csv("rejection_grounds.csv", fieldnames, rows)


# ─────────────────────────────────────────────────────────
# 4. appeals_statistics.csv
# ─────────────────────────────────────────────────────────
def generate_appeals_statistics():
    """
    National first appeals: Table 2.9 (pp.29-30)
    CIC second appeals: Section 3.2.2 (p.32)
    Ministry-level second appeals: Table 2.8 (p.26)
    """
    fieldnames = [
        "financial_year", "level", "entity_name", "entity_type",
        "received", "disposed", "pending",
        "source_file", "pdf_page", "table_number", "source_table", "notes"
    ]

    rows = []

    # National first appeals (Table 2.9)
    rows.append({
        "financial_year": YEAR,
        "level": "First Appeal",
        "entity_name": "All Public Authorities (National)",
        "entity_type": "National",
        "received": 152354,
        "disposed": 96812,
        "pending": "NA",
        "source_file": SOURCE_FILE,
        "pdf_page": "29",
        "table_number": "Table_2.9",
        "source_table": "Table_2.9",
        "notes": "National aggregate; pending balance not separately reported in this table",
    })

    # CIC second appeals (Section 3.2.2 p.32)
    rows.append({
        "financial_year": YEAR,
        "level": "Second Appeal / Complaint",
        "entity_name": "Central Information Commission (CIC)",
        "entity_type": "CIC",
        "received": 22243,
        "disposed": 16720,
        "pending": 35178,
        "source_file": SOURCE_FILE,
        "pdf_page": "32",
        "table_number": "Section_3.2.2",
        "source_table": "Section_3.2.2",
        "notes": "pending = cases pending as on 1st April of reporting year (opening balance); CIC 2nd appeals & complaints combined",
    })

    # Ministry-level second appeals from Table 2.8 (p.26)
    # 2nd_appeals = second_appeals_received (Table 2.8 col 4)
    top20_sa = [
        (1,  "Ministry of Finance",                                   5422),
        (2,  "Ministry of Railways",                                   1780),
        (3,  "Ministry of Communications",                             1427),
        (4,  "UT of Delhi",                                            2491),
        (5,  "Ministry of Human Resource Development",                 1852),
        (6,  "Ministry of Corporate Affairs",                           162),
        (7,  "Ministry of Labour and Employment",                       584),
        (8,  "Ministry of Defence",                                    1286),
        (9,  "Ministry of Personnel, Public Grievances and Pensions",   570),
        (10, "Ministry of Home Affairs",                                985),
        (11, "Ministry of Road Transport and Highways",                 188),
        (12, "Ministry of Health and Family Welfare",                   418),
        (13, "Ministry of Petroleum and Natural Gas",                   438),
        (14, "Ministry of Housing and Urban Affairs",                   501),
        (15, "UT of Chandigarh",                                        138),
        (16, "Ministry of Coal",                                        325),
        (17, "Prime Minister's Office",                                 173),
        (18, "Ministry of Consumer Affairs, Food and Public Distribution", 153),
        (19, "Ministry of Agriculture & Farmers Welfare",               244),
        (20, "Ministry of Civil Aviation",                              139),
    ]

    for rank, name, sa_recv in top20_sa:
        rows.append({
            "financial_year": YEAR,
            "level": "Second Appeal / Complaint",
            "entity_name": name,
            "entity_type": "Ministry",
            "received": sa_recv,
            "disposed": "NA",
            "pending": "NA",
            "source_file": SOURCE_FILE,
            "pdf_page": "26",
            "table_number": "Table_2.8",
            "source_table": "Table_2.8",
            "notes": f"Top 20 ministry by RTI volume (rank {rank}); second appeals include complaints; disposed/pending not reported at ministry level",
        })

    write_csv("appeals_statistics.csv", fieldnames, rows)


# ─────────────────────────────────────────────────────────
# 5. accountability_statistics.csv
# ─────────────────────────────────────────────────────────
def generate_accountability_statistics():
    """
    Disciplinary actions: Table 2.9 (p.29)
    CIC penalties: Section 3.3.1 (p.33)
    Revenue: Annexure-1 Grand Total (p.182)
    """
    fieldnames = [
        "financial_year", "metric", "value", "unit",
        "source_file", "pdf_page", "table_number", "source_table", "notes"
    ]

    rows = [
        {
            "financial_year": YEAR,
            "metric": "Disciplinary Actions Taken Against Officers",
            "value": 23,
            "unit": "Cases",
            "source_file": SOURCE_FILE,
            "pdf_page": "29",
            "table_number": "Table_2.9",
            "source_table": "Table_2.9",
            "notes": "Number of cases where disciplinary action taken against any officer in respect of administration of RTI Act",
        },
        {
            "financial_year": YEAR,
            "metric": "CIC Section 20(1) Penalties Imposed",
            "value": 1062000,
            "unit": "INR",
            "source_file": SOURCE_FILE,
            "pdf_page": "33",
            "table_number": "Section_3.3.1",
            "source_table": "Section_3.3.1",
            "notes": "Penalties imposed by CIC under Section 20(1); reported as Rs.10,62,000",
        },
        {
            "financial_year": YEAR,
            "metric": "CIC Section 20(1) Penalties Realized",
            "value": 640500,
            "unit": "INR",
            "source_file": SOURCE_FILE,
            "pdf_page": "33",
            "table_number": "Section_3.3.1",
            "source_table": "Section_3.3.1",
            "notes": "Amount received against CIC penalties; reported as Rs.6,40,500; may include carry-over collections from prior-year impositions",
        },
        {
            "financial_year": YEAR,
            "metric": "Fee (Application) Collected by PAs",
            "value": 5718102.20,
            "unit": "INR",
            "source_file": SOURCE_FILE,
            "pdf_page": "182",
            "table_number": "Annexure-1_GrandTotal",
            "source_table": "Annexure-1_GrandTotal",
            "notes": "RTI application fee collected by all PAs; Annexure-1 Grand Total row; value has decimal (5718102.20)",
        },
        {
            "financial_year": YEAR,
            "metric": "Additional Charges Collected by PAs",
            "value": 3395856,
            "unit": "INR",
            "source_file": SOURCE_FILE,
            "pdf_page": "182",
            "table_number": "Annexure-1_GrandTotal",
            "source_table": "Annexure-1_GrandTotal",
            "notes": "Additional charges for providing information (photocopying etc.) collected by all PAs",
        },
        {
            "financial_year": YEAR,
            "metric": "Section 20 Penalty Collected by PAs",
            "value": 194576,
            "unit": "INR",
            "source_file": SOURCE_FILE,
            "pdf_page": "182",
            "table_number": "Annexure-1_GrandTotal",
            "source_table": "Annexure-1_GrandTotal",
            "notes": "Section 20 penalty collected by Public Authorities (distinct from CIC-imposed penalties); reported in Annexure-1 Grand Total",
        },
        {
            "financial_year": YEAR,
            "metric": "Total Amount Collected by PAs",
            "value": 9308534,
            "unit": "INR",
            "source_file": SOURCE_FILE,
            "pdf_page": "28;182",
            "table_number": "Figure_2.6;Annexure-1_GrandTotal",
            "source_table": "Figure_2.6;Annexure-1_GrandTotal",
            "notes": "Fee + Addl.Charges + Penalty = 5718102.20 + 3395856 + 194576 = 9308534; verified against Figure 2.6 (p.28)",
        },
        {
            "financial_year": YEAR,
            "metric": "RTI Requests Rejected",
            "value": 58634,
            "unit": "Requests",
            "source_file": SOURCE_FILE,
            "pdf_page": "29",
            "table_number": "Table_2.9",
            "source_table": "Table_2.9",
            "notes": "Overall rejection count for 2019-20; rejection rate = 4.27% over requests received (not total)",
        },
    ]

    write_csv("accountability_statistics.csv", fieldnames, rows)


# ─────────────────────────────────────────────────────────
# 6. institutional_compliance.csv
# ─────────────────────────────────────────────────────────
def generate_institutional_compliance():
    """
    Table 2.1 (p.12): 15-year PA compliance time series
    Table 2.3 (p.17): Category-wise compliance for 2019-20
    Figure 2.5 (p.27): CAPIOs/CPIOs/FAAs trend 2015-16 to 2019-20
    Annexure-2 (pp.183-184): Ministry-wise annual return compliance (68 entries)
    """
    fieldnames = [
        "financial_year", "entity_name", "entity_type",
        "pa_registered", "pa_compliant", "pa_non_compliant",
        "compliance_pct_reported", "capios", "cpios", "faas",
        "source_file", "pdf_page", "table_number", "source_table", "notes"
    ]

    rows = []

    # --- Table 2.1 (p.12): National aggregate time series ---
    # Note: 2019-20 uses quarterly returns; prior years used annual returns
    # Figure 2.5 (p.27): officer trend for 2015-16 to 2019-20
    ts_compliance = [
        # (year, pa_reg, submitted, not_submitted, compliance_pct, capios, cpios, faas)
        ("2005-06", 938,  837,  101,  89.23, "NA", "NA", "NA"),
        ("2006-07", 1412, 1168, 244,  82.72, "NA", "NA", "NA"),
        ("2007-08", 1597, 1382, 215,  86.54, "NA", "NA", "NA"),
        ("2008-09", 1770, 1528, 242,  86.33, "NA", "NA", "NA"),
        ("2009-10", 1847, 1427, 420,  77.26, "NA", "NA", "NA"),
        ("2010-11", 2149, 1452, 697,  67.57, "NA", "NA", "NA"),
        ("2011-12", 2314, 1593, 721,  68.84, "NA", "NA", "NA"),
        ("2012-13", 2333, 1864, 469,  79.90, "NA", "NA", "NA"),
        ("2013-14", 2276, 1651, 625,  72.54, "NA", "NA", "NA"),
        ("2014-15", 2030, 1528, 502,  75.27, "NA", "NA", "NA"),
        ("2015-16", 2023, 1903, 120,  94.07, 66025, 22210, 8766),
        ("2016-17", 2092, 1964, 128,  93.88, 64711, 23561, 9497),
        ("2017-18", 2079, 2079,   0, 100.00, 55176, 23213, 9314),
        ("2018-19", 2145, 2145,   0, 100.00, 63869, 24048, 9309),
        ("2019-20", 2193, 2131,  62,  97.17, 60432, 21756, 8923),
    ]

    for yr, pa_reg, pa_comp, pa_non, comp_pct, capios, cpios, faas in ts_compliance:
        note = "National aggregate; compliance measured as PAs who submitted all 4 quarterly returns (2019-20) or annual returns (prior years)"
        if yr == "2019-20":
            note += "; officers from Table 2.9/Annexure-1 Grand Total (p.182)"
        rows.append({
            "financial_year": yr,
            "entity_name": "All Public Authorities (National)",
            "entity_type": "National",
            "pa_registered": pa_reg,
            "pa_compliant": pa_comp,
            "pa_non_compliant": pa_non,
            "compliance_pct_reported": comp_pct,
            "capios": capios,
            "cpios": cpios,
            "faas": faas,
            "source_file": SOURCE_FILE,
            "pdf_page": "12" if yr != "2019-20" else "12;27;182",
            "table_number": "Table_2.1" if yr != "2019-20" else "Table_2.1;Figure_2.5;Annexure-1_GrandTotal",
            "source_table": "Table_2.1" if yr != "2019-20" else "Table_2.1;Figure_2.5;Annexure-1_GrandTotal",
            "notes": note,
        })

    # --- Table 2.3 (p.17): Category-wise compliance for 2019-20 ---
    # (category, total_pas, pct_of_total, submitted_all_4, compliance_pct)
    categories_2019 = [
        ("Independent Ministry/Department",        110, 5.02, 104, 95),
        ("Department Under Ministry",              125, 5.70, 122, 98),
        ("Attached Office",                        177, 8.07, 171, 97),
        ("Subordinate Office",                     924,42.13, 894, 97),
        ("Corporation",                             50, 2.28,  49, 98),
        ("Govt. Autonomous Body",                  570,25.99, 561, 98),
        ("Govt. Company Under Companies Act",       76, 3.47,  74, 97),
        ("Others",                                 161, 7.34, 156, 97),
    ]

    for name, pa_tot, pct_total, pa_comp, comp_pct in categories_2019:
        rows.append({
            "financial_year": YEAR,
            "entity_name": name,
            "entity_type": "Category",
            "pa_registered": pa_tot,
            "pa_compliant": pa_comp,
            "pa_non_compliant": pa_tot - pa_comp,
            "compliance_pct_reported": comp_pct,
            "capios": "NA",
            "cpios": "NA",
            "faas": "NA",
            "source_file": SOURCE_FILE,
            "pdf_page": "17",
            "table_number": "Table_2.3",
            "source_table": "Table_2.3",
            "notes": f"Category comprises {pct_total}% of all PAs; compliance = PAs who submitted all 4 quarterly returns in 2019-20",
        })

    # --- Annexure-2 (pp.183-184): Ministry-wise compliance ---
    # (ministry_name, total_pas, pa_compliant, compliance_pct)
    annexure2 = [
        ("Election Commission of India",                                    1,   1, 100.00),
        ("Cabinet Secretariat",                                             1,   1, 100.00),
        ("Ministry Of Agriculture & Farmers Welfare",                     200, 200, 100.00),
        ("Ministry of Food Processing Industries",                          1,   1, 100.00),
        ("Ministry of Chemicals & Fertilizers",                            32,  31,  96.88),
        ("Ministry of Civil Aviation",                                     11,  11, 100.00),
        ("Ministry of Coal",                                               13,  13, 100.00),
        ("Ministry of Minority Affairs",                                    7,   7, 100.00),
        ("Ministry of Mines",                                               9,   9, 100.00),
        ("Ministry of Commerce & Industry",                                44,  43,  97.73),
        ("Department of Atomic Energy",                                    34,  34, 100.00),
        ("Ministry of Communications",                                      9,   9, 100.00),
        ("Ministry Of Consumer Affairs, Food and Public Distribution",     28,  26,  92.86),
        ("Ministry of Defence",                                            48,  47,  97.92),
        ("Ministry of Development of North Eastern Region",                 5,   5, 100.00),
        ("Ministry Of Environment, Forest and Climate Change",             33,  32,  96.97),
        ("Ministry of External Affairs",                                  179, 167,  93.30),
        ("Ministry of Finance",                                           192, 188,  97.92),
        ("Ministry of Health & Family Welfare",                           102, 100,  98.04),
        ("Ministry of Panchayati Raj",                                      1,   1, 100.00),
        ("Ministry of Heavy Industry & Public Enterprises",                28,  28, 100.00),
        ("Ministry of Home Affairs",                                       31,  29,  93.55),
        ("Ministry of Human Resource Development",                        202, 199,  98.51),
        ("Ministry of Women & Child Development",                           7,   6,  85.71),
        ("Ministry of Information & Broadcasting",                         25,  25, 100.00),
        ("Ministry of Labour & Employment",                                33,  32,  96.97),
        ("Ministry of Law & Justice",                                      41,  41, 100.00),
        ("Ministry of Corporate Affairs",                                  63,  59,  93.65),
        ("Ministry of New & Renewable Energy",                              6,   6, 100.00),
        ("Ministry of Earth Sciences",                                     10,  10, 100.00),
        ("Prime Minister's Office",                                         1,   1, 100.00),
        ("Ministry of Parliamentary Affairs",                               1,   1, 100.00),
        ("Ministry of Personnel, Public Grievances & Pensions",            12,  11,  91.67),
        ("Ministry of Petroleum & Natural Gas",                            24,  22,  91.67),
        ("NITI Aayog",                                                      1,   1, 100.00),
        ("Ministry of Power",                                              18,  18, 100.00),
        ("Ministry of Railways",                                           13,  13, 100.00),
        ("Ministry of Shipping",                                           19,  18,  94.74),
        ("Ministry of Rural Development",                                   4,   4, 100.00),
        ("Ministry of Science & Technology",                               92,  92, 100.00),
        ("Ministry of Social Justice & Empowerment",                       24,  24, 100.00),
        ("Department of Space",                                             1,   1, 100.00),
        ("Ministry of Statistics & Programme Implementation",               1,   1, 100.00),
        ("Ministry of Steel",                                              13,  12,  92.31),
        ("Ministry of Textiles",                                           19,  18,  94.74),
        ("Ministry of Tourism",                                            25,  25, 100.00),
        ("Ministry of Culture",                                            36,  36, 100.00),
        ("Ministry of Tribal Affairs",                                      4,   4, 100.00),
        ("Ministry of Road Transport & Highways",                           5,   5, 100.00),
        ("Ministry of Youth Affairs & Sports",                              6,   6, 100.00),
        ("President's Secretariat",                                         1,   1, 100.00),
        ("Comptroller and Auditor General of India",                        1,   1, 100.00),
        ("UT of Andaman & Nicobar",                                         2,   2, 100.00),
        ("UT of Chandigarh",                                               67,  66,  98.51),
        ("UT of Dadar & Nagar Haveli",                                      1,   0,   0.00),
        ("UT of Daman & Diu",                                               1,   1, 100.00),
        ("UT of Lakshadweep",                                               1,   1, 100.00),
        ("UT of Puducherry",                                               47,  45,  95.74),
        ("Vice-President's Secretariat",                                    1,   1, 100.00),
        ("Supreme Court of India",                                          1,   1, 100.00),
        ("UT of Delhi",                                                   203, 193,  95.07),
        ("High Court Of Delhi",                                             2,   2, 100.00),
        ("Ministry of Micro, Small and Medium Enterprises",                60,  60, 100.00),
        ("Ministry of Skill Development & Entrepreneurship",                6,   6, 100.00),
        ("Ministry of Housing & Urban Affairs",                            28,  23,  82.14),
        ("Ministry of Electronics & Information Technology",               13,  12,  92.31),
        ("Ministry of Ayush",                                              21,  21, 100.00),
        ("Ministry of Jal Shakti",                                         22,  21,  95.45),
        # Grand Total
        ("Grand Total",                                                  2193, 2131,  97.17),
    ]

    for name, pa_tot, pa_comp, comp_pct in annexure2:
        entity_type = "Grand Total" if name == "Grand Total" else "Ministry"
        rows.append({
            "financial_year": YEAR,
            "entity_name": name,
            "entity_type": entity_type,
            "pa_registered": pa_tot,
            "pa_compliant": pa_comp,
            "pa_non_compliant": pa_tot - pa_comp,
            "compliance_pct_reported": comp_pct,
            "capios": "NA",
            "cpios": "NA",
            "faas": "NA",
            "source_file": SOURCE_FILE,
            "pdf_page": "183-184",
            "table_number": "Annexure-2",
            "source_table": "Annexure-2",
            "notes": "Ministry-wise annual return compliance per Annexure-2; note header says 'Annual Return' but report uses quarterly returns; compliance% matches Table 2.1 national aggregate (97.17%)",
        })

    write_csv("institutional_compliance.csv", fieldnames, rows)


# ─────────────────────────────────────────────────────────
# 7. data_discrepancies.csv
# ─────────────────────────────────────────────────────────
def generate_data_discrepancies():
    fieldnames = [
        "discrepancy_id", "financial_year", "dataset_affected",
        "description", "source_location", "resolution", "impact"
    ]

    rows = [
        {
            "discrepancy_id": "D1",
            "financial_year": YEAR,
            "dataset_affected": "ministry_statistics.csv",
            "description": "Table 2.5 (p.22) category-wise data lacks a printed total row; individual category totals sum to 1374315 received and 58634 rejected per external verification",
            "source_location": "AR2019-20E.pdf p.22 Table 2.5",
            "resolution": "Total row sourced from Table 2.4 (p.19) and Table 2.9 (pp.29-30); documented in notes column of affected rows",
            "impact": "Low — values are consistent across sources",
        },
        {
            "discrepancy_id": "D2",
            "financial_year": YEAR,
            "dataset_affected": "national_statistics.csv",
            "description": "2017-18 rejection% has conflicting values: reported as 5.13% in Table 2.4, but footnote states 4% when opening balance is included in denominator",
            "source_location": "AR2019-20E.pdf p.19 Table 2.4 (footnote)",
            "resolution": "Retained 5.13% as reported; footnote explanation included in notes column",
            "impact": "Low — footnote explains the discrepancy; not an error",
        },
        {
            "discrepancy_id": "D3",
            "financial_year": YEAR,
            "dataset_affected": "accountability_statistics.csv; national_statistics.csv",
            "description": "Fee collected reported as 5718102.20 (decimal) in Annexure-1 Grand Total; likely a data entry artefact",
            "source_location": "AR2019-20E.pdf p.182 Annexure-1 Grand Total",
            "resolution": "Stored as 5718102.20; total still reconciles to 9308534 (5718102.20 + 3395856 + 194576 = 9308534.20 ≈ 9308534 after rounding)",
            "impact": "Very low — rounding artefact; total is correct to nearest rupee",
        },
        {
            "discrepancy_id": "D4",
            "financial_year": YEAR,
            "dataset_affected": "rejection_grounds.csv",
            "description": "Total invocations of rejection provisions (62123) exceeds total rejections (58634) by 3489",
            "source_location": "AR2019-20E.pdf p.24 Table 2.7; p.29 Table 2.9",
            "resolution": "Expected — a single rejection can cite multiple sections; reported as invocations not unique rejections; documented in notes",
            "impact": "None — different metrics measuring different things",
        },
        {
            "discrepancy_id": "D5",
            "financial_year": YEAR,
            "dataset_affected": "institutional_compliance.csv",
            "description": "Annexure-2 header says 'Status Report on the Submission of RTI Annual Return' but 2019-20 uses quarterly returns; compliance basis is quarterly return submission",
            "source_location": "AR2019-20E.pdf p.183 Annexure-2",
            "resolution": "Noted in row-level notes; compliance% (97.17%) matches Table 2.1 national figure confirming the data is correct despite header terminology mismatch",
            "impact": "Very low — terminology inconsistency; data is correct",
        },
        {
            "discrepancy_id": "D6",
            "financial_year": YEAR,
            "dataset_affected": "institutional_compliance.csv",
            "description": "Table 2.2 (p.14) only shows lowest-compliance ministries — not a complete ministry list",
            "source_location": "AR2019-20E.pdf p.14 Table 2.2",
            "resolution": "Full ministry-wise compliance taken from Annexure-2 (pp.183-184) which has all 68 entries; Table 2.2 used as supplemental reference only",
            "impact": "None — Annexure-2 is the authoritative complete source",
        },
    ]

    write_csv("data_discrepancies.csv", fieldnames, rows)


# ─────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────
if __name__ == "__main__":
    print(f"Extracting cleaned datasets for {YEAR}...")
    print(f"Output directory: {CLEANED_DIR}")
    print()

    generate_national_statistics()
    generate_ministry_statistics()
    generate_rejection_grounds()
    generate_appeals_statistics()
    generate_accountability_statistics()
    generate_institutional_compliance()
    generate_data_discrepancies()

    print()
    print("Done! All 7 files written.")
    print()
    print("Summary:")
    for f in sorted(CLEANED_DIR.glob("*.csv")):
        with open(f, encoding="utf-8") as fh:
            n = sum(1 for _ in fh) - 1  # exclude header
        print(f"  {f.name}: {n} data rows")
