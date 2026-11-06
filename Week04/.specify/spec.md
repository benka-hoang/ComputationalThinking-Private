# Feature Specification: Keyword Expense Classifier & Budget Status Monitor

**Feature ID:** `FEAT-01-BUDGET-TRACKER`  
**System:** Smart Personal Finance Assistant (Group 4)  
**Author:** Hoang Thien Nhan (Student ID: 25125031)  
**Date:** November 2026  
**Status:** Approved for Implementation  

---

## 1. Problem Statement & Motivation

University students and young adults frequently spend money across multiple categories without real-time visibility into whether their spending is approaching or exceeding their monthly limits. 

This feature automates two critical stages defined in the system architecture:
1. **Stage B4 (Classify):** Automatically assigns raw transaction records to pre-defined categories and sub-categories using Vietnamese unaccented keyword matching.
2. **Stage C1 & C2 (Calculate & Evaluate):** Aggregates total monthly income and expenses, computes remaining balance and savings goal progress, and evaluates category-level budget statuses against fixed percentage thresholds (`OK`, `Warning`, `Over budget`).

---

## 2. Scope & Boundaries

### In Scope
- Categorization of normalized transactions into 6 fixed categories:
  - `Food` (Sub-categories: `Meals`, `Coffee`, `Delivery`)
  - `Transport`
  - `Education`
  - `Entertainment`
  - `Shopping`
  - `Other`
- Keyword dictionary matching with case-insensitivity and Vietnamese diacritic stripping.
- Calculation of:
  - Total Monthly Income
  - Total Monthly Expenses
  - Remaining Balance (`Total Income - Total Expenses`)
  - Savings Status (`Remaining Balance vs Monthly Savings Goal`)
  - Category Spending and Utilization Rate (`spent / limit * 100%`)
- Status determination rule:
  - `OK`: `spent / limit < 80%`
  - `Warning`: `80% <= spent / limit <= 100%`
  - `Over budget`: `spent / limit > 100%`
- Interactive visual interface built with Streamlit.

### Out of Scope (deferred to future phases)
- Image OCR and multimodal LLM vision parsing (Stage A / Phase 5).
- Bank API synchronization (users provide text/receipt evidence).
- Multi-currency conversions (VND only).

---

## 3. User Stories & Acceptance Criteria

### User Story 1: Keyword-based Categorization
> **As a** student managing monthly expenses,  
> **I want** my transactions to be categorized automatically based on merchant name or description keywords,  
> **So that** I do not have to manually tag each expense every day.

- **AC 1.1 (Exact and Substring Matching):** Given a transaction with merchant `"Highlands Coffee"`, when categorized, its category must be `"Food"` and its subcategory must be `"Coffee"`.
- **AC 1.2 (Unaccented Vietnamese Handling):** Given an expense note `"an trua can tin 35k"`, the system must normalize it to unaccented lowercase (`"an trua can tin 35k"`) and classify it under `"Food - Meals"`.
- **AC 1.3 (Fallback Category):** Given an unknown merchant (e.g. `"Tiem tap hoa Ba Ba"`), if no keyword matches, the category must fall back to `"Other"`.

---

### User Story 2: Monthly Summary & Savings Health
> **As a** user with a monthly savings target,  
> **I want** to see my total income, total expenses, net balance, and savings goal status,  
> **So that** I know immediately if I am on track to meet my financial goals.

- **AC 2.1 (Financial Totals):** Given the verified transactions of October 2026 with income of 3,000,000 VND and expenses of 2,200,000 VND, the net balance must calculate to exactly `800,000 VND`.
- **AC 2.2 (Savings Goal Achieved):** Given a savings target of `500,000 VND` and a balance of `800,000 VND`, the savings status must indicate `"Goal achieved"` with a surplus of `300,000 VND`.
- **AC 2.3 (Savings Goal Missed):** Given a savings target of `1,000,000 VND` and a balance of `800,000 VND`, the savings status must indicate `"Goal not met"` with a deficit of `200,000 VND`.

---

### User Story 3: Category Budget Status Warning
> **As a** budget-conscious individual,  
> **I want** visual alerts when any spending category reaches 80% or exceeds 100% of its budget,  
> **So that** I can halt non-essential spending before debt accumulates.

- **AC 3.1 (Warning Status at 80%):** Given category `Transport` with limit `300,000 VND` and spending of `240,000 VND` (80.0%), the status must be `"Warning"`.
- **AC 3.2 (Over Budget Status > 100%):** Given category `Food` with limit `1,000,000 VND` and spending of `1,200,000 VND` (120.0%), the status must be `"Over budget"` with overspent amount of `200,000 VND`.
- **AC 3.3 (OK Status < 80%):** Given category `Education` with limit `400,000 VND` and spending of `250,000 VND` (62.5%), the status must be `"OK"`.

---

## 4. Ground Truth Verification (October 2026 Test Case)

From Group 4 Project Report Section 2.4 & 2.5:

| Category | Spent (VND) | Limit (VND) | Percentage | Expected Status |
|---|---|---|---|---|
| Food | 1,200,000 | 1,000,000 | 120.0% | Over budget |
| Transport | 240,000 | 300,000 | 80.0% | Warning |
| Education | 250,000 | 400,000 | 62.5% | OK |
| Entertainment | 220,000 | 300,000 | 73.3% | OK |
| Shopping | 190,000 | 300,000 | 63.3% | OK |
| Other | 100,000 | 200,000 | 50.0% | OK |
| **Total Expenses** | **2,200,000** | **2,500,000** | **88.0%** | **Within Total Limit** |
