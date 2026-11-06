"""
app.py
Interactive Streamlit Dashboard for Smart Personal Finance Assistant.
Author: Hoang Thien Nhan (Student ID: 25125031)
Course: CSC10014 - Computational Thinking
Group 4 - Smart Personal Finance Assistant
"""

import streamlit as st
import pandas as pd
from tracker import (
    Transaction,
    TransactionType,
    BudgetStatus,
    classify_all,
    compute_monthly_summary,
    load_october_sample,
)

# Page configuration
st.set_page_config(
    page_title="Personal Finance Assistant - Budget Monitor",
    page_icon="💰",
    layout="wide",
)

# Custom Styling
st.markdown(
    """
    <style>
    .metric-card {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 15px;
        border-left: 5px solid #1f77b4;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .badge-ok {
        background-color: #d4edda;
        color: #155724;
        padding: 3px 10px;
        border-radius: 12px;
        font-weight: bold;
    }
    .badge-warning {
        background-color: #fff3cd;
        color: #856404;
        padding: 3px 10px;
        border-radius: 12px;
        font-weight: bold;
    }
    .badge-over {
        background-color: #f8d7da;
        color: #721c24;
        padding: 3px 10px;
        border-radius: 12px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header Banner
st.title("💰 Smart Personal Finance Assistant")
st.caption(
    "**Course:** CSC10014 - Computational Thinking | **Student:** Hoang Thien Nhan (25125031) | **Team:** Group 4"
)
st.write("---")

# Sidebar: Controls & Budget Configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    dataset_choice = st.selectbox(
        "Select Dataset:",
        ["October 2026 (Report Worked Example)", "Empty (Manual Entry)"],
    )

    st.subheader("Monthly Limits (VND)")
    limit_food = st.number_input("Food", value=1_000_000, step=50_000)
    limit_transport = st.number_input("Transport", value=300_000, step=50_000)
    limit_education = st.number_input("Education", value=400_000, step=50_000)
    limit_entertainment = st.number_input("Entertainment", value=300_000, step=50_000)
    limit_shopping = st.number_input("Shopping", value=300_000, step=50_000)
    limit_other = st.number_input("Other", value=200_000, step=50_000)

    savings_goal = st.number_input("Monthly Savings Goal", value=500_000, step=50_000)

limits = {
    "Food": int(limit_food),
    "Transport": int(limit_transport),
    "Education": int(limit_education),
    "Entertainment": int(limit_entertainment),
    "Shopping": int(limit_shopping),
    "Other": int(limit_other),
}

# Load & Process Data
if dataset_choice.startswith("October"):
    transactions, _, _ = load_october_sample()
else:
    transactions = []

# Classify transactions
classify_all(transactions)

# Compute Summary
summary = compute_monthly_summary(transactions, limits, int(savings_goal))

# KPI Metric Row
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(
        label="📥 Total Income",
        value=f"{summary.total_income:,.0f} ₫",
    )
with col2:
    st.metric(
        label="📤 Total Expenses",
        value=f"{summary.total_expenses:,.0f} ₫",
        delta=f"-{summary.total_expenses:,.0f} ₫",
        delta_color="inverse",
    )
with col3:
    st.metric(
        label="💵 Net Balance",
        value=f"{summary.net_balance:,.0f} ₫",
    )
with col4:
    if summary.is_goal_met:
        st.metric(
            label="🎯 Savings Target (500k ₫)",
            value="Goal Achieved",
            delta=f"+{summary.savings_delta:,.0f} ₫ surplus",
            delta_color="normal",
        )
    else:
        st.metric(
            label="🎯 Savings Target (500k ₫)",
            value="Goal Not Met",
            delta=f"-{abs(summary.savings_delta):,.0f} ₫ deficit",
            delta_color="inverse",
        )

st.write("---")

# Main Content Layout: Budget Health (Left) & Food Breakdown (Right)
left_col, right_col = st.columns([3, 2])

with left_col:
    st.subheader("📊 Category Budget Health")
    st.caption("Thresholds: 🟢 **OK** (<80%) | 🟡 **Warning** (80–100%) | 🔴 **Over budget** (>100%)")

    for cat_name, cat_eval in summary.categories.items():
        # Badge determination
        if cat_eval.status == BudgetStatus.OK:
            badge_html = f'<span class="badge-ok">OK ({cat_eval.percentage}%)</span>'
        elif cat_eval.status == BudgetStatus.WARNING:
            badge_html = f'<span class="badge-warning">⚠️ Warning ({cat_eval.percentage}%)</span>'
        else:
            badge_html = f'<span class="badge-over">🚨 Over budget ({cat_eval.percentage}%) +{cat_eval.overspend:,.0f} ₫</span>'

        col_a, col_b = st.columns([3, 2])
        with col_a:
            st.markdown(f"**{cat_name}**: {cat_eval.spent:,.0f} / {cat_eval.limit:,.0f} ₫")
        with col_b:
            st.markdown(badge_html, unsafe_allow_html=True)

        # Progress bar (clamped to 1.0 for Streamlit visual)
        progress_val = min(1.0, cat_eval.spent / cat_eval.limit if cat_eval.limit > 0 else 0.0)
        st.progress(progress_val)

with right_col:
    st.subheader("☕ Food Category Deep-Dive")
    if summary.food_breakdown:
        food_total = sum(summary.food_breakdown.values())
        if food_total > 0:
            df_food = pd.DataFrame(
                [
                    {
                        "Subcategory": k,
                        "Spent (VND)": v,
                        "Share": f"{(v / food_total)*100:.1f}%",
                    }
                    for k, v in summary.food_breakdown.items()
                ]
            )
            st.dataframe(df_food, use_container_width=True, hide_index=True)

            st.info(
                """
                💡 **Actionable Recommendation (from Proposal Report):**
                - **Coffee** accounts for **33.3%** (400,000 ₫).
                - Cutting from 8 cups to 4 cups saves **220,000 ₫**, which alone fully eliminates the **200,000 ₫ Food overspending**!
                """
            )
        else:
            st.write("No food expenses recorded.")

st.write("---")

# Transactions Table with Filter
st.subheader("🧾 Categorized Transactions (October 2026)")

filter_col1, filter_col2 = st.columns([2, 3])
with filter_col1:
    cat_filter = st.selectbox(
        "Filter by Category:",
        ["All"] + list(limits.keys()) + ["Income"],
    )
with filter_col2:
    search_query = st.text_input("🔍 Search Merchant / Note:", "")

filtered_tx = transactions
if cat_filter != "All":
    filtered_tx = [t for t in filtered_tx if t.category == cat_filter]

if search_query:
    q = search_query.lower()
    filtered_tx = [
        t for t in filtered_tx
        if q in t.merchant.lower() or q in t.desc.lower()
    ]

# Render Table
table_data = [
    {
        "ID": t.id,
        "Date": t.date,
        "Merchant / Note": t.merchant,
        "Description": t.desc,
        "Amount (VND)": f"{t.amount:,.0f}",
        "Type": t.type.value,
        "Category": t.category,
        "Subcategory": t.subcategory or "-",
        "Status": t.status,
    }
    for t in filtered_tx
]

if table_data:
    st.dataframe(pd.DataFrame(table_data), use_container_width=True, hide_index=True)
else:
    st.warning("No transactions match the selected filter.")
