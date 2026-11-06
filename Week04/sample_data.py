"""
sample_data.py
Ground-truth transaction and budget dataset for October 2026.
Extracted from Group 4 Project Proposal Report (Sections 2.4 & 2.5).
"""

from typing import List, Dict

OCTOBER_BUDGET_LIMITS: Dict[str, int] = {
    "Food": 1_000_000,
    "Transport": 300_000,
    "Education": 400_000,
    "Entertainment": 300_000,
    "Shopping": 300_000,
    "Other": 200_000,
}

OCTOBER_SAVINGS_GOAL: int = 500_000

# Raw transactions before classification
# Each item represents a normalized transaction extracted from raw financial evidence
RAW_OCTOBER_TRANSACTIONS: List[dict] = [
    # T01: Income
    {
        "id": "T01",
        "date": "01/10/2026",
        "merchant": "Me gui tien thang 10",
        "desc": "VCB: TK 0123xxx +3,000,000VND luc 08:30 01/10/2026. ND: Me gui tien thang 10",
        "amount": 3_000_000,
        "type": "Income",
    },
    # T02: Merged Highlands Coffee receipt + VCB message
    {
        "id": "T02",
        "date": "05/10/2026",
        "merchant": "Highlands Coffee",
        "desc": "Phin Sua Da Highlands Coffee",
        "amount": 45_000,
        "type": "Expense",
    },
    # T03-T07: Highlands Coffee x5 (45,000 each = 225,000)
    {
        "id": "T03",
        "date": "06/10/2026",
        "merchant": "Highlands Coffee",
        "desc": "Phin Sua Da Highlands",
        "amount": 45_000,
        "type": "Expense",
    },
    {
        "id": "T04",
        "date": "10/10/2026",
        "merchant": "Highlands Coffee",
        "desc": "Freeze Tra Xanh",
        "amount": 45_000,
        "type": "Expense",
    },
    {
        "id": "T05",
        "date": "15/10/2026",
        "merchant": "Highlands Coffee",
        "desc": "Phin Den Da Highlands",
        "amount": 45_000,
        "type": "Expense",
    },
    {
        "id": "T06",
        "date": "19/10/2026",
        "merchant": "Highlands Coffee",
        "desc": "Tra Sen Vang",
        "amount": 45_000,
        "type": "Expense",
    },
    {
        "id": "T07",
        "date": "24/10/2026",
        "merchant": "Highlands Coffee",
        "desc": "Phin Sua Da",
        "amount": 45_000,
        "type": "Expense",
    },
    # T08-T09: Phuc Long x2 (65,000 each = 130,000)
    {
        "id": "T08",
        "date": "11/10/2026",
        "merchant": "Phuc Long",
        "desc": "Tra Oolong Phuc Long",
        "amount": 65_000,
        "type": "Expense",
    },
    {
        "id": "T09",
        "date": "25/10/2026",
        "merchant": "Phuc Long",
        "desc": "Tra Dao Phuc Long",
        "amount": 65_000,
        "type": "Expense",
    },
    # T10: Lunch transfer
    {
        "id": "T10",
        "date": "08/10/2026",
        "merchant": "chuyen tien an trua",
        "desc": "VCB: Account 0123xxx -80,000VND Desc: chuyen tien an trua",
        "amount": 80_000,
        "type": "Expense",
    },
    # T11-T20: Canteen lunch x10 (35,000 each = 350,000)
    *[
        {
            "id": f"T{i:02d}",
            "date": f"{min(i, 31):02d}/10/2026",
            "merchant": "can tin",
            "desc": "an trua can tin 35k",
            "amount": 35_000,
            "type": "Expense",
        }
        for i in range(11, 21)
    ],
    # T21-T22: GrabFood x2 (185,000 each = 370,000)
    {
        "id": "T21",
        "date": "14/10/2026",
        "merchant": "GrabFood",
        "desc": "GrabFood order com tam",
        "amount": 185_000,
        "type": "Expense",
    },
    {
        "id": "T22",
        "date": "27/10/2026",
        "merchant": "GrabFood",
        "desc": "GrabFood bun bo hue",
        "amount": 185_000,
        "type": "Expense",
    },
    # T23-T26: Petrolimex (petrol) x4 (60,000 each = 240,000)
    {
        "id": "T23",
        "date": "02/10/2026",
        "merchant": "Petrolimex",
        "desc": "Do xang Petrolimex",
        "amount": 60_000,
        "type": "Expense",
    },
    {
        "id": "T24",
        "date": "10/10/2026",
        "merchant": "Petrolimex",
        "desc": "Do xang xe may",
        "amount": 60_000,
        "type": "Expense",
    },
    {
        "id": "T25",
        "date": "18/10/2026",
        "merchant": "Petrolimex",
        "desc": "Petrolimex cay xang so 3",
        "amount": 60_000,
        "type": "Expense",
    },
    {
        "id": "T26",
        "date": "30/10/2026",
        "merchant": "Petrolimex",
        "desc": "Do xang cuoi thang",
        "amount": 60_000,
        "type": "Expense",
    },
    # T27: Fahasa textbook
    {
        "id": "T27",
        "date": "07/10/2026",
        "merchant": "Fahasa",
        "desc": "Nha sach Fahasa giao trinh dai so",
        "amount": 250_000,
        "type": "Expense",
    },
    # T28: CGV cinema
    {
        "id": "T28",
        "date": "18/10/2026",
        "merchant": "CGV",
        "desc": "CGV 2 ve xem phim",
        "amount": 220_000,
        "type": "Expense",
    },
    # T29: Shopee
    {
        "id": "T29",
        "date": "20/10/2026",
        "merchant": "Shopee",
        "desc": "Shopee don hang phu kien",
        "amount": 190_000,
        "type": "Expense",
    },
    # T30: Viettel mobile top-up
    {
        "id": "T30",
        "date": "03/10/2026",
        "merchant": "Viettel",
        "desc": "Viettel nap the dien thoai 100k",
        "amount": 100_000,
        "type": "Expense",
    },
]
