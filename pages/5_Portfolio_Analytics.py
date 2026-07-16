import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Portfolio Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Portfolio Analytics Dashboard")
st.subheader("Infrastructure Investment Portfolio Overview")

# --------------------
# Load Dataset
# --------------------

df = pd.read_csv("data/infrastructure_projects.csv")

# --------------------
# KPIs
# --------------------

total_projects = len(df)

total_investment = df["Project_Cost_Million_USD"].sum()

average_debt = df["Debt_Ratio"].mean()

average_interest = df["Interest_Rate"].mean()

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Total Projects",
        total_projects
    )

    st.metric(
        "Average Debt Ratio",
        f"{average_debt:.2f}"
    )

with col2:

    st.metric(
        "Total Investment",
        f"${total_investment:,.0f} M"
    )

    st.metric(
        "Average Interest Rate",
        f"{average_interest:.2f}%"
    )

st.divider()
st.subheader("💰 Investment by Sector")

sector_investment = df.groupby("Sector")["Project_Cost_Million_USD"].sum().reset_index()

fig1 = px.bar(
    sector_investment,
    x="Sector",
    y="Project_Cost_Million_USD",
    color="Sector",
    title="Infrastructure Investment by Sector"
)

st.plotly_chart(fig1, use_container_width=True)
st.divider()

st.subheader("🚨 Risk Distribution")

fig2 = px.pie(
    df,
    names="Risk_Level",
    title="Portfolio Risk Distribution",
    color="Risk_Level",
    color_discrete_map={
        "Low": "green",
        "Medium": "orange",
        "High": "red"
    }
)

st.plotly_chart(fig2, use_container_width=True)
st.divider()

st.subheader("🌍 Projects by Country")

country_projects = df.groupby("Country").size().reset_index(name="Projects")

fig3 = px.bar(
    country_projects,
    x="Country",
    y="Projects",
    color="Country",
    title="Projects by Country"
)

st.plotly_chart(fig3, use_container_width=True)
st.divider()

st.subheader("📈 Debt Ratio Analysis")

fig4 = px.box(
    df,
    y="Debt_Ratio",
    color="Risk_Level",
    title="Debt Ratio Distribution"
)

st.plotly_chart(fig4, use_container_width=True)
st.divider()

st.subheader("🏦 Interest Rate Comparison")

fig5 = px.bar(
    df,
    x="Project_Name",
    y="Interest_Rate",
    color="Risk_Level",
    title="Interest Rate by Project"
)

st.plotly_chart(fig5, use_container_width=True)
st.divider()

st.subheader("🤖 Executive Portfolio Insights")

high_risk = len(df[df["Risk_Level"] == "High"])
low_risk = len(df[df["Risk_Level"] == "Low"])

if high_risk >= 3:
    st.error("""
### Portfolio Assessment

- High-risk projects require immediate review.
- Diversify investments across sectors.
- Closely monitor debt and construction delays.
- Reassess financing strategies for high-risk projects.
""")
else:
    st.success("""
### Portfolio Assessment

- Portfolio is well balanced.
- Financial risk is under control.
- Continue monitoring key financial indicators.
- Maintain investment discipline.
""")