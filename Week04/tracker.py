"""
tracker.py
Core Algorithmic Engine for Smart Personal Finance Assistant.
Implements:
- Vietnamese Diacritic Stripping & Normalization
- Keyword Dictionary Classification (Stage B4)
- Monthly Income/Expense/Savings Aggregation (Stage C1)
- Category-level Budget Threshold Evaluation (Stage C2)
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, List, Dict, Tuple
import unicodedata


class TransactionType(str, Enum):
    INCOME = "Income"
    EXPENSE = "Expense"
    TRANSFER = "Transfer"
    UNKNOWN = "Unknown"


class BudgetStatus(str, Enum):
    OK = "OK"
    WARNING = "Warning"
    OVER_BUDGET = "Over budget"


@dataclass
class Transaction:
    id: str
    date: str
    merchant: str
    amount: int                         # Positive VND integer
    type: TransactionType = TransactionType.EXPENSE
    category: str = "Other"
    subcategory: Optional[str] = None
    desc: str = ""
    status: str = "Confirmed"


@dataclass
class CategoryEvaluation:
    category: str
    spent: int
    limit: int
    percentage: float                   # e.g., 120.0 for 120%
    status: BudgetStatus
    overspend: int = 0                  # max(0, spent - limit)


@dataclass
class MonthlyFinancialSummary:
    total_income: int
    total_expenses: int
    net_balance: int
    savings_goal: int
    is_goal_met: bool
    savings_delta: int                  # net_balance - savings_goal
    categories: Dict[str, CategoryEvaluation] = field(default_factory=dict)
    food_breakdown: Dict[str, int] = field(default_factory=dict)


def strip_accents(text: str) -> str:
    """
    Remove Vietnamese diacritics and convert text to lowercase ASCII.
    Example: 'Phúc Long - Ăn trưa' -> 'phuc long - an trua'
    """
    if not text:
        return ""
    # Normalize unicode to decomposed form
    normalized = unicodedata.normalize("NFD", text)
    stripped = "".join(
        c for c in normalized if unicodedata.category(c) != "Mn"
    )
    # Replace 'đ' and 'Đ'
    stripped = stripped.replace("đ", "d").replace("Đ", "d")
    return stripped.lower()


# Keyword Dictionary based on Section 3.2 of Group 4 Report
# Format: (Category, Subcategory, Tuple of keywords)
KEYWORD_RULES: List[Tuple[str, Optional[str], Tuple[str, ...]]] = [
    # Food sub-categories
    ("Food", "Coffee", ("highlands", "phuc long", "cafe", "coffee", "tra sua")),
    ("Food", "Delivery", ("grabfood", "shopeefood", "baemin")),
    ("Food", "Meals", ("an trua", "an toi", "com", "can tin", "pho")),
    # Other primary categories
    ("Transport", None, ("petrolimex", "xang", "grab bike", "xe buyt")),
    ("Education", None, ("fahasa", "sach", "hoc phi", "khoa hoc")),
    ("Entertainment", None, ("cgv", "lotte cinema", "netflix", "game")),
    ("Shopping", None, ("shopee", "lazada", "tiki")),
    ("Other", None, ("viettel", "mobifone", "nap the", "dien", "nuoc")),
]


def classify_transaction(t: Transaction) -> Transaction:
    """
    Classifies a transaction into a category and subcategory based on its
    merchant name and description.
    """
    if t.type == TransactionType.INCOME:
        t.category = "Income"
        t.subcategory = None
        return t

    combined_text = strip_accents(f"{t.merchant} {t.desc}")

    for category, subcategory, keywords in KEYWORD_RULES:
        for kw in keywords:
            if kw in combined_text:
                t.category = category
                t.subcategory = subcategory
                return t

    # Fallback to Other
    t.category = "Other"
    t.subcategory = None
    return t


def classify_all(transactions: List[Transaction]) -> List[Transaction]:
    """Classifies a list of transactions in-place and returns it."""
    for t in transactions:
        classify_transaction(t)
    return transactions


def evaluate_category_budget(spent: int, limit: int, category: str) -> CategoryEvaluation:
    """
    Evaluates spending in a category against its limit.
    Thresholds:
    - spent < 80% limit -> OK
    - 80% <= spent <= 100% limit -> Warning
    - spent > 100% limit -> Over budget
    """
    if limit <= 0:
        pct = 100.0 if spent > 0 else 0.0
        status = BudgetStatus.OVER_BUDGET if spent > 0 else BudgetStatus.OK
        overspend = spent
    else:
        raw_ratio = spent / limit
        pct = round(raw_ratio * 100.0, 1)
        if raw_ratio < 0.80:
            status = BudgetStatus.OK
        elif raw_ratio <= 1.00:
            status = BudgetStatus.WARNING
        else:
            status = BudgetStatus.OVER_BUDGET
        overspend = max(0, spent - limit)

    return CategoryEvaluation(
        category=category,
        spent=spent,
        limit=limit,
        percentage=pct,
        status=status,
        overspend=overspend,
    )


def compute_monthly_summary(
    transactions: List[Transaction],
    limits: Dict[str, int],
    savings_goal: int,
) -> MonthlyFinancialSummary:
    """
    Aggregates income and expenses, compares spending against limits,
    and returns a MonthlyFinancialSummary.
    """
    total_income = 0
    total_expenses = 0
    category_spending: Dict[str, int] = {cat: 0 for cat in limits.keys()}
    food_breakdown: Dict[str, int] = {"Meals": 0, "Coffee": 0, "Delivery": 0}

    for t in transactions:
        if t.type == TransactionType.INCOME:
            total_income += t.amount
        elif t.type == TransactionType.EXPENSE:
            total_expenses += t.amount
            cat = t.category if t.category in category_spending else "Other"
            category_spending[cat] += t.amount

            if t.category == "Food" and t.subcategory in food_breakdown:
                food_breakdown[t.subcategory] += t.amount

    net_balance = total_income - total_expenses
    is_goal_met = net_balance >= savings_goal
    savings_delta = net_balance - savings_goal

    categories_eval: Dict[str, CategoryEvaluation] = {}
    for cat, limit in limits.items():
        spent = category_spending.get(cat, 0)
        categories_eval[cat] = evaluate_category_budget(spent, limit, cat)

    return MonthlyFinancialSummary(
        total_income=total_income,
        total_expenses=total_expenses,
        net_balance=net_balance,
        savings_goal=savings_goal,
        is_goal_met=is_goal_met,
        savings_delta=savings_delta,
        categories=categories_eval,
        food_breakdown=food_breakdown,
    )


def load_october_sample() -> Tuple[List[Transaction], Dict[str, int], int]:
    """Utility loader for October 2026 data."""
    from sample_data import (
        RAW_OCTOBER_TRANSACTIONS,
        OCTOBER_BUDGET_LIMITS,
        OCTOBER_SAVINGS_GOAL,
    )

    transactions = [
        Transaction(
            id=raw["id"],
            date=raw["date"],
            merchant=raw["merchant"],
            amount=raw["amount"],
            type=TransactionType(raw["type"]),
            desc=raw.get("desc", ""),
        )
        for raw in RAW_OCTOBER_TRANSACTIONS
    ]
    return transactions, OCTOBER_BUDGET_LIMITS, OCTOBER_SAVINGS_GOAL
