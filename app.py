import streamlit as st
import pandas as pd

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="InfraRisk AI",
    page_icon="🏗️",
    layout="wide"
)

# Load Dataset

df = pd.read_csv("data/infrastructure_projects.csv")


# Title

st.title("🏗️ InfraRisk AI")
st.subheader("Infrastructure Finance Risk Modelling & Credit Assessment")

st.success("Dataset Loaded Successfully!")


# Dashboard Cards

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Projects", len(df))

with col2:
    st.metric("Average Cost (Million USD)",
              round(df["Project_Cost_Million_USD"].mean(),2))

with col3:
    st.metric("Average Debt Ratio",
              round(df["Debt_Ratio"].mean(),2))

with col4:
    high_risk = len(df[df["Risk_Level"]=="High"])
    st.metric("High Risk Projects", high_risk)

st.divider()

st.subheader("Infrastructure Project Dataset")

st.dataframe(df, use_container_width=True)