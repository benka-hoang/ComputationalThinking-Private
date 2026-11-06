# AI Usage Declaration - Lab 04

## 1. Student Information
- **Full Name:** Hoang Thien Nhan
- **Student ID:** 25125031
- **Course:** CSC10014 - Computational Thinking
- **Semester:** Semester 4
- **Lab Assignment:** Lab 04 - From Spec to Code: Phased Vibe-coding with AI

---

## 2. Summary of AI Usage
- **Primary AI Tool:** Google Antigravity AI Coding Assistant (Gemini 3.8 Flash).
- **Development Methodology:** Spec-Driven Vibe-coding using Spec Kit standards (Specification $\to$ Architecture & Mermaid Plan $\to$ Task Breakdown $\to$ Implementation $\to$ Testing $\to$ UI).
- **Student Oversight:** Directed system boundary definitions, verified domain rules against the Group 4 Proposal Report, manually audited the threshold comparison logic for edge cases (fixing rounding issues on boundary values), and verified test assertions.

---

## 3. Detailed AI Interaction Log by Phase

### Phase 1: Feature Selection & Specification (`spec.md`)
- **Prompts:**
  - *"im prepare to do my homework assignment in Lab04... pick for me an easy feature to prepare to vibecode. How can I apply Spec Kit & a Artifacts in this feature?"*
  - *"tạo bộ khung ik"*
- **Assistance Received:**
  - Recommended the core engine (Keyword Expense Classifier & Budget Status Monitor) combining Stage B4 and Stage C with a Streamlit interface.
  - Drafted the formal specification (`spec.md`) including User Stories in Gherkin syntax and acceptance criteria.

### Phase 2: Technical Planning & Design Artifacts (`plan.md`)
- **Prompts:**
  - Designed component architecture, data contracts (`dataclasses`), and boundary edge-case handling.
  - Generated 4 Mermaid diagrams: Activity Diagram, Sequence Diagram, State Machine Diagram, and Class Diagram.
- **Assistance Received:**
  - Validated syntax of Mermaid diagrams.
  - Structured data models for `Transaction`, `CategoryEvaluation`, and `MonthlyFinancialSummary`.

### Phase 3: Task Breakdown (`tasks.md`)
- **Assistance Received:**
  - Formulated a 6-phase decomposed checklist with clear git commit checkpoints to adhere to the phased vibe-coding methodology.

### Phase 4: Core Implementation & Bug Fix (`tracker.py`, `test_tracker.py`)
- **Assistance Received:**
  - Implemented diacritic stripping function (`strip_accents`) using Python's `unicodedata`.
  - Implemented the keyword dictionary matching and monthly aggregator.
  - Drafted unit test suite testing individual cases and October ground-truth trace.
  - **Debugging Assistance:** Caught boundary bug where `round((spent / limit) * 100.0, 1)` rounded `100.0001%` down to `100.0%`, misclassifying `1,000,001 VND` as `Warning` instead of `Over budget`. Fixed by comparing raw ratio before formatting.

### Phase 5: Streamlit Interactive Dashboard (`app.py`)
- **Assistance Received:**
  - Implemented clean Streamlit dashboard with KPI cards, color-coded badges, progress bars, and reactive transaction filtering.
