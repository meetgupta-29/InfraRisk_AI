import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Executive Dashboard",
    page_icon="🏢",
    layout="wide"
)

st.title("🏢 Executive Infrastructure Dashboard")
st.subheader("InfraRisk AI - Executive Overview")

# Load Dataset
df = pd.read_csv("data/infrastructure_projects.csv")

# KPI Cards

total_projects = len(df)
investment = df["Project_Cost_Million_USD"].sum()
high_risk = len(df[df["Risk_Level"]=="High"])
avg_debt = df["Debt_Ratio"].mean()

c1,c2,c3,c4 = st.columns(4)

c1.metric("Projects", total_projects)
c2.metric("Investment", f"${investment:,.0f} M")
c3.metric("High Risk", high_risk)
c4.metric("Avg Debt Ratio", f"{avg_debt:.2f}")

st.divider()

# Charts

left,right = st.columns(2)

with left:

    fig1 = px.pie(
        df,
        names="Risk_Level",
        title="Risk Distribution",
        color="Risk_Level",
        color_discrete_map={
            "Low":"green",
            "Medium":"orange",
            "High":"red"
        }
    )

    st.plotly_chart(fig1, use_container_width=True)

with right:

    sector = df.groupby("Sector")["Project_Cost_Million_USD"].sum().reset_index()

    fig2 = px.bar(
        sector,
        x="Sector",
        y="Project_Cost_Million_USD",
        color="Sector",
        title="Investment by Sector"
    )

    st.plotly_chart(fig2, use_container_width=True)

st.divider()

st.subheader("🌍 Project Portfolio")

st.dataframe(df, use_container_width=True)

st.divider()

st.subheader("📌 Executive Insights")

if high_risk >= 3:

    st.error("""
• High-risk projects require immediate monitoring.

• Consider reducing leverage.

• Improve construction execution.

• Review financing strategy.

• Strengthen contingency planning.
""")

else:

    st.success("""
Portfolio remains financially stable.

Continue regular monitoring.

Investment diversification is satisfactory.
""")
    st.divider()

st.subheader("📥 Download Dataset")

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📄 Download Infrastructure Dataset (CSV)",
    data=csv,
    file_name="infrastructure_projects.csv",
    mime="text/csv"
)