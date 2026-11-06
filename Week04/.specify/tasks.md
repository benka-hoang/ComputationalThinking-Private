# Implementation Tasks: Keyword Expense Classifier & Budget Status Monitor

**Feature ID:** `FEAT-01-BUDGET-TRACKER`  
**Approach:** Spec-Driven Vibe-Coding (Phased Execution)  
**Verification Target:** October 2026 Ground Truth from Group 4 Proposal Report  

---

## Phase 1: Setup, Data Models & Ground Truth Data
- [ ] **Task 1.1:** Create data model definitions in `tracker.py` (`Transaction`, `TransactionType`, `BudgetStatus`, `CategoryEvaluation`, `MonthlyFinancialSummary`).
- [ ] **Task 1.2:** Implement ground-truth dataset in `sample_data.py` containing the verified October 2026 records and budget limits.
- [ ] **Checkpoint 1.1:** Verify models load correctly without import errors.
- [ ] **Git Commit:** `git commit -m "feat(phase-1): define data models and October 2026 ground-truth dataset"`

---

## Phase 2: Vietnamese Text Normalization & Keyword Classifier
- [ ] **Task 2.1:** Implement string normalization helper `strip_accents(text: str) -> str` using `unicodedata`.
- [ ] **Task 2.2:** Build `KEYWORD_RULES` dictionary mapping categories and sub-categories to unaccented keyword lists.
- [ ] **Task 2.3:** Implement `classify_transaction(t: Transaction) -> Transaction` matching merchant and description against dictionary rules.
- [ ] **Task 2.4:** Implement batch classifier `classify_all(transactions: List[Transaction]) -> List[Transaction]`.
- [ ] **Checkpoint 2.1:** Run unit check on Highlands Coffee ("Food", "Coffee"), GrabFood ("Food", "Delivery"), Petrolimex ("Transport").
- [ ] **Git Commit:** `git commit -m "feat(phase-2): implement Vietnamese text normalization and keyword classifier"`

---

## Phase 3: Budget Status & Financial Summary Engine
- [ ] **Task 3.1:** Implement `evaluate_category_budget(spent: int, limit: int, category: str) -> CategoryEvaluation` implementing the threshold logic:
  - `< 80%` $\to$ `OK`
  - `80% - 100%` $\to$ `Warning`
  - `> 100%` $\to$ `Over budget`
- [ ] **Task 3.2:** Implement `compute_monthly_summary(transactions: List[Transaction], limits: Dict[str, int], savings_goal: int) -> MonthlyFinancialSummary`:
  - Calculate `total_income`, `total_expenses`, `net_balance`.
  - Calculate `is_goal_met` and `savings_delta`.
  - Generate category evaluations for all 6 categories.
- [ ] **Checkpoint 3.1:** Verify totals match October 2026: Income = 3,000,000, Expense = 2,200,000, Balance = 800,000.
- [ ] **Git Commit:** `git commit -m "feat(phase-3): implement budget evaluation and monthly summary calculation"`

---

## Phase 4: Automated Testing & Verification
- [ ] **Task 4.1:** Write test suite `test_tracker.py` using `unittest` or `pytest`:
  - Test individual keyword categorization.
  - Test edge cases (unaccented, uppercase, unknown merchant).
  - Test budget threshold boundary values (79.9%, 80.0%, 100.0%, 100.1%).
  - Test end-to-end October 2026 dataset against all expected numbers from Report Section 2.5.
- [ ] **Checkpoint 4.1:** Run `python -m unittest test_tracker.py` and ensure all tests pass (0 failures).
- [ ] **Git Commit:** `git commit -m "test(phase-4): add comprehensive test suite for October ground truth"`

---

## Phase 5: Streamlit Interactive UI
- [ ] **Task 5.1:** Build `app.py` Streamlit frontend:
  - Header & student metadata banner.
  - KPI Summary Cards: Total Income, Total Expenses, Balance, Savings Target Status.
  - Budget Health section: Category progress bars with color badges (Green/Yellow/Red).
  - Food Breakdown sub-chart (Meals vs Coffee vs Delivery).
  - Interactive transaction table with filtering by category and status.
- [ ] **Checkpoint 5.1:** Launch `streamlit run app.py` locally and verify visual fidelity.
- [ ] **Task 5.2:** Take screenshots of the running dashboard and save to `screenshots/`.
- [ ] **Git Commit:** `git commit -m "feat(phase-5): build Streamlit interactive dashboard and capture screenshots"`

---

## Phase 6: Submission Documentation
- [ ] **Task 6.1:** Fill in `README.md` (Development Report) detailing the Spec Kit process, artifacts, screenshots, and test results.
- [ ] **Task 6.2:** Fill in `AI_DECLARATION.md` detailing all AI tools and prompts used.
- [ ] **Task 6.3:** Generate `Git Commit Log.md` from `git log`.
- [ ] **Git Commit:** `git commit -m "docs(phase-6): finalize lab report, AI declaration, and git commit logs"`
