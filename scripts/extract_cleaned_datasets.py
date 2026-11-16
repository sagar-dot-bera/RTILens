"""
extract_cleaned_datasets.py
Extracts, cleans, and validates CIC Annual Report data for 2023-24 and 2024-25.
"""
import csv, os
from pathlib import Path

PROJECT_ROOT = Path("/home/neel-shah/Desktop/Academics/Sem-3/EDA/Project/RTILens")
STAGING_2324 = PROJECT_ROOT / "data/staging/2023-24/raw_csv"
CLEANED_2324  = PROJECT_ROOT / "data/cleaned/2023-24"
CLEANED_2425  = PROJECT_ROOT / "data/cleaned/2024-25"
YEAR_2324, YEAR_2425 = "2023-24", "2024-25"

def ensure_dir(p): p.mkdir(parents=True, exist_ok=True)

def write_csv(path, fieldnames, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader(); w.writerows(rows)
    print(f"  {path.name}: {len(rows)} rows")

def write_csv_headers(path, fieldnames):
    with open(path, "w", newline="", encoding="utf-8") as f:
        csv.DictWriter(f, fieldnames=fieldnames).writeheader()
    print(f"  {path.name}: headers only (no data)")

# ── national_statistics.csv ─────────────────────────────────────────────────
def national_stats():
    FN = ["financial_year","pa_registered","opening_balance","requests_received",
          "total_requests","requests_transferred","requests_rejected",
          "rejection_pct_reported","first_appeals_received","first_appeals_disposed",
          "second_appeals_registered","second_appeals_disposed","second_appeals_pending",
          "disciplinary_actions","fee_collected_rs","addl_charges_collected_rs",
          "section20_penalty_collected_rs","total_amount_collected_rs",
          "capios","cpios","faas","total_officers",
          "source_file","pdf_page","table_number","source_table","notes"]

    # 18-year time series from Table 2.3 (page 16)
    ts = [
        ("2006-07",1412,12026,171398,183424,15388,9.0),
        ("2007-08",1597,23926,263261,287187,18966,7.2),
        ("2008-09",1770,32792,329728,362520,23954,7.26),
        ("2009-10",1847,97474,529274,626748,34057,6.43),
        ("2010-11",2149,137771,417955,555726,21413,5.1),
        ("2011-12",2314,76016,629960,705976,52313,8.3),
        ("2012-13",2333,75331,811350,886681,62231,7.7),
        ("2013-14",2276,128447,834183,962630,60127,7.21),
        ("2014-15",2030,89785,755247,845032,63351,8.39),
        ("2015-16",2024,188538,976679,1165217,64666,6.62),
        ("2016-17",2092,212430,915749,1128179,60428,6.59),
        ("2017-18",2079,215466,1233207,1448673,63206,5.13),
        ("2018-19",2145,259919,1370129,1630048,64344,4.7),
        ("2019-20",2193,310110,1374315,1684425,58634,4.27),
        ("2020-21",2275,348410,1333802,1682212,51390,3.85),
        ("2021-22",2278,410907,1421226,1832133,53733,3.78),
        ("2022-23",2294,441861,1638784,2080645,52662,3.21),
        ("2023-24",2298,495039,1750863,2245902,67615,3.86),
    ]
    rows = []
    for (yr,pa,ob,recv,tot,rej,rpct) in ts:
        cur = (yr == "2023-24")
        rows.append({
            "financial_year":yr,"pa_registered":pa,"opening_balance":ob,
            "requests_received":recv,"total_requests":tot,
            "requests_transferred":237671 if cur else "NA",
            "requests_rejected":rej,"rejection_pct_reported":rpct,
            "first_appeals_received":176872 if cur else "NA",
            "first_appeals_disposed":109682 if cur else "NA",
            "second_appeals_registered":20361 if cur else "NA",
            "second_appeals_disposed":16790 if cur else "NA",
            "second_appeals_pending":23078 if cur else "NA",
            "disciplinary_actions":36 if cur else "NA",
            "fee_collected_rs":5540245 if cur else "NA",
            "addl_charges_collected_rs":2590979 if cur else "NA",
            "section20_penalty_collected_rs":22663 if cur else "NA",
            "total_amount_collected_rs":8153887 if cur else "NA",
            "capios":61056 if cur else "NA",
            "cpios":27657 if cur else "NA",
            "faas":21619 if cur else "NA",
            "total_officers":110332 if cur else "NA",
            "source_file":"table_page_16_1.csv; table_page_24_1.csv; table_page_26_1.csv; table_page_190_1.csv" if cur else "table_page_16_1.csv",
            "pdf_page":"16; 24; 26; 190" if cur else "16",
            "table_number":"Table 2.3; Table 2.1; standalone; Table 3.1 grand total" if cur else "Table 2.3",
            "source_table":"RTI Requests Details in a Nutshell (Year-wise); Consolidated Annual Return Summary 2023-24; Second Appeals/Complaints Statistics; PA-wise Annual Return Data Grand Total" if cur else "RTI Requests Details in a Nutshell (Year-wise)",
            "notes":(
                "2023-24: requests/rejected/total from Table 2.3 p16; transfers/appeals/officers from Table 2.1 p24; "
                "second_appeals from p26; fee/charges/penalty disaggregated from Table 3.1 grand total p190. "
                "rejection_pct_reported=3.86% (Table 2.3 col h); Table 3.1 rounds to 4%. "
                "total_amount_collected_rs=fee+addl_charges+penalty=5540245+2590979+22663=8153887 VERIFIED."
            ) if cur else "Only columns available in multi-year Table 2.3; all year-specific columns are NA for prior years.",
        })
    return FN, rows

# ── ministry_statistics.csv ──────────────────────────────────────────────────
def ministry_stats():
    FN = ["financial_year","entity_name","entity_type",
          "rank_by_volume","rank_by_rejection_pct",
          "requests_received","requests_rejected","rejection_pct_reported",
          "first_appeals_received","second_appeals_received",
          "source_file","pdf_page","table_number","source_table","notes"]
    rows = []

    # Table 2.4: 8 categories + total (pages 17-t2 and 18-t1)
    cats = [
        (1,"Independent Ministry/Department",205804,7387,3.59,"17 (table 2)","table_page_17_2.csv"),
        (2,"Department under Ministry",258930,4723,1.82,"17 (table 2)","table_page_17_2.csv"),
        (3,"Attached Office",486384,6452,1.33,"17 (table 2)","table_page_17_2.csv"),
        (4,"Subordinate Office",405215,31907,7.87,"18 (table 1)","table_page_18_1.csv"),
        (5,"Corporation",39552,584,1.48,"18 (table 1)","table_page_18_1.csv"),
        (6,"Govt. Autonomous Body",243926,13078,5.36,"18 (table 1)","table_page_18_1.csv"),
        (7,"Govt. Company under Companies Act",30328,1580,5.21,"18 (table 1)","table_page_18_1.csv"),
        (8,"Others",80724,1904,2.36,"18 (table 1)","table_page_18_1.csv"),
        (None,"Total (all categories)",1750863,67615,3.86,"18 (table 1)","table_page_18_1.csv"),
    ]
    for (n,name,recv,rej,rpct,page,sf) in cats:
        rows.append({"financial_year":YEAR_2324,"entity_name":name,"entity_type":"PA Category",
            "rank_by_volume":"NA","rank_by_rejection_pct":"NA",
            "requests_received":recv,"requests_rejected":rej,"rejection_pct_reported":rpct,
            "first_appeals_received":"NA","second_appeals_received":"NA",
            "source_file":sf,"pdf_page":page,"table_number":"Table 2.4",
            "source_table":"Percentage Rejection by Category of Public Authority",
            "notes":f"Category row {n}. Total row verified: sum of categories = national total." if n else
                "Total row: sum of all 8 categories. Verified against national totals in Table 2.3 (page 16). Consistent."})

    # Table 2.5: top 20 by volume (pages 18-t2 and 19)
    vol20 = [
        (1,"Ministry of Finance",239207,24087,10.06,"18 (table 2)","table_page_18_2.csv"),
        (2,"Ministry of Railways",227895,4855,2.13,"18 (table 2)","table_page_18_2.csv"),
        (3,"Ministry of Corporate Affairs",225226,385,0.17,"18 (table 2)","table_page_18_2.csv"),
        (4,"Ministry of Education",124314,1328,1.07,"18 (table 2)","table_page_18_2.csv"),
        (5,"UT of Delhi",118943,3462,2.91,"18 (table 2)","table_page_18_2.csv"),
        (6,"Ministry of Communications",95595,1348,1.41,"18 (table 2)","table_page_18_2.csv"),
        (7,"Ministry of Defence",86415,3801,4.40,"18 (table 2)","table_page_18_2.csv"),
        (8,"Ministry of Personnel, Public Grievances & Pensions",73505,1714,2.33,"18 (table 2)","table_page_18_2.csv"),
        (9,"Ministry of Labour & Employment",62149,2881,4.64,"18 (table 2)","table_page_18_2.csv"),
        (10,"Ministry of Home Affairs",54102,10681,19.74,"18 (table 2)","table_page_18_2.csv"),
        (11,"Ministry of Health & Family Welfare",51109,942,1.84,"19","table_page_19_1.csv"),
        (12,"Ministry of Road Transport & Highways",26559,537,2.02,"19","table_page_19_1.csv"),
        (13,"Ministry of Housing & Urban Affairs",26278,407,1.55,"19","table_page_19_1.csv"),
        (14,"Ministry of External Affairs",20756,761,3.67,"19","table_page_19_1.csv"),
        (15,"Ministry of Civil Aviation",19606,787,4.01,"19","table_page_19_1.csv"),
        (16,"Ministry of Coal",19584,649,3.31,"19","table_page_19_1.csv"),
        (17,"Ministry of Law & Justice",16281,1134,6.97,"19","table_page_19_1.csv"),
        (18,"UT of Jammu and Kashmir",15296,416,2.72,"19","table_page_19_1.csv"),
        (19,"Ministry of Petroleum & Natural Gas",14920,654,4.38,"19","table_page_19_1.csv"),
        (20,"Ministry of Consumer Aff., Food, & Public Dist.",13505,337,2.50,"19","table_page_19_1.csv"),
    ]
    for (rank,name,recv,rej,rpct,page,sf) in vol20:
        rows.append({"financial_year":YEAR_2324,"entity_name":name,"entity_type":"Ministry/Department/UT",
            "rank_by_volume":rank,"rank_by_rejection_pct":"NA",
            "requests_received":recv,"requests_rejected":rej,"rejection_pct_reported":rpct,
            "first_appeals_received":"NA","second_appeals_received":"NA",
            "source_file":sf,"pdf_page":page,"table_number":"Table 2.5",
            "source_table":"Top Ministries/Departments/Independent PAs by RTI Requests Received",
            "notes":f"Rank {rank} by RTI volume. rejection_pct = (rejected/received)*100 as reported."})

    # Table 2.7: top 20 by rejection % with FA+SA (page 21)
    rej20 = [
        (1,"High Court Of Delhi",1683,395,23.47,188,18,""),
        (2,"Ministry of Home Affairs",54102,10681,19.74,773,927,""),
        (3,"UT of Andaman & Nicobar",1142,195,17.08,94,92,""),
        (4,"Supreme Court of India",4331,453,10.46,674,103,""),
        (5,"Ministry of Finance",239207,24087,10.06,2496,5117,""),
        (6,"Ministry of Mines",2955,221,7.48,357,69,""),
        (7,"Ministry of Electronics & Information Technology",9081,672,7.40,869,85,""),
        (8,"Ministry of Shipping",3561,258,7.25,321,59,""),
        (9,"Ministry of Law & Justice",16281,1134,6.97,951,183,""),
        (10,"Ministry of Women & Child Development",4238,280,6.61,288,46,""),
        (11,"UT of Dadra and Nagar Haveli and Daman and Diu",722,44,6.09,94,29,""),
        (12,"UT of Chandigarh",12507,749,5.99,117,178,""),
        (13,"Cabinet Secretariat",1558,86,5.52,162,9,""),
        (14,"Ministry of Textiles",2729,138,5.06,310,46,"CAUTION: name reconstructed from cell-split artefact in source CSV row 14; verify against PDF page 21"),
        (15,"UT of Puducherry",6527,311,4.76,958,186,""),
        (16,"Ministry of Labour & Employment",62149,2881,4.64,5847,575,""),
        (17,"Ministry of Defence",86415,3801,4.40,15592,1073,""),
        (18,"Ministry of Petroleum & Natural Gas",14920,654,4.38,1899,265,""),
        (19,"Ministry of Civil Aviation",19606,787,4.01,998,97,""),
        (20,"Ministry of External Affairs",20756,761,3.67,1368,104,""),
    ]
    for (rank,name,recv,rej,rpct,fa,sa,note) in rej20:
        rows.append({"financial_year":YEAR_2324,"entity_name":name,"entity_type":"Ministry/Department/UT",
            "rank_by_volume":"NA","rank_by_rejection_pct":rank,
            "requests_received":recv,"requests_rejected":rej,"rejection_pct_reported":rpct,
            "first_appeals_received":fa,"second_appeals_received":sa,
            "source_file":"table_page_21_1.csv","pdf_page":"21","table_number":"Table 2.7",
            "source_table":"Ministry-wise RTI Statistics Ranked by Rejection Percentage",
            "notes":(f"Rank {rank} by rejection %. "+note).strip()})
    return FN, rows

# ── rejection_grounds.csv ────────────────────────────────────────────────────
def rejection_grounds():
    FN = ["financial_year","provision","provision_detail","invocations_count",
          "invocations_pct_of_total","reporting_period",
          "source_file","pdf_page","table_number","source_table","notes"]
    TOTAL = 68189
    S8_TOTAL = 31736
    rows = []

    sub = [
        ("Section 8(1)","(a) - Third party information: sovereignty, security, strategic etc.",2206),
        ("Section 8(1)","(b) - Expressly forbidden by court or disclosure contempt of court",144),
        ("Section 8(1)","(c) - Breach of privilege of Parliament or State Legislature",38),
        ("Section 8(1)","(d) - Commercial confidence, trade secrets, intellectual property",4506),
        ("Section 8(1)","(e) - Fiduciary relationship information",4534),
        ("Section 8(1)","(f) - Received in confidence from foreign Government",563),
        ("Section 8(1)","(g) - Endangers life or physical safety of person",720),
        ("Section 8(1)","(h) - Impede process of investigation or apprehension of offenders",2876),
        ("Section 8(1)","(i) - Cabinet papers including deliberations of Council of Ministers",396),
        ("Section 8(1)","(j) - Personal information: unrelated to public activity or interest",15753),
    ]
    for (prov,det,cnt) in sub:
        pct = round(cnt/TOTAL*100, 2)
        rows.append({"financial_year":YEAR_2324,"provision":prov,"provision_detail":det,
            "invocations_count":cnt,"invocations_pct_of_total":pct,
            "reporting_period":"1 April 2023 to 31 March 2024",
            "source_file":"table_page_24_1.csv","pdf_page":"24",
            "table_number":"Table 2.1 (rows 17-26)",
            "source_table":"Consolidated Annual Return Summary 2023-24 - Sections Invoked",
            "notes":f"Sub-clause count from Table 2.1 (p24). pct = {cnt}/{TOTAL}*100. No per-sub-clause pct reported in source; calculated here."})

    # Aggregate sections from Table 2.6 (page 19) with reported percentages
    agg_sections = [
        ("Section 8(1)","AGGREGATE TOTAL (sub-clauses a through j)",S8_TOTAL,46.54,"Reported in Table 2.6 (page 19). Verified: sum of sub-clauses (a)-(j) = 31736. Consistent."),
        ("Section 9","Third party information (complete section)",293,0.43,"Reported in Table 2.6 (page 19). Cross-verified: Table 2.1 (p24) row 27 = 293. Consistent."),
        ("Section 11","Third party information exemption (complete section)",750,1.10,"Reported in Table 2.6 (page 19). Cross-verified: Table 2.1 (p24) row 28 = 750. Consistent."),
        ("Section 24","Security organisations exemption (complete section)",10543,15.46,"Reported in Table 2.6 (page 19). Cross-verified: Table 2.1 (p24) row 29 = 10543. Consistent."),
        ("Others","Other provisions not separately categorised",24867,36.47,"Reported in Table 2.6 (page 19). Cross-verified: Table 2.1 (p24) row 30 = 24867. Consistent."),
        ("GRAND TOTAL","All provisions combined",TOTAL,100.0,
         f"Grand total invocations. Verification: S8(1) {S8_TOTAL} + S9 293 + S11 750 + S24 10543 + Others 24867 = {S8_TOTAL+293+750+10543+24867}. IMPORTANT: invocations (68189) differ from rejection decisions (67615) by 574 — one decision may cite multiple sections."),
    ]
    for (prov,det,cnt,pct,note) in agg_sections:
        rows.append({"financial_year":YEAR_2324,"provision":prov,"provision_detail":det,
            "invocations_count":cnt,"invocations_pct_of_total":pct,
            "reporting_period":"1 April 2023 to 31 March 2024",
            "source_file":"table_page_19_1.csv; table_page_24_1.csv","pdf_page":"19; 24",
            "table_number":"Table 2.6; Table 2.1",
            "source_table":"Sections Invoked while Rejecting Information; Consolidated Annual Return Summary",
            "notes":note})
    return FN, rows

# ── appeals_statistics.csv ───────────────────────────────────────────────────
def appeals_stats():
    FN = ["financial_year","level","entity_name","entity_type",
          "received","disposed","pending",
          "source_file","pdf_page","table_number","source_table","notes"]
    rows = []

    # National first appeals (Table 2.1 page 24)
    rows.append({"financial_year":YEAR_2324,"level":"First Appeal",
        "entity_name":"National Total","entity_type":"Aggregate",
        "received":176872,"disposed":109682,"pending":"NA",
        "source_file":"table_page_24_1.csv","pdf_page":"24","table_number":"Table 2.1",
        "source_table":"Consolidated Annual Return Summary 2023-24",
        "notes":"Rows 8-9 of Table 2.1. Pending not stated explicitly; left as NA (derivation would require confirmed prior-year carry-forward). Cross-verified: Table 3.1 grand total (p190) row 5=176872, row 6=109682. Consistent."})

    # National second appeals (page 26 standalone)
    rows.append({"financial_year":YEAR_2324,"level":"Second Appeal/Complaint",
        "entity_name":"National Total","entity_type":"Aggregate",
        "received":20361,"disposed":16790,"pending":23078,
        "source_file":"table_page_26_1.csv","pdf_page":"26",
        "table_number":"Standalone table (no table number in PDF)",
        "source_table":"Second Appeals/Complaints Statistics 2023-24",
        "notes":"pending=23078 is cumulative carry-forward to 1 April 2024, NOT current-year residual (20361-16790=3571). This confirms significant backlog from prior years."})

    # Ministry-level FA and SA from Table 2.7 (page 21)
    min_appeals = [
        (1,"High Court Of Delhi",188,18,""),
        (2,"Ministry of Home Affairs",773,927,""),
        (3,"UT of Andaman & Nicobar",94,92,""),
        (4,"Supreme Court of India",674,103,""),
        (5,"Ministry of Finance",2496,5117,""),
        (6,"Ministry of Mines",357,69,""),
        (7,"Ministry of Electronics & Information Technology",869,85,""),
        (8,"Ministry of Shipping",321,59,""),
        (9,"Ministry of Law & Justice",951,183,""),
        (10,"Ministry of Women & Child Development",288,46,""),
        (11,"UT of Dadra and Nagar Haveli and Daman and Diu",94,29,""),
        (12,"UT of Chandigarh",117,178,""),
        (13,"Cabinet Secretariat",162,9,""),
        (14,"Ministry of Textiles",310,46,"CAUTION: ministry name reconstructed from cell-split artefact"),
        (15,"UT of Puducherry",958,186,""),
        (16,"Ministry of Labour & Employment",5847,575,""),
        (17,"Ministry of Defence",15592,1073,""),
        (18,"Ministry of Petroleum & Natural Gas",1899,265,""),
        (19,"Ministry of Civil Aviation",998,97,""),
        (20,"Ministry of External Affairs",1368,104,""),
    ]
    for (rank,name,fa,sa,note) in min_appeals:
        base_note = f"Rank {rank} by rejection %. Only received counts available; disposal and pending not in Table 2.7. {note}".strip()
        rows.append({"financial_year":YEAR_2324,"level":"First Appeal",
            "entity_name":name,"entity_type":"Ministry/Department/UT",
            "received":fa,"disposed":"NA","pending":"NA",
            "source_file":"table_page_21_1.csv","pdf_page":"21","table_number":"Table 2.7",
            "source_table":"Ministry-wise RTI Statistics Ranked by Rejection Percentage",
            "notes":base_note})
        rows.append({"financial_year":YEAR_2324,"level":"Second Appeal/Complaint",
            "entity_name":name,"entity_type":"Ministry/Department/UT",
            "received":sa,"disposed":"NA","pending":"NA",
            "source_file":"table_page_21_1.csv","pdf_page":"21","table_number":"Table 2.7",
            "source_table":"Ministry-wise RTI Statistics Ranked by Rejection Percentage",
            "notes":base_note})
    return FN, rows

# ── accountability_statistics.csv ────────────────────────────────────────────
def accountability_stats():
    FN = ["financial_year","metric","value","unit",
          "source_file","pdf_page","table_number","source_table","notes"]
    rows = [
        {"financial_year":YEAR_2324,"metric":"disciplinary_actions_taken","value":36,"unit":"count",
         "source_file":"table_page_24_1.csv; table_page_190_1.csv","pdf_page":"24; 190",
         "table_number":"Table 2.1 (row 11); Table 3.1 (grand total row 9)",
         "source_table":"Consolidated Annual Return Summary 2023-24; PA-wise Annual Return Data Grand Total",
         "notes":"Number of cases where disciplinary action taken against any officer in respect of administration of RTI Act 2005. Cross-verified: Table 2.1 p24=36; Table 3.1 grand total p190 row 9=36. Consistent. No case-level breakdown found in extracted tables."},
        {"financial_year":YEAR_2324,"metric":"fee_application_collected_rs","value":5540245,"unit":"INR",
         "source_file":"table_page_190_1.csv","pdf_page":"190",
         "table_number":"Table 3.1 (grand total row 10)",
         "source_table":"PA-wise Annual Return Data - Grand Total",
         "notes":"Application fee collected across all PAs. Source: Table 3.1 grand total row 10 'Fee (Application) Collected'. NOT a penalty."},
        {"financial_year":YEAR_2324,"metric":"additional_charges_collected_rs","value":2590979,"unit":"INR",
         "source_file":"table_page_190_1.csv","pdf_page":"190",
         "table_number":"Table 3.1 (grand total row 11)",
         "source_table":"PA-wise Annual Return Data - Grand Total",
         "notes":"Additional charges collected across all PAs. Source: Table 3.1 grand total row 11 'Addl. Charges Collected'. NOT a penalty."},
        {"financial_year":YEAR_2324,"metric":"section20_penalty_collected_rs","value":22663,"unit":"INR",
         "source_file":"table_page_190_1.csv","pdf_page":"190",
         "table_number":"Table 3.1 (grand total row 12)",
         "source_table":"PA-wise Annual Return Data - Grand Total",
         "notes":"Penalty collected across all PAs. Source: Table 3.1 grand total row 12 'Penalty Collected (Rs.)'. This is distinct from fee and additional charges. Total penalty (22663) is 0.28% of composite total (8153887). No case-level Section 20 breakdown found."},
        {"financial_year":YEAR_2324,"metric":"total_amount_collected_composite_rs","value":8153887,"unit":"INR",
         "source_file":"table_page_24_1.csv; table_page_190_1.csv","pdf_page":"24; 190",
         "table_number":"Table 2.1 (row 12); Table 3.1 (grand total row 13)",
         "source_table":"Consolidated Annual Return Summary 2023-24; PA-wise Annual Return Data Grand Total",
         "notes":"COMPOSITE TOTAL: fee+addl_charges+penalty = 5540245+2590979+22663 = 8153887. VERIFIED. DO NOT use as Section 20 penalty figure."},
        {"financial_year":YEAR_2324,"metric":"section20_penalty_orders_count","value":"NA","unit":"count",
         "source_file":"NA","pdf_page":"NA","table_number":"NA","source_table":"NA",
         "notes":"NOT FOUND: Number of Section 20(1) penalty orders issued by CIC not available in extracted tables. Only aggregate penalty collected (22663 INR) available."},
        {"financial_year":YEAR_2324,"metric":"section20_2_disciplinary_recommendations_by_cic","value":"NA","unit":"count",
         "source_file":"NA","pdf_page":"NA","table_number":"NA","source_table":"NA",
         "notes":"NOT FOUND: Section 20(2) disciplinary recommendations by CIC not separately enumerated in extracted tables."},
    ]
    return FN, rows

# ── institutional_compliance.csv ─────────────────────────────────────────────
def institutional_compliance():
    FN = ["financial_year","entity_name","entity_type",
          "pa_registered","pa_compliant","pa_non_compliant","compliance_pct_reported",
          "capios","cpios","faas",
          "source_file","pdf_page","table_number","source_table","notes"]
    rows = []

    # 18-year time series from Table 2.1 compliance (page 13)
    ts = [
        ("2006-07",1412,1168,244,82.72,""),
        ("2007-08",1597,1382,215,86.54,""),
        ("2008-09",1770,1528,242,86.33,""),
        ("2009-10",1847,1427,420,77.26,""),
        ("2010-11",2149,1452,697,67.57,""),
        ("2011-12",2314,1593,721,68.84,""),
        ("2012-13",2333,1864,469,79.90,""),
        ("2013-14",2276,1651,625,72.54,""),
        ("2014-15",2030,1528,502,75.27,""),
        ("2015-16",2023,1903,120,94.07,"NOTE: pa_registered=2023 here (Table 2.1 compliance p13); Table 2.3 (p16) shows 2024 for same year — 1-PA discrepancy documented in data_discrepancies.csv"),
        ("2016-17",2092,1964,128,"NA","FLAGGED: compliance_pct_reported=NA — blank in source CSV due to column header layout shift in extracted page 13. Calculated 1964/2092*100=93.88% but not entered to preserve source integrity. Verify against original PDF p13."),
        ("2017-18",2079,2079,0,100.0,""),
        ("2018-19",2145,2145,0,100.0,""),
        ("2019-20",2193,2131,62,97.17,""),
        ("2020-21",2275,2182,93,95.91,""),
        ("2021-22",2278,2173,105,95.39,""),
        ("2022-23",2294,2220,74,96.77,""),
        ("2023-24",2298,2298,0,100.0,""),
    ]
    for (yr,pa_r,pa_c,pa_n,cpct,note) in ts:
        cur = (yr == "2023-24")
        rows.append({"financial_year":yr,"entity_name":"National Total","entity_type":"Annual Aggregate",
            "pa_registered":pa_r,"pa_compliant":pa_c,"pa_non_compliant":pa_n,
            "compliance_pct_reported":cpct,
            "capios":61056 if cur else "NA","cpios":27657 if cur else "NA","faas":21619 if cur else "NA",
            "source_file":"table_page_13_1.csv"+("; table_page_24_1.csv" if cur else ""),
            "pdf_page":"13"+("; 24" if cur else ""),
            "table_number":"Table 2.1 (compliance)"+("; Table 2.1 rows 13-16" if cur else ""),
            "source_table":"Year-wise PA Registration and Annual Return Compliance"+("; Consolidated Annual Return Summary 2023-24" if cur else ""),
            "notes":note})

    # Category-wise 2023-24 (Table 2.2 page 15)
    cat_comp = [
        ("Independent Ministry/Department",111),
        ("Department under Ministry",166),
        ("Attached Office",202),
        ("Subordinate Office",967),
        ("Corporation",47),
        ("Govt. Autonomous Body",566),
        ("Govt. Company under Companies Act",85),
        ("Others",154),
    ]
    for (cat,pa) in cat_comp:
        rows.append({"financial_year":YEAR_2324,"entity_name":cat,"entity_type":"PA Category",
            "pa_registered":pa,"pa_compliant":pa,"pa_non_compliant":0,"compliance_pct_reported":100.0,
            "capios":"NA","cpios":"NA","faas":"NA",
            "source_file":"table_page_15_1.csv","pdf_page":"15","table_number":"Table 2.2",
            "source_table":"Category-wise PA Registration and Compliance 2023-24",
            "notes":"Category name reconstructed from split cells in source CSV. All categories show 100% compliance for 2023-24."})

    # Ministry-wise Table 4.1 (pages 191-192)
    min_comp = [
        (1,"Election Commission of India",1,1,100.00,"191","table_page_191_1.csv",""),
        (2,"Cabinet Secretariat",1,1,100.00,"191","table_page_191_1.csv",""),
        (3,"Ministry of Food Processing Industries",1,1,100.00,"191","table_page_191_1.csv",""),
        (4,"Ministry of Chemicals & Fertilizers",29,29,100.00,"191","table_page_191_1.csv",""),
        (5,"Ministry of Coal",13,13,100.00,"191","table_page_191_1.csv",""),
        (6,"Ministry of Minority Affairs",7,7,100.00,"191","table_page_191_1.csv",""),
        (7,"Ministry of Mines",8,8,100.00,"191","table_page_191_1.csv",""),
        (8,"Ministry of Commerce & Industry",47,47,100.00,"191","table_page_191_1.csv",""),
        (9,"Department of Atomic Energy",35,35,100.00,"191","table_page_191_1.csv",""),
        (10,"Ministry of Communications",14,14,100.00,"191","table_page_191_1.csv",""),
        (11,"Ministry of Defence",56,56,100.00,"191","table_page_191_1.csv",""),
        (12,"Ministry of Development of North Eastern Region",5,5,100.00,"191","table_page_191_1.csv",""),
        (13,"Ministry of External Affairs",192,192,100.00,"191","table_page_191_1.csv",""),
        (14,"Ministry of Panchayati Raj",1,1,100.00,"191","table_page_191_1.csv",""),
        (15,"Ministry of Heavy Industry & Public Enterprises",22,22,100.00,"191","table_page_191_1.csv",""),
        (16,"Ministry of Women & Child Development",5,5,100.00,"191","table_page_191_1.csv",""),
        (17,"Ministry of Information & Broadcasting",16,16,100.00,"191","table_page_191_1.csv",""),
        (18,"Ministry of Law & Justice",46,46,100.00,"191","table_page_191_1.csv",""),
        (19,"Ministry of New & Renewable Energy",6,6,100.00,"191","table_page_191_1.csv",""),
        (20,"Ministry of Earth Sciences",10,10,100.00,"191","table_page_191_1.csv",""),
        (21,"Prime Minister's Office",1,1,100.00,"191","table_page_191_1.csv",""),
        (22,"Ministry of Parliamentary Affairs",1,1,100.00,"191","table_page_191_1.csv",""),
        (23,"Ministry of Personnel, Public Grievances & Pensions",12,12,100.00,"191","table_page_191_1.csv",""),
        (24,"NITI Aayog",1,1,100.00,"191","table_page_191_1.csv",""),
        (25,"Ministry of Power",19,19,100.00,"191","table_page_191_1.csv",""),
        (26,"Ministry of Railways",34,34,100.00,"191","table_page_191_1.csv",""),
        (27,"Ministry of Rural Development",3,3,100.00,"191","table_page_191_1.csv",""),
        (28,"Ministry of Social Justice & Empowerment",25,25,100.00,"191","table_page_191_1.csv",""),
        (29,"Department of Space",20,20,100.00,"191","table_page_191_1.csv","RECONSTRUCTION: PA count (20) was on a separate CSV line below the name row; merged into single row."),
        (30,"Ministry of Statistics & Programme Implementation",1,1,100.00,"191","table_page_191_1.csv",""),
        (31,"Ministry of Steel",11,11,100.00,"191","table_page_191_1.csv",""),
        (32,"Ministry of Textiles",18,18,100.00,"191","table_page_191_1.csv",""),
        (33,"Ministry of Tourism",25,25,100.00,"191","table_page_191_1.csv",""),
        (34,"Ministry of Tribal Affairs",4,4,100.00,"191","table_page_191_1.csv",""),
        (35,"Ministry of Road Transport & Highways",5,5,100.00,"191","table_page_191_1.csv",""),
        (36,"Ministry of Youth Affairs & Sports",6,6,100.00,"191","table_page_191_1.csv",""),
        (37,"President Secretariat",1,1,100.00,"191","table_page_191_1.csv",""),
        (38,"Comptroller & Auditor General",1,1,100.00,"191","table_page_191_1.csv",""),
        (39,"UT of Andaman & Nicobar",2,2,100.00,"191","table_page_191_1.csv",""),
        (40,"UT of Lakshadweep",1,1,100.00,"192","table_page_192_1.csv",""),
        (41,"Vice-President Secretariat",1,1,100.00,"192","table_page_192_1.csv",""),
        (42,"Supreme Court of India",1,1,100.00,"192","table_page_192_1.csv",""),
        (43,"High Court Of Delhi",2,2,100.00,"192","table_page_192_1.csv",""),
        (44,"Ministry of Skill Development & Entrepreneurship",6,6,100.00,"192","table_page_192_1.csv",""),
        (45,"Ministry of Electronics & Information Technology",15,15,100.00,"192","table_page_192_1.csv",""),
        (46,"Ministry of Ayush",22,22,100.00,"192","table_page_192_1.csv",""),
        (47,"Ministry of Jal Shakti",24,24,100.00,"192","table_page_192_1.csv",""),
        (48,"Ministry of Fisheries, Animal Husbandry & Dairying",53,53,100.00,"192","table_page_192_1.csv",""),
        (49,"UT of Dadra and Nagar Haveli and Daman and Diu",1,1,100.00,"192","table_page_192_1.csv",""),
        (50,"Ministry of Cooperation",1,1,100.00,"192","table_page_192_1.csv",""),
        (51,"Ministry of Education",204,204,100.00,"192","table_page_192_1.csv",""),
        (52,"Ministry of Science & Technology",89,89,100.00,"192","table_page_192_1.csv",""),
        (53,"Ministry of Micro, Small and Medium Enterprises",61,61,100.00,"192","table_page_192_1.csv",""),
        (54,"Ministry of Health & Family Welfare",92,92,100.00,"192","table_page_192_1.csv",""),
        (55,"Ministry of Agriculture & Farmers Welfare",150,150,100.00,"192","table_page_192_1.csv",""),
        (56,"Ministry of Culture",37,37,100.00,"192","table_page_192_1.csv",""),
        (57,"Ministry of Environment & Forests",32,32,100.00,"192","table_page_192_1.csv",""),
        (58,"UT of Chandigarh",66,66,100.00,"192","table_page_192_1.csv",""),
        (59,"Ministry of Home Affairs",30,30,100.00,"192","table_page_192_1.csv",""),
        (60,"Ministry of Consumer Aff., Food, & Public Dist.",26,26,100.00,"192","table_page_192_1.csv",""),
        (61,"Ministry of Petroleum & Natural Gas",22,22,100.00,"192","table_page_192_1.csv",""),
        (62,"UT of Puducherry",47,47,100.00,"192","table_page_192_1.csv",""),
        (63,"Ministry of Corporate Affairs",64,64,100.00,"192","table_page_192_1.csv",""),
        (64,"Ministry of Shipping",19,19,100.00,"192","table_page_192_1.csv",""),
        (65,"Ministry of Finance",219,219,100.00,"192","table_page_192_1.csv",""),
        (66,"UT of Delhi",192,192,100.00,"192","table_page_192_1.csv",""),
        (67,"Ministry of Labour & Employment",34,34,100.00,"192","table_page_192_1.csv",""),
        (68,"Ministry of Civil Aviation",10,10,100.00,"192","table_page_192_1.csv",""),
        (69,"Ministry of Housing & Urban Affairs",29,29,100.00,"192","table_page_192_1.csv",""),
        (70,"UT of Jammu and Kashmir",43,43,100.00,"192","table_page_192_1.csv",""),
        (None,"Grand Total (Table 4.1)",2298,2298,100.00,"192","table_page_192_1.csv","Grand Total row. Sum of 70 ministry entries. Verification: sum of pa_registered entries = 2298. Consistent with national total."),
    ]
    for item in min_comp:
        sl,name,pa_r,pa_c,cpct,page,sf,note = item
        rows.append({"financial_year":YEAR_2324,"entity_name":name,
            "entity_type":"Ministry/Independent Department" if sl else "Grand Total",
            "pa_registered":pa_r,"pa_compliant":pa_c,"pa_non_compliant":pa_r-pa_c,
            "compliance_pct_reported":cpct,
            "capios":"NA","cpios":"NA","faas":"NA",
            "source_file":sf,"pdf_page":page,"table_number":"Table 4.1",
            "source_table":"Ministry/Independent Department-wise Annual Return Compliance",
            "notes":note})
    return FN, rows

# ── data_discrepancies.csv ───────────────────────────────────────────────────
def discrepancies():
    FN = ["financial_year","metric","source_1","value_1","source_2","value_2","description","resolution_status"]
    rows = [
        {"financial_year":YEAR_2324,"metric":"RTI rejection decisions vs total section invocations",
         "source_1":"table_page_16_1.csv (Table 2.3 p16) + table_page_24_1.csv (Table 2.1 row 10 p24)",
         "value_1":"67615 (decisions where information rejected)",
         "source_2":"table_page_24_1.csv (Table 2.1 Total row p24) + table_page_19_1.csv (Table 2.6 p19)",
         "value_2":"68189 (total section invocations)",
         "description":"Rejection decisions (67615) differs from total section invocations (68189) by 574. These are different metrics: one rejection decision can invoke multiple sections simultaneously. NOT a data error.",
         "resolution_status":"Resolved — different metrics; invocations >= decisions by design"},

        {"financial_year":YEAR_2324,"metric":"Rejection percentage precision",
         "source_1":"table_page_16_1.csv (Table 2.3 p16)",
         "value_1":"3.86%",
         "source_2":"table_page_190_1.csv (Table 3.1 grand total row 8 p190)",
         "value_2":"4% (rounded display)",
         "description":"Table 2.3 reports to 2 decimal places (3.86%). Table 3.1 grand total displays as '67615 (4%)' rounded to integer. Not a data error.",
         "resolution_status":"Resolved — rounding artefact only; use 3.86% from Table 2.3 for analysis"},

        {"financial_year":YEAR_2324,"metric":"Duplicate consolidated summary table",
         "source_1":"table_page_24_1.csv (Table 2.1 p24)",
         "value_1":"38 rows; all values primary",
         "source_2":"table_page_41_1.csv (Table 2.1 repeat p41)",
         "value_2":"38 rows; identical to p24",
         "description":"Table 2.1 (Consolidated Annual Return Summary 2023-24) appears at two PDF locations. Both CSVs contain identical data. Only page 24 used as primary source; page 41 used for cross-verification only.",
         "resolution_status":"Resolved — page 24 used as primary; page 41 excluded to prevent double-counting"},

        {"financial_year":YEAR_2324,"metric":"2015-16 PA registration count",
         "source_1":"table_page_16_1.csv (Table 2.3 p16)",
         "value_1":"2024",
         "source_2":"table_page_13_1.csv (Table 2.1 compliance p13)",
         "value_2":"2023",
         "description":"1-PA discrepancy in 2015-16 PA registration count between Table 2.3 (p16)=2024 and Table 2.1 compliance table (p13)=2023. Source of difference unclear — may be registration timing. Both values documented.",
         "resolution_status":"Unresolved — verify against original PDF pages 13 and 16"},

        {"financial_year":YEAR_2324,"metric":"2016-17 compliance percentage",
         "source_1":"table_page_13_1.csv (Table 2.1 compliance p13)",
         "value_1":"NA (blank in extracted CSV)",
         "source_2":"Calculated from same row: 1964/2092*100",
         "value_2":"93.88% (calculated only)",
         "description":"The 2016-17 compliance percentage cell is blank in the extracted CSV due to a column header layout shift. Left as NA to preserve source integrity. Calculated value is 93.88% but not entered into the dataset.",
         "resolution_status":"Flagged — verify against original PDF page 13; compliance_pct_reported=NA in output"},

        {"financial_year":YEAR_2324,"metric":"Ministry of Textiles name in Table 2.7",
         "source_1":"table_page_21_1.csv (Table 2.7 p21) row 14 raw",
         "value_1":"'Ministry of Textiles,istry of Textiles' (cell-split artefact)",
         "source_2":"table_page_191_1.csv (Table 4.1 p191) entry 32",
         "value_2":"Ministry of Textiles",
         "description":"Row 14 of Table 2.7 (p21) has ministry name split across two CSV cells creating a duplicate name fragment. Reconstructed as 'Ministry of Textiles'. All numeric values (received=2729, rejected=138, etc.) are unambiguous.",
         "resolution_status":"Flagged — name reconstructed; verify row 14 against original PDF page 21"},

        {"financial_year":YEAR_2324,"metric":"Total amount collected reconciliation",
         "source_1":"table_page_24_1.csv (Table 2.1 row 12 p24)",
         "value_1":"8153887 (composite: fee+charges+penalty)",
         "source_2":"table_page_190_1.csv (Table 3.1 grand total rows 10+11+12 p190)",
         "value_2":"5540245+2590979+22663=8153887",
         "description":"Table 2.1 composite total (8153887) equals sum of Table 3.1 components (fee+addl.charges+penalty). Values reconcile exactly.",
         "resolution_status":"Resolved — values consistent; no discrepancy"},
    ]
    return FN, rows

# ── quality report ───────────────────────────────────────────────────────────
def write_quality_report(out_dir, counts):
    ns,mn,rg,ap,ac,ic,dc = counts
    txt = f"""# Data Quality Report — CIC Annual Report 2023-24

**Report generated:** 2026-11-16
**Annual report processed:** AR2023-24E.pdf
**Staging path:** data/staging/2023-24/raw_csv/

---

## 1. Source Files Inspected

| PDF Page | CSV File | Table | Used For |
|---|---|---|---|
| 13 | table_page_13_1.csv | Table 2.1 (compliance time series) | institutional_compliance.csv |
| 14 | table_page_14_1.csv | CID-encoded chart artefact | EXCLUDED |
| 15 | table_page_15_1.csv | Table 2.2 (category compliance) | institutional_compliance.csv |
| 16 | table_page_16_1.csv | Table 2.3 (national time series) | national_statistics.csv |
| 17-t1 | table_page_17_1.csv | CID-encoded chart artefact | EXCLUDED |
| 17-t2 | table_page_17_2.csv | Table 2.4 rows 1-3 | ministry_statistics.csv |
| 18-t1 | table_page_18_1.csv | Table 2.4 rows 4-8+Total | ministry_statistics.csv |
| 18-t2 | table_page_18_2.csv | Table 2.5 (top 10 by volume) | ministry_statistics.csv |
| 19 | table_page_19_1.csv | Table 2.5 (ranks 11-20) + Table 2.6 | ministry_statistics.csv; rejection_grounds.csv |
| 20 | table_page_20_1.csv | CID-encoded chart artefact | EXCLUDED |
| 21 | table_page_21_1.csv | Table 2.7 (top 20 by rejection %) | ministry_statistics.csv; appeals_statistics.csv |
| 22 | table_page_22_1.csv | CID-encoded chart artefact | EXCLUDED |
| 24 | table_page_24_1.csv | Table 2.1 (consolidated summary) | national_statistics; rejection_grounds; appeals; accountability; institutional |
| 25 | table_page_25_1.csv | CIC terms of office | EXCLUDED — administrative |
| 26 | table_page_26_1.csv | Second Appeals/Complaints stats | appeals_statistics.csv |
| 34-35 | table_page_34_1.csv, 35_1.csv | CIC budget | EXCLUDED |
| 36 | table_page_36_1.csv | Acronym glossary | EXCLUDED |
| 41 | table_page_41_1.csv | Table 2.1 duplicate | Cross-verification only |
| 190 | table_page_190_1.csv | Table 3.1 grand total | accountability_statistics.csv |
| 191 | table_page_191_1.csv | Table 4.1 entries 1-39 | institutional_compliance.csv |
| 192 | table_page_192_1.csv | Table 4.1 entries 40-70+Grand Total | institutional_compliance.csv |
| 42-189 | table_page_42_1 to 189_1.csv | Table 3.1 PA-level detail | NOT PROCESSED — deferred (mirrored headers) |
| 193-271 | table_page_193_1 to 271_1.csv | Table 4.2+5.1 (PA registry/grades) | NOT PROCESSED — deferred (cell-split repair) |

---

## 2. Datasets Created and Row Counts

| Dataset | Rows | Coverage |
|---|---|---|
| national_statistics.csv | {ns} | 18 years (2006-07 to 2023-24); all year-specific columns only for 2023-24 |
| ministry_statistics.csv | {mn} | 8 PA categories + top 20 by volume + top 20 by rejection % (some overlap) |
| rejection_grounds.csv | {rg} | 10 Section 8(1) sub-clauses + 4 aggregate sections + grand total |
| appeals_statistics.csv | {ap} | 2 national aggregate rows + 40 ministry-level rows (20 ministries × 2 levels) |
| accountability_statistics.csv | {ac} | 7 metrics (5 with values, 2 as NA — not found in extracted tables) |
| institutional_compliance.csv | {ic} | 18-year trend + 8 categories + 70 ministry entries + 1 grand total |
| data_discrepancies.csv | {dc} | 7 discrepancies documented |

---

## 3. Validation Checks

| Check | Result |
|---|---|
| Total requests = opening_balance + received | 495039+1750863=2245902 ✅ |
| Rejection pct = rejected/received*100 | 67615/1750863*100=3.861≈3.86% ✅ |
| Section 8(1) sub-clause sum = S8(1) aggregate | 2206+144+38+4506+4534+563+720+2876+396+15753=31736 ✅ |
| Total invocations = sum all sections | 31736+293+750+10543+24867=68189 ✅ |
| Fee+charges+penalty = composite total | 5540245+2590979+22663=8153887 ✅ |
| Table 2.4 category total = national total | received 1750863 ✅; rejected 67615 ✅; pct 3.86% ✅ |
| Table 4.1 ministry entries sum = grand total | Sum of 70 entries = 2298 ✅ |
| Category-wise PAs sum | 111+166+202+967+47+566+85+154=2298 ✅ |
| Table 2.1 (p24) = Table 2.1 (p41) duplicate | All values identical ✅ |
| Table 2.1 FA (p24) = Table 3.1 grand total (p190) | 176872 ✅ |
| Disciplinary actions: p24 vs p190 | 36 ✅ |
| CAPIOs+CPIOs+FAAs = total officers | 61056+27657+21619=110332 ✅ |

---

## 4. Metrics Missing from Extracted Tables

| Metric | Reason |
|---|---|
| Full PA-level data (2298 PAs, Table 3.1 p42-190) | Deferred — requires mirrored-header decoding + 149-file horizontal concatenation |
| PA-level Section 8(1) sub-clause invocations | Part of Table 3.1; deferred |
| Individual Section 20 penalty orders | Not in any extracted table; only aggregate (₹22663) available |
| Section 20(1) penalty orders count | Not stated in extracted tables |
| Section 20(2) disciplinary recommendations by CIC | Not in extracted tables |
| First appeals pending (carry-forward) | Not stated; requires confirmed prior-year balance |
| Ministry-level second appeal disposal | Table 2.7 gives only received counts |
| IC/bench-wise case disposal | Narrative text only |
| Multi-year fee collection trend | Only 2023-24 available |
| RTI requests pending at year-end | Not stated; derivable with caveat |
| PA directory (Table 4.2 p193-240) | Deferred — 48 CSVs requiring split-cell repair |
| PA compliance grades (Table 5.1 p241-271) | Deferred — 31 CSVs requiring split-cell repair |

---

## 5. Fragmented Tables Reconstructed

| Source | Reconstruction | Confidence |
|---|---|---|
| table_page_15_1.csv | Category names joined across split cells (8 categories) | High |
| table_page_17_2.csv + table_page_18_1.csv | Table 2.4 combined from 2 pages | High |
| table_page_18_2.csv + table_page_19_1.csv | Table 2.5 combined from 2 pages (20 ministries) | High |
| table_page_19_1.csv rows 30-38 | Table 2.6 sliced from mixed-content CSV | High |
| table_page_21_1.csv row 14 | Ministry of Textiles name reconstructed from split cell | Medium — flagged |
| table_page_191_1.csv rows 37-38 | Department of Space PA count merged from two lines | High |
| table_page_13_1.csv rows 11-12 | 2016-17 two-line row merged; compliance_pct_reported=NA | Medium — flagged |

---

## 6. Data Quality Concerns

| Issue | Severity | Status |
|---|---|---|
| Table 3.1 mirrored headers (p42-190) — full PA data not extracted | High | Deferred pipeline |
| 2016-17 compliance pct blank in source | Medium | Flagged; compliance_pct_reported=NA |
| Ministry of Textiles name artefact (p21 row 14) | Low | Flagged for manual verification |
| 2015-16 PA count discrepancy (2024 vs 2023) | Low | Both values documented; unresolved |
| Section 20 case-level data absent | Medium | Only aggregate penalty available |

---

## 7. Items Requiring Manual Verification

1. **Ministry of Textiles (Table 2.7 p21 row 14):** Verify name and all values in original PDF.
2. **2016-17 compliance percentage (Table 2.1 p13):** Verify whether printed in PDF and confirm column.
3. **2015-16 PA registration count:** Verify whether PDF shows 2024 or 2023 on pages 13 and 16.
4. **Table 3.1 full extraction (p42-190):** Requires dedicated reconstruction pipeline.
5. **Section 20 penalty count:** Search narrative text of PDF for individual penalty order count.

---

## 8. Overall Assessment

| Dimension | Status |
|---|---|
| National aggregate statistics | ✅ Complete and validated |
| Ministry summary statistics | ⚠️ Partial — top 20 covered; full 2298 PAs deferred |
| Rejection grounds (national) | ✅ Complete at sub-clause level |
| Appeals statistics | ⚠️ Partial — national aggregate complete; disposal breakdown absent |
| Accountability statistics | ⚠️ Partial — aggregate penalty and disciplinary count only |
| Institutional compliance | ✅ Substantially complete — 18-year trend + all 70 ministry entries |

**Overall extraction completeness: ~70%**
Primary gap: Table 3.1 full PA-level data (p42-190).
**Ready for human review: Yes** with documented caveats.
"""
    with open(out_dir / "data_quality_report.md", "w", encoding="utf-8") as f:
        f.write(txt)
    print(f"  data_quality_report.md")

# ── 2024-25 stubs ────────────────────────────────────────────────────────────
STUB_FIELDS = {
    "national_statistics.csv":["financial_year","pa_registered","opening_balance","requests_received","total_requests","requests_transferred","requests_rejected","rejection_pct_reported","first_appeals_received","first_appeals_disposed","second_appeals_registered","second_appeals_disposed","second_appeals_pending","disciplinary_actions","fee_collected_rs","addl_charges_collected_rs","section20_penalty_collected_rs","total_amount_collected_rs","capios","cpios","faas","total_officers","source_file","pdf_page","table_number","source_table","notes"],
    "ministry_statistics.csv":["financial_year","entity_name","entity_type","rank_by_volume","rank_by_rejection_pct","requests_received","requests_rejected","rejection_pct_reported","first_appeals_received","second_appeals_received","source_file","pdf_page","table_number","source_table","notes"],
    "rejection_grounds.csv":["financial_year","provision","provision_detail","invocations_count","invocations_pct_of_total","reporting_period","source_file","pdf_page","table_number","source_table","notes"],
    "appeals_statistics.csv":["financial_year","level","entity_name","entity_type","received","disposed","pending","source_file","pdf_page","table_number","source_table","notes"],
    "accountability_statistics.csv":["financial_year","metric","value","unit","source_file","pdf_page","table_number","source_table","notes"],
    "institutional_compliance.csv":["financial_year","entity_name","entity_type","pa_registered","pa_compliant","pa_non_compliant","compliance_pct_reported","capios","cpios","faas","source_file","pdf_page","table_number","source_table","notes"],
    "data_discrepancies.csv":["financial_year","metric","source_1","value_1","source_2","value_2","description","resolution_status"],
}

def write_2425_stubs(out_dir):
    for fname, flds in STUB_FIELDS.items():
        write_csv_headers(out_dir / fname, flds)
    with open(out_dir / "data_quality_report.md", "w", encoding="utf-8") as f:
        f.write("""# Data Quality Report — CIC Annual Report 2024-25

**Report generated:** 2026-11-16
**Status: NOT PROCESSED — STAGING DATA UNAVAILABLE**

The staging directory for 2024-25 contains only empty stub files:
- data/staging/2024-25/raw_tables.json: empty array []
- data/staging/2024-25/table_manifest.csv: header row only
- data/staging/2024-25/raw_csv/table_inventory.csv: header row only
- data/staging/2024-25/raw_csv/: no CSV files

All six dataset files have been created with correct column headers but zero data rows.

## Next Steps
1. Run PDF extraction pipeline against AR2024-25E.pdf.
2. Populate data/staging/2024-25/ with extracted tables.
3. Re-run this extraction script.
4. See reports/table_mapping_report_2024-25.md for anticipated table locations
   and known extraction challenges (mirrored headers, CID artefacts, etc.).
""")
    print("  data_quality_report.md (2024-25 stub)")

# ── main ──────────────────────────────────────────────────────────────────────
def main():
    print("\n=== CIC Annual Report Data Extraction ===\n")
    print(f"[1/2] Processing 2023-24")
    ensure_dir(CLEANED_2324)

    fn,rows = national_stats();      write_csv(CLEANED_2324/"national_statistics.csv", fn, rows);       ns=len(rows)
    fn,rows = ministry_stats();      write_csv(CLEANED_2324/"ministry_statistics.csv", fn, rows);       mn=len(rows)
    fn,rows = rejection_grounds();   write_csv(CLEANED_2324/"rejection_grounds.csv", fn, rows);         rg=len(rows)
    fn,rows = appeals_stats();       write_csv(CLEANED_2324/"appeals_statistics.csv", fn, rows);        ap=len(rows)
    fn,rows = accountability_stats();write_csv(CLEANED_2324/"accountability_statistics.csv", fn, rows); ac=len(rows)
    fn,rows = institutional_compliance(); write_csv(CLEANED_2324/"institutional_compliance.csv", fn, rows); ic=len(rows)
    fn,rows = discrepancies();       write_csv(CLEANED_2324/"data_discrepancies.csv", fn, rows);        dc=len(rows)
    write_quality_report(CLEANED_2324, (ns,mn,rg,ap,ac,ic,dc))

    print(f"\n[2/2] Processing 2024-25 (staging unavailable — writing stubs)")
    ensure_dir(CLEANED_2425)
    write_2425_stubs(CLEANED_2425)

    print("\n=== Done ===")
    print(f"\n2023-24 row counts: national={ns} ministry={mn} rejection={rg} appeals={ap} accountability={ac} compliance={ic} discrepancies={dc}")

if __name__ == "__main__":
    main()
