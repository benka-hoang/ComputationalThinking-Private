"""
test_tracker.py
Unit tests verifying the Expense Classifier & Budget Status Monitor
against the October 2026 Ground Truth from Group 4 Proposal Report.
"""

import unittest
from tracker import (
    Transaction,
    TransactionType,
    BudgetStatus,
    strip_accents,
    classify_transaction,
    classify_all,
    evaluate_category_budget,
    compute_monthly_summary,
    load_october_sample,
)


class TestTrackerEngine(unittest.TestCase):

    def test_strip_accents(self):
        """Verify Vietnamese diacritic removal and case normalization."""
        self.assertEqual(strip_accents("Phúc Long Coffee"), "phuc long coffee")
        self.assertEqual(strip_accents("Ăn trưa căng tin 35k"), "an trua cang tin 35k")
        self.assertEqual(strip_accents("Đổ xăng Petrolimex"), "do xang petrolimex")
        self.assertEqual(strip_accents("Học phí ĐHQG"), "hoc phi dhqg")

    def test_classify_individual_merchants(self):
        """Verify keyword classification into categories and subcategories."""
        cases = [
            ("Highlands Coffee", "Phin Sua Da", "Food", "Coffee"),
            ("Phuc Long", "Tra Dao", "Food", "Coffee"),
            ("GrabFood", "Com ga xoi mo", "Food", "Delivery"),
            ("can tin", "an trua can tin 35k", "Food", "Meals"),
            ("Petrolimex", "Do xang xe may", "Transport", None),
            ("Fahasa", "Sach lap trinh Python", "Education", None),
            ("CGV", "2 ve xem phim", "Entertainment", None),
            ("Shopee", "Don hang op lung", "Shopping", None),
            ("Viettel", "Nap the 100k", "Other", None),
            ("Tiem Banh Mi Co Ba", "Banh mi pate", "Other", None),  # Fallback
        ]
        for idx, (merchant, desc, expected_cat, expected_sub) in enumerate(cases):
            t = Transaction(id=f"TEST_{idx}", date="01/10/2026", merchant=merchant, amount=50_000, desc=desc)
            classify_transaction(t)
            self.assertEqual(t.category, expected_cat, f"Failed category for {merchant}")
            self.assertEqual(t.subcategory, expected_sub, f"Failed subcategory for {merchant}")

    def test_budget_status_thresholds(self):
        """Verify the 80% and 100% boundary rules."""
        limit = 1_000_000

        # < 80% -> OK
        eval_ok = evaluate_category_budget(799_000, limit, "Food")
        self.assertEqual(eval_ok.status, BudgetStatus.OK)
        self.assertEqual(eval_ok.overspend, 0)

        # Exactly 80% -> Warning
        eval_warn_80 = evaluate_category_budget(800_000, limit, "Food")
        self.assertEqual(eval_warn_80.status, BudgetStatus.WARNING)
        self.assertEqual(eval_warn_80.overspend, 0)

        # Exactly 100% -> Warning
        eval_warn_100 = evaluate_category_budget(1_000_000, limit, "Food")
        self.assertEqual(eval_warn_100.status, BudgetStatus.WARNING)
        self.assertEqual(eval_warn_100.overspend, 0)

        # > 100% -> Over budget
        eval_over = evaluate_category_budget(1_000_001, limit, "Food")
        self.assertEqual(eval_over.status, BudgetStatus.OVER_BUDGET)
        self.assertEqual(eval_over.overspend, 1)

    def test_october_ground_truth_full_pipeline(self):
        """
        Verify the complete October 2026 worked example from Report Section 2.5.
        - Total income: 3,000,000 VND
        - Total expenses: 2,200,000 VND
        - Net balance: 800,000 VND
        - Savings goal: 500,000 VND -> Met, surplus 300,000 VND
        - Food: 1,200,000 VND (120%) -> Over budget by 200,000 VND
          * Meals: 430,000 VND
          * Coffee: 400,000 VND
          * Delivery: 370,000 VND
        - Transport: 240,000 VND (80%) -> Warning
        - Education: 250,000 VND (62.5%) -> OK
        - Entertainment: 220,000 VND (73.3%) -> OK
        - Shopping: 190,000 VND (63.3%) -> OK
        - Other: 100,000 VND (50.0%) -> OK
        """
        transactions, limits, savings_goal = load_october_sample()
        classify_all(transactions)
        summary = compute_monthly_summary(transactions, limits, savings_goal)

        # Overall financial summary
        self.assertEqual(summary.total_income, 3_000_000)
        self.assertEqual(summary.total_expenses, 2_200_000)
        self.assertEqual(summary.net_balance, 800_000)
        self.assertTrue(summary.is_goal_met)
        self.assertEqual(summary.savings_delta, 300_000)

        # Category statuses
        food = summary.categories["Food"]
        self.assertEqual(food.spent, 1_200_000)
        self.assertEqual(food.limit, 1_000_000)
        self.assertEqual(food.percentage, 120.0)
        self.assertEqual(food.status, BudgetStatus.OVER_BUDGET)
        self.assertEqual(food.overspend, 200_000)

        # Food breakdown
        self.assertEqual(summary.food_breakdown["Meals"], 430_000)
        self.assertEqual(summary.food_breakdown["Coffee"], 400_000)
        self.assertEqual(summary.food_breakdown["Delivery"], 370_000)

        transport = summary.categories["Transport"]
        self.assertEqual(transport.spent, 240_000)
        self.assertEqual(transport.limit, 300_000)
        self.assertEqual(transport.percentage, 80.0)
        self.assertEqual(transport.status, BudgetStatus.WARNING)

        education = summary.categories["Education"]
        self.assertEqual(education.spent, 250_000)
        self.assertEqual(education.status, BudgetStatus.OK)

        entertainment = summary.categories["Entertainment"]
        self.assertEqual(entertainment.spent, 220_000)
        self.assertEqual(entertainment.status, BudgetStatus.OK)

        shopping = summary.categories["Shopping"]
        self.assertEqual(shopping.spent, 190_000)
        self.assertEqual(shopping.status, BudgetStatus.OK)

        other = summary.categories["Other"]
        self.assertEqual(other.spent, 100_000)
        self.assertEqual(other.status, BudgetStatus.OK)


if __name__ == "__main__":
    unittest.main()
