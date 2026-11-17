"""
extract_2018_19_cleaned_datasets.py
Generates the 6 cleaned datasets, data_discrepancies.csv, and data_quality_report.md
for CIC Annual Report 2018-19.
"""
import csv
from pathlib import Path

PROJECT_ROOT = Path("C:/Users/hp/OneDrive/Documents/Desktop/new/RTILens")
CLEANED_DIR = PROJECT_ROOT / "data/cleaned/2018-19"
CLEANED_DIR.mkdir(parents=True, exist_ok=True)
YEAR = "2018-19"

def write_csv(path, fieldnames, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)
    print(f"Created {path.name} with {len(rows)} rows")

def generate_national_statistics():
    FN = ["financial_year", "pa_registered", "opening_balance", "requests_received",
          "total_requests", "requests_transferred", "requests_rejected",
          "rejection_pct_reported", "first_appeals_received", "first_appeals_disposed",
          "second_appeals_registered", "second_appeals_disposed", "second_appeals_pending",
          "disciplinary_actions", "fee_collected_rs", "addl_charges_collected_rs",
          "section20_penalty_collected_rs", "total_amount_collected_rs",
          "capios", "cpios", "faas", "total_officers",
          "source_file", "pdf_page", "table_number", "source_table", "notes"]

    # 14-year time series from Table 2.4 (page 18)
    ts = [
        ("2005-06", 938, 0, 24436, 24436, 3387, 13.9),
        ("2006-07", 1412, 12026, 171398, 183424, 15388, 9.0),
        ("2007-08", 1597, 23926, 263261, 287187, 18966, 7.20),
        ("2008-09", 1770, 32792, 329728, 362520, 23954, 7.26),
        ("2009-10", 1847, 97474, 529274, 626748, 34057, 6.43),
        ("2010-11", 2149, 137771, 417955, 555726, 21413, 5.10),
        ("2011-12", 2314, 76016, 629960, 705976, 52313, 8.30),
        ("2012-13", 2333, 75331, 811350, 886681, 62231, 7.70),
        ("2013-14", 2276, 128447, 834183, 962630, 60127, 7.21),
        ("2014-15", 2030, 89785, 755247, 845032, 63351, 8.39),
        ("2015-16", 2023, 188538, 976679, 1165217, 64666, 6.62),
        ("2016-17", 2092, 212430, 915749, 1128179, 60428, 6.59),
        ("2017-18", 2079, 215466, 1233207, 1448673, 63206, 5.13),
        ("2018-19", 2145, 259919, 1370129, 1630048, 64344, 4.70),
    ]

    rows = []
    for (yr, pa, ob, recv, tot, rej, rpct) in ts:
        cur = (yr == "2018-19")
        rows.append({
            "financial_year": yr,
            "pa_registered": pa,
            "opening_balance": ob,
            "requests_received": recv,
            "total_requests": tot,
            "requests_transferred": 186084 if cur else "NA",
            "requests_rejected": rej,
            "rejection_pct_reported": rpct,
            "first_appeals_received": 151481 if cur else "NA",
            "first_appeals_disposed": 99618 if cur else "NA",
            "second_appeals_registered": 22736 if cur else "NA",
            "second_appeals_disposed": 17188 if cur else "NA",
            "second_appeals_pending": 29655 if cur else "NA",
            "disciplinary_actions": 9 if cur else "NA",
            "fee_collected_rs": 6142217 if cur else "NA",
            "addl_charges_collected_rs": 3746331 if cur else "NA",
            "section20_penalty_collected_rs": 472140 if cur else "NA",
            "total_amount_collected_rs": 10360688 if cur else "NA",
            "capios": 63869 if cur else "NA",
            "cpios": 24048 if cur else "NA",
            "faas": 9309 if cur else "NA",
            "total_officers": 97226 if cur else "NA",
            "source_file": "table_page_18_1.csv; table_page_28_1.csv; table_page_31_1.csv; table_page_162_1.csv" if cur else "table_page_18_1.csv",
            "pdf_page": "18; 28; 31; 162" if cur else "18",
            "table_number": "Table 2.4; Table 2.9; Sec 3.2.2; Annexure-1 Grand Total" if cur else "Table 2.4",
            "source_table": "Disposal of RTI Applications 2005-06 to 2018-19; Summary of Annual Returns 2018-19; Registration/Disposal; Annexure-1 Grand Total" if cur else "Disposal of RTI Applications 2005-06 to 2018-19",
            "notes": (
                "2018-19: requests/rejected/total from Table 2.4 p18; transfers/appeals/officers from Table 2.9 p28; "
                "second_appeals from Sec 3.2.2 p31; disaggregated fee/charges/penalty from Annexure-1 Grand Total p162. "
                "total_amount_collected_rs = fee + addl_charges + penalty = 6142217 + 3746331 + 472140 = 10360688 VERIFIED to exact rupee."
            ) if cur else "Columns available in multi-year Table 2.4; year-specific columns are NA for prior years."
        })
    write_csv(CLEANED_DIR / "national_statistics.csv", FN, rows)

def generate_ministry_statistics():
    FN = ["financial_year", "entity_name", "entity_type", "rank_by_volume", "rank_by_rejection_pct",
          "requests_received", "requests_rejected", "rejection_pct_reported",
          "first_appeals_received", "second_appeals_received",
          "source_file", "pdf_page", "table_number", "source_table", "notes"]
    rows = []

    # Table 2.5: 8 categories + Total (page 21)
    cats = [
        (1, "Independent Ministry/Department", 290654, 4613, 1.59),
        (2, "Department under Ministry", 271147, 5828, 2.15),
        (3, "Attached Office", 57881, 1396, 2.41),
        (4, "Subordinate Office", 389444, 33071, 8.49),
        (5, "Corporation", 38667, 978, 2.53),
        (6, "Govt. Autonomous Body", 211702, 13341, 6.30),
        (7, "Govt. Company under Companies Act", 26862, 1545, 5.75),
        (8, "Others", 83772, 3572, 4.26),
        (None, "Total (all categories)", 1370129, 64344, 4.70),
    ]
    for (n, name, recv, rej, rpct) in cats:
        rows.append({
            "financial_year": YEAR,
            "entity_name": name,
            "entity_type": "PA Category",
            "rank_by_volume": "NA",
            "rank_by_rejection_pct": "NA",
            "requests_received": recv,
            "requests_rejected": rej,
            "rejection_pct_reported": rpct,
            "first_appeals_received": "NA",
            "second_appeals_received": "NA",
            "source_file": "table_page_21_1.csv",
            "pdf_page": "21",
            "table_number": "Table 2.5",
            "source_table": "Distribution of applications received and rejected by Public Authorities during 2018-19",
            "notes": f"Category row {n}. Sum of categories equals national total (1370129 received, 64344 rejected)." if n else
                     "Total row: sum of all 8 categories. Verified against national totals in Table 2.4 (page 18). Consistent."
        })

    # Table 2.6: Top 20 Ministries by volume and rejections (pages 21-22)
    vol20 = [
        (1, "Ministry Of Finance", 211083, 27098, 12.84, "21", "table_page_21_1.csv"),
        (2, "Ministry Of Communications & Information Technology", 147359, 3448, 2.34, "21", "table_page_21_1.csv"),
        (3, "UT Of Delhi", 128629, 566, 0.44, "21", "table_page_21_1.csv"),
        (4, "Ministry Of Railways", 124506, 1438, 1.15, "21", "table_page_21_1.csv"),
        (5, "Ministry Of Human Resource Development", 98035, 1030, 1.05, "22", "table_page_22_1.csv"),
        (6, "Ministry Of Defence", 84796, 3868, 4.56, "22", "table_page_22_1.csv"),
        (7, "Ministry Of Labour & Employment", 83389, 3357, 4.03, "22", "table_page_22_1.csv"),
        (8, "Ministry Of Home Affairs", 57208, 9390, 16.41, "22", "table_page_22_1.csv"),
        (9, "Ministry Of Personnel, Public Grievances & Pensions", 54559, 2249, 4.12, "22", "table_page_22_1.csv"),
        (10, "Ministry Of Health & Family Welfare", 34915, 571, 1.64, "22", "table_page_22_1.csv"),
        (11, "Ministry Of Housing & Urban Affairs", 31992, 429, 1.34, "22", "table_page_22_1.csv"),
        (12, "Ministry Of Petroleum & Natural Gas", 23558, 1161, 4.93, "22", "table_page_22_1.csv"),
        (13, "UT Of Chandigarh", 15894, 323, 2.03, "22", "table_page_22_1.csv"),
        (14, "Ministry Of Agriculture", 14050, 328, 2.33, "22", "table_page_22_1.csv"),
        (15, "Ministry Of Road Transport & Highways", 13389, 70, 0.52, "22", "table_page_22_1.csv"),
        (16, "Ministry Of Coal", 13003, 580, 4.46, "22", "table_page_22_1.csv"),
        (17, "Ministry Of Consumer Affairs, Food, & Public Distribution", 12877, 195, 1.51, "22", "table_page_22_1.csv"),
        (18, "Ministry Of Civil Aviation", 12295, 204, 1.66, "22", "table_page_22_1.csv"),
        (19, "Prime Minister’s Office", 12143, 724, 5.96, "22", "table_page_22_1.csv"),
        (20, "Ministry Of Corporate Affairs", 10956, 448, 4.09, "22", "table_page_22_1.csv"),
    ]
    for (rank, name, recv, rej, rpct, page, sf) in vol20:
        rows.append({
            "financial_year": YEAR,
            "entity_name": name,
            "entity_type": "Ministry/Department/UT",
            "rank_by_volume": rank,
            "rank_by_rejection_pct": "NA",
            "requests_received": recv,
            "requests_rejected": rej,
            "rejection_pct_reported": rpct,
            "first_appeals_received": "NA",
            "second_appeals_received": "NA",
            "source_file": sf,
            "pdf_page": page,
            "table_number": "Table 2.6",
            "source_table": "Receipt of RTI applications and their rejections in top 20 Ministries/Departments",
            "notes": f"Rank {rank} by RTI volume. rejection_pct = (rejected/received)*100 as reported in Table 2.6."
        })

    # Table 2.8: Top 20 Ministries by Requests, First Appeals, Second Appeals (pages 24-25)
    app20 = [
        (1, "Ministry Of Finance", 211083, 25394, 12.03, 5141, "24", "table_page_24_1.csv"),
        (2, "Ministry Of Communications & Information Technology", 147359, 10159, 6.89, 1766, "24", "table_page_24_1.csv"),
        (3, "UT Of Delhi", 128629, 12086, 9.40, 2540, "24", "table_page_24_1.csv"),
        (4, "Ministry Of Railways", 124506, 14457, 11.61, 1954, "25", "table_page_25_1.csv"),
        (5, "Ministry Of Human Resource Development", 98035, 16581, 16.91, 1395, "25", "table_page_25_1.csv"),
        (6, "Ministry Of Defence", 84796, 15028, 17.72, 1345, "25", "table_page_25_1.csv"),
        (7, "Ministry Of Labour & Employment", 83389, 6720, 8.06, 522, "25", "table_page_25_1.csv"),
        (8, "Ministry Of Home Affairs", 57208, 7321, 12.80, 983, "25", "table_page_25_1.csv"),
        (9, "Ministry Of Personnel, Public Grievances & Pensions", 54559, 4994, 9.15, 641, "25", "table_page_25_1.csv"),
        (10, "Ministry Of Health & Family Welfare", 34915, 3714, 10.64, 424, "25", "table_page_25_1.csv"),
        (11, "Ministry Of Housing & Urban Affairs", 31992, 3558, 11.12, 536, "25", "table_page_25_1.csv"),
        (12, "Ministry Of Petroleum & Natural Gas", 23558, 2777, 11.79, 560, "25", "table_page_25_1.csv"),
        (13, "UT Of Chandigarh", 15894, 878, 5.52, 176, "25", "table_page_25_1.csv"),
        (14, "Ministry Of Agriculture", 14050, 1087, 7.74, 236, "25", "table_page_25_1.csv"),
        (15, "Ministry Of Road Transport & Highways", 13389, 1824, 13.62, 159, "25", "table_page_25_1.csv"),
        (16, "Ministry Of Coal", 13003, 1998, 15.37, 353, "25", "table_page_25_1.csv"),
        (17, "Ministry Of Consumer Affairs, Food, & Public Distribution", 12877, 1680, 13.05, 189, "25", "table_page_25_1.csv"),
        (18, "Ministry Of Civil Aviation", 12295, 1110, 9.03, 167, "25", "table_page_25_1.csv"),
        (19, "Prime Minister’s Office", 12143, 2000, 16.47, 259, "25", "table_page_25_1.csv"),
        (20, "Ministry Of Corporate Affairs", 10956, 908, 8.29, 127, "25", "table_page_25_1.csv"),
    ]
    for (rank, name, recv, fa, fa_conv_pct, sa, page, sf) in app20:
        rows.append({
            "financial_year": YEAR,
            "entity_name": name,
            "entity_type": "Ministry/Department/UT",
            "rank_by_volume": rank,
            "rank_by_rejection_pct": "NA",
            "requests_received": recv,
            "requests_rejected": "NA",
            "rejection_pct_reported": "NA",
            "first_appeals_received": fa,
            "second_appeals_received": sa,
            "source_file": sf,
            "pdf_page": page,
            "table_number": "Table 2.8",
            "source_table": "Top twenty Public Authorities receiving RTI Applications, First Appeals, Second Appeals",
            "notes": f"Rank {rank} by RTI requests. First appeal conversion rate reported as {fa_conv_pct}%. Second appeals received reported as {sa}."
        })
    write_csv(CLEANED_DIR / "ministry_statistics.csv", FN, rows)

def generate_rejection_grounds():
    FN = ["financial_year", "provision", "provision_detail", "invocations_count",
          "invocations_pct_of_total", "reporting_period", "source_file",
          "pdf_page", "table_number", "source_table", "notes"]
    rows = []
    TOTAL = 71321
    S8_TOTAL = 35733

    # Section 8(1) sub-clauses from Table 2.9 (page 29) & Annexure-1 (pages 45 & 162)
    sub = [
        ("Section 8(1)", "(a) - Sovereignty, integrity, security, strategic interests of State", 1162),
        ("Section 8(1)", "(b) - Expressly forbidden to be published by court or tribunal", 142),
        ("Section 8(1)", "(c) - Breach of privilege of Parliament or State Legislature", 65),
        ("Section 8(1)", "(d) - Commercial confidence, trade secrets or intellectual property", 6516),
        ("Section 8(1)", "(e) - Information available to a person in his fiduciary relationship", 6060),
        ("Section 8(1)", "(f) - Information received in confidence from foreign Government", 749),
        ("Section 8(1)", "(g) - Endangering life or physical safety of any person", 824),
        ("Section 8(1)", "(h) - Impeding process of investigation or apprehension of offenders", 2729),
        ("Section 8(1)", "(i) - Cabinet papers including deliberations of Council of Ministers", 1165),
        ("Section 8(1)", "(j) - Personal information without public interest", 16321),
    ]
    for (prov, det, cnt) in sub:
        pct = round(cnt / TOTAL * 100, 2)
        rows.append({
            "financial_year": YEAR,
            "provision": prov,
            "provision_detail": det,
            "invocations_count": cnt,
            "invocations_pct_of_total": pct,
            "reporting_period": "1 April 2018 to 31 March 2019",
            "source_file": "table_page_29_1.csv",
            "pdf_page": "29",
            "table_number": "Table 2.9 (rows 17-26)",
            "source_table": "Summary of Annual Returns 2018-19 - Sections Invoked",
            "notes": f"Sub-clause count from Table 2.9 (p29). Calculated pct = {cnt}/{TOTAL}*100 ({pct}%)."
        })

    # High-level aggregate sections from Table 2.7 (page 23)
    agg = [
        ("Section 8(1)", "AGGREGATE TOTAL (sub-clauses a through j)", S8_TOTAL, 50.10,
         "Reported in Table 2.7 (page 23). Verified: sum of sub-clauses (a)-(j) = 1162+142+65+6516+6060+749+824+2729+1165+16321 = 35733. Consistent."),
        ("Section 9", "Infringement of copyright exemption (complete section)", 807, 1.13,
         "Reported in Table 2.7 (page 23). Cross-verified: Table 2.9 (p29) row 27 = 807. Consistent."),
        ("Section 11", "Third party information procedure (complete section)", 1408, 1.97,
         "Reported in Table 2.7 (page 23). Cross-verified: Table 2.9 (p29) row 28 = 1408. Consistent."),
        ("Section 24", "Exempted intelligence and security organisations", 9661, 13.55,
         "Reported in Table 2.7 (page 23). Cross-verified: Table 2.9 (p29) row 29 = 9661. Consistent."),
        ("Others", "Other provisions / reasons not specified", 23712, 33.25,
         "Reported in Table 2.7 (page 23). Cross-verified: Table 2.9 (p29) row 30 = 23712. Consistent."),
        ("GRAND TOTAL", "All provisions combined", TOTAL, 100.0,
         f"Grand total invocations. Verification: S8(1) {S8_TOTAL} + S9 807 + S11 1408 + S24 9661 + Others 23712 = {S8_TOTAL+807+1408+9661+23712}. Invocations (71321) exceed rejected requests (64344) because multiple sections can be cited per rejection decision.")
    ]
    for (prov, det, cnt, pct, note) in agg:
        rows.append({
            "financial_year": YEAR,
            "provision": prov,
            "provision_detail": det,
            "invocations_count": cnt,
            "invocations_pct_of_total": pct,
            "reporting_period": "1 April 2018 to 31 March 2019",
            "source_file": "table_page_23_1.csv; table_page_29_1.csv",
            "pdf_page": "23; 29",
            "table_number": "Table 2.7; Table 2.9",
            "source_table": "Sections Invoked for Rejection; Summary of Annual Returns",
            "notes": note
        })
    write_csv(CLEANED_DIR / "rejection_grounds.csv", FN, rows)

def generate_appeals_statistics():
    FN = ["financial_year", "level", "entity_name", "entity_type",
          "received", "disposed", "pending",
          "source_file", "pdf_page", "table_number", "source_table", "notes"]
    rows = []

    # National first appeals
    rows.append({
        "financial_year": YEAR,
        "level": "First Appeal",
        "entity_name": "National Total",
        "entity_type": "Aggregate",
        "received": 151481,
        "disposed": 99618,
        "pending": "NA",
        "source_file": "table_page_28_1.csv",
        "pdf_page": "28",
        "table_number": "Table 2.9",
        "source_table": "Summary of Annual Returns 2018-19",
        "notes": "Rows 8-9 of Table 2.9. Disposal rate = 99618/151481 = 65.76% (also reported in Sec 2.5 p24). Closing pendency not stated as an explicit balance sheet figure."
    })

    # National second appeals & complaints
    rows.append({
        "financial_year": YEAR,
        "level": "Second Appeal/Complaint",
        "entity_name": "National Total",
        "entity_type": "Aggregate",
        "received": 22736,
        "disposed": 17188,
        "pending": 29655,
        "source_file": "table_page_31_1.csv",
        "pdf_page": "31",
        "table_number": "Section 3.2.2",
        "source_table": "Registration/Disposal of cases during 2018-19 in the Commission",
        "notes": "Official Commission database statistics. Closing pendency as on 1st April 2019: 29655."
    })

    # Ministry-level FA and SA from Table 2.8 (pages 24-25)
    min_appeals = [
        (1, "Ministry Of Finance", 25394, 5141),
        (2, "Ministry Of Communications & Information Technology", 10159, 1766),
        (3, "UT Of Delhi", 12086, 2540),
        (4, "Ministry Of Railways", 14457, 1954),
        (5, "Ministry Of Human Resource Development", 16581, 1395),
        (6, "Ministry Of Defence", 15028, 1345),
        (7, "Ministry Of Labour & Employment", 6720, 522),
        (8, "Ministry Of Home Affairs", 7321, 983),
        (9, "Ministry Of Personnel, Public Grievances & Pensions", 4994, 641),
        (10, "Ministry Of Health & Family Welfare", 3714, 424),
        (11, "Ministry Of Housing & Urban Affairs", 3558, 536),
        (12, "Ministry Of Petroleum & Natural Gas", 2777, 560),
        (13, "UT Of Chandigarh", 878, 176),
        (14, "Ministry Of Agriculture", 1087, 236),
        (15, "Ministry Of Road Transport & Highways", 1824, 159),
        (16, "Ministry Of Coal", 1998, 353),
        (17, "Ministry Of Consumer Affairs, Food, & Public Distribution", 1680, 189),
        (18, "Ministry Of Civil Aviation", 1110, 167),
        (19, "Prime Minister’s Office", 2000, 259),
        (20, "Ministry Of Corporate Affairs", 908, 127),
    ]
    for (rank, name, fa, sa) in min_appeals:
        base_note = f"Rank {rank} in Table 2.8. Disposed and pending not reported at ministry level in Table 2.8."
        rows.append({
            "financial_year": YEAR,
            "level": "First Appeal",
            "entity_name": name,
            "entity_type": "Ministry/Department/UT",
            "received": fa,
            "disposed": "NA",
            "pending": "NA",
            "source_file": "table_page_24_1.csv; table_page_25_1.csv",
            "pdf_page": "24; 25",
            "table_number": "Table 2.8",
            "source_table": "Top twenty Public Authorities receiving RTI Applications, First Appeals, Second Appeals",
            "notes": base_note
        })
        rows.append({
            "financial_year": YEAR,
            "level": "Second Appeal/Complaint",
            "entity_name": name,
            "entity_type": "Ministry/Department/UT",
            "received": sa,
            "disposed": "NA",
            "pending": "NA",
            "source_file": "table_page_24_1.csv; table_page_25_1.csv",
            "pdf_page": "24; 25",
            "table_number": "Table 2.8",
            "source_table": "Top twenty Public Authorities receiving RTI Applications, First Appeals, Second Appeals",
            "notes": base_note
        })
    write_csv(CLEANED_DIR / "appeals_statistics.csv", FN, rows)

def generate_accountability_statistics():
    FN = ["financial_year", "metric", "value", "unit",
          "source_file", "pdf_page", "table_number", "source_table", "notes"]
    rows = [
        {"financial_year": YEAR, "metric": "disciplinary_actions_taken", "value": 9, "unit": "count",
         "source_file": "table_page_28_1.csv; table_page_45_1.csv", "pdf_page": "28; 45",
         "table_number": "Table 2.9 (row 11); Annexure-1 (row 11)",
         "source_table": "Summary of Annual Returns 2018-19; Annexure-1 Grand Total",
         "notes": "Number of cases where disciplinary action taken against any officer in respect of administration of RTI Act 2005. Cross-verified: Table 2.9 p28=9, Annexure-1 p45/162=9. Consistent."},
        {"financial_year": YEAR, "metric": "fee_application_collected_rs", "value": 6142217, "unit": "INR",
         "source_file": "table_page_162_1.csv", "pdf_page": "162",
         "table_number": "Annexure-1 Grand Total (row 10)",
         "source_table": "Annexure-1 PA-wise Annual Return Data - Grand Total",
         "notes": "Application fee collected across all PAs. Source: Annexure-1 Grand Total row 10 'Fee (Application) Collected (Rs.)'. NOT a penalty."},
        {"financial_year": YEAR, "metric": "additional_charges_collected_rs", "value": 3746331, "unit": "INR",
         "source_file": "table_page_162_1.csv", "pdf_page": "162",
         "table_number": "Annexure-1 Grand Total (row 11)",
         "source_table": "Annexure-1 PA-wise Annual Return Data - Grand Total",
         "notes": "Additional charges collected across all PAs (copying, inspection, etc.). Source: Annexure-1 Grand Total row 11 'Addl. Charges Collected (Rs.)'. NOT a penalty."},
        {"financial_year": YEAR, "metric": "section20_penalty_collected_by_pas_rs", "value": 472140, "unit": "INR",
         "source_file": "table_page_162_1.csv", "pdf_page": "162",
         "table_number": "Annexure-1 Grand Total (row 12)",
         "source_table": "Annexure-1 PA-wise Annual Return Data - Grand Total",
         "notes": "Section 20 penalty collected by Public Authorities as reported in Annual Returns. Source: Annexure-1 Grand Total row 12 'Penalty Collected (Rs.)'."},
        {"financial_year": YEAR, "metric": "total_amount_collected_by_pas_rs", "value": 10360688, "unit": "INR",
         "source_file": "table_page_28_1.csv; table_page_45_1.csv; table_page_162_1.csv", "pdf_page": "28; 45; 162",
         "table_number": "Table 2.9 (row 12); Annexure-1 (row 12)",
         "source_table": "Summary of Annual Returns 2018-19; Annexure-1 Grand Total",
         "notes": "Composite total of application fee + additional charges + penalty collected by PAs. Reconciles exactly: 6142217 + 3746331 + 472140 = 10360688. VERIFIED to exact rupee."},
        {"financial_year": YEAR, "metric": "section20_1_penalties_imposed_by_cic_rs", "value": 3041000, "unit": "INR",
         "source_file": "table_page_31_1.csv", "pdf_page": "31",
         "table_number": "Section 3.3.1 narrative",
         "source_table": "Imposition and realization of penalty by the Commission during 2018-2019",
         "notes": "Total penalty amount imposed by CIC under Section 20(1) of RTI Act 2005 during 2018-19."},
        {"financial_year": YEAR, "metric": "section20_1_penalties_realized_by_cic_rs", "value": 3210527, "unit": "INR",
         "source_file": "table_page_31_1.csv", "pdf_page": "31",
         "table_number": "Section 3.3.1 narrative",
         "source_table": "Imposition and realization of penalty by the Commission during 2018-2019",
         "notes": "Total penalty amount received/realized by CIC. Narrative explains that realized penalties include recoveries from prior reporting years."},
        {"financial_year": YEAR, "metric": "penalty_orders_stayed_set_aside_high_courts", "value": 32, "unit": "count",
         "source_file": "table_page_31_1.csv", "pdf_page": "31",
         "table_number": "Section 3.3.1 narrative",
         "source_table": "Imposition and realization of penalty by the Commission during 2018-2019",
         "notes": "Penalty orders of the Commission set aside or stayed by Hon'ble High Courts during the year, collectively involving Rs. 5,85,000 (of which Rs. 70,000 had already been recovered prior to the stay orders)."}
    ]
    write_csv(CLEANED_DIR / "accountability_statistics.csv", FN, rows)

def generate_institutional_compliance():
    FN = ["financial_year", "entity_name", "entity_type", "pa_registered", "pa_compliant",
          "pa_non_compliant", "compliance_pct_reported", "capios", "cpios", "faas",
          "source_file", "pdf_page", "table_number", "source_table", "notes"]
    rows = []

    # 14-year time series from Table 2.1 (page 13)
    ts = [
        ("2005-06", 938, 837, 101, 89.23),
        ("2006-07", 1412, 1168, 244, 82.72),
        ("2007-08", 1597, 1382, 215, 86.54),
        ("2008-09", 1770, 1528, 242, 86.33),
        ("2009-10", 1847, 1427, 420, 77.26),
        ("2010-11", 2149, 1452, 697, 67.57),
        ("2011-12", 2314, 1594, 720, 68.89),
        ("2012-13", 2333, 1693, 640, 72.57),
        ("2013-14", 2276, 1713, 563, 75.26),
        ("2014-15", 2030, 1526, 504, 75.17),
        ("2015-16", 2023, 1801, 222, 89.03),
        ("2016-17", 2092, 1928, 164, 92.16),
        ("2017-18", 2079, 1993, 86, 95.86),
        ("2018-19", 2145, 2145, 0, 100.00),
    ]
    for (yr, reg, comp, noncomp, pct) in ts:
        cur = (yr == "2018-19")
        rows.append({
            "financial_year": yr,
            "entity_name": "National Total",
            "entity_type": "Annual Aggregate",
            "pa_registered": reg,
            "pa_compliant": comp,
            "pa_non_compliant": noncomp,
            "compliance_pct_reported": pct,
            "capios": 63869 if cur else "NA",
            "cpios": 24048 if cur else "NA",
            "faas": 9309 if cur else "NA",
            "source_file": "table_page_13_1.csv; table_page_26_1.csv" if cur else "table_page_13_1.csv",
            "pdf_page": "13; 26" if cur else "13",
            "table_number": "Table 2.1; Sec 2.7" if cur else "Table 2.1",
            "source_table": "No. of Public Authorities registered and percentage compliance in last 14 years",
            "notes": "100% compliance achieved in 2018-19 with all 2145 registered PAs submitting returns." if cur else "Historic time series from Table 2.1."
        })

    # Category compliance from Table 2.3 (page 17)
    cats = [
        ("Independent Ministry/Department", 110, 110, 0, 100.0),
        ("Department under Ministry", 123, 123, 0, 100.0),
        ("Attached Office", 177, 177, 0, 100.0),
        ("Subordinate Office", 890, 890, 0, 100.0),
        ("Corporation", 50, 50, 0, 100.0),
        ("Govt. Autonomous Body", 559, 559, 0, 100.0),
        ("Govt. Company under Companies Act", 65, 65, 0, 100.0),
        ("Others", 171, 171, 0, 100.0),
    ]
    for (name, reg, comp, noncomp, pct) in cats:
        rows.append({
            "financial_year": YEAR,
            "entity_name": name,
            "entity_type": "PA Category",
            "pa_registered": reg,
            "pa_compliant": comp,
            "pa_non_compliant": noncomp,
            "compliance_pct_reported": pct,
            "capios": "NA",
            "cpios": "NA",
            "faas": "NA",
            "source_file": "table_page_17_1.csv",
            "pdf_page": "17",
            "table_number": "Table 2.3",
            "source_table": "Total number of Public Authorities Registered by Category",
            "notes": f"Category breakdown of PAs. All categories achieved 100% submission compliance in 2018-19. Sum of registered PAs = {sum(x[1] for x in cats)} = 2145."
        })

    # Designated officials 5-year trend (page 26 table)
    officials_trend = [
        ("2014-15", 2030, 58247, 19597, 7781),
        ("2015-16", 2023, 66025, 22210, 8766),
        ("2016-17", 2092, 64711, 23561, 9497),
        ("2017-18", 2079, 55176, 23213, 9314),
        ("2018-19", 2145, 63869, 24048, 9309),
    ]
    for (yr, pa, cap, cp, fa) in officials_trend:
        if yr != "2018-19": # 2018-19 is already included above as national total
            rows.append({
                "financial_year": yr,
                "entity_name": "National Total (Officials Trend)",
                "entity_type": "Designated Officials Multi-Year",
                "pa_registered": pa,
                "pa_compliant": "NA",
                "pa_non_compliant": "NA",
                "compliance_pct_reported": "NA",
                "capios": cap,
                "cpios": cp,
                "faas": fa,
                "source_file": "table_page_26_1.csv",
                "pdf_page": "26",
                "table_number": "Section 2.7 / Figure 2.4",
                "source_table": "Details of officials designated as CAPIOs, CPIOs and FAAs",
                "notes": f"Multi-year trend of designated RTI officials from Section 2.7 (page 26). Total officers for {yr} = {cap+cp+fa}."
            })
    write_csv(CLEANED_DIR / "institutional_compliance.csv", FN, rows)

def generate_data_discrepancies():
    FN = ["financial_year", "metric", "source_1", "value_1", "source_2", "value_2", "description", "resolution_status"]
    rows = [
        {
            "financial_year": YEAR,
            "metric": "RTI rejection decisions vs total section invocations",
            "source_1": "table_page_18_1.csv (Table 2.4 p18) & table_page_28_1.csv (Table 2.9 p28)",
            "value_1": "64344 (decisions where information rejected)",
            "source_2": "table_page_23_1.csv (Table 2.7 p23) & table_page_29_1.csv (Table 2.9 p29)",
            "value_2": "71321 (total section invocations)",
            "description": "Total section invocations (71,321) exceeds rejection decisions (64,344) by 6,977. One RTI rejection decision can cite multiple exempt sections simultaneously (footnote # in Table 2.7).",
            "resolution_status": "Resolved — different metrics; invocations >= decisions by design."
        },
        {
            "financial_year": YEAR,
            "metric": "Composite collections vs Section 20 penalty collected",
            "source_1": "table_page_28_1.csv (Table 2.9 row 12 p28) & table_page_45_1.csv (Annexure-1 p45)",
            "value_1": "10360688 (composite fee + charges + penalty)",
            "source_2": "table_page_162_1.csv (Annexure-1 Grand Total row 12 p162)",
            "value_2": "472140 (Section 20 penalty collected)",
            "description": "Table 2.9 row 12 reports a composite total of Rs. 10,360,688. The disaggregated breakdown was identified in Annexure-1 Grand Total: Fee = Rs. 6,142,217; Additional Charges = Rs. 3,746,331; Penalty = Rs. 472,140 (summing exactly to Rs. 10,360,688).",
            "resolution_status": "Resolved — disaggregated components identified and verified to exact rupee."
        },
        {
            "financial_year": YEAR,
            "metric": "CIC Section 20(1) penalty imposed vs realized vs PA penalty collected",
            "source_1": "table_page_31_1.csv (Section 3.3.1 p31)",
            "value_1": "3041000 (imposed by CIC) / 3210527 (realized by CIC)",
            "source_2": "table_page_162_1.csv (Annexure-1 Grand Total row 12 p162)",
            "value_2": "472140 (collected by PAs)",
            "description": "CIC imposed Rs. 30,41,000 and realized Rs. 32,10,527 directly at the Central Commission level. Meanwhile, Public Authorities reported Rs. 4,72,140 in penalties collected across their respective accounts.",
            "resolution_status": "Resolved — preserved as distinct metrics with explicit institutional context."
        },
        {
            "financial_year": YEAR,
            "metric": "Historical registered PAs count for 2015-16",
            "source_1": "table_page_13_1.csv (Table 2.1 p13) & table_page_18_1.csv (Table 2.4 p18)",
            "value_1": "2023",
            "source_2": "AR 2023-24 Table 2.3",
            "value_2": "2024",
            "description": "In 2018-19 Table 2.1 and Table 2.4, registered PAs for 2015-16 is recorded as 2023. In some subsequent annual reports (e.g. 2023-24), it is cited as 2024.",
            "resolution_status": "Documented — 2018-19 reported value (2023) preserved for historical integrity."
        }
    ]
    write_csv(CLEANED_DIR / "data_discrepancies.csv", FN, rows)

if __name__ == "__main__":
    generate_national_statistics()
    generate_ministry_statistics()
    generate_rejection_grounds()
    generate_appeals_statistics()
    generate_accountability_statistics()
    generate_institutional_compliance()
    generate_data_discrepancies()
    print("All 2018-19 datasets successfully created!")
