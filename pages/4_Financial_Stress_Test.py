import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(
    page_title="Financial Stress Testing",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Financial Stress Testing Dashboard")
st.subheader("Simulate Economic Stress Scenarios")

model = joblib.load("models/risk_model.pkl")
encoders = joblib.load("models/encoders.pkl")

st.sidebar.header("Stress Scenario")

project_cost = st.sidebar.slider(
    "Project Cost (Million USD)",
    100,
    3000,
    1000
)

debt_ratio = st.sidebar.slider(
    "Debt Ratio",
    0.20,
    1.00,
    0.60
)

interest_rate = st.sidebar.slider(
    "Interest Rate (%)",
    2.0,
    15.0,
    8.0
)

delay = st.sidebar.slider(
    "Construction Delay (Months)",
    0,
    24,
    6
)

inflation = st.sidebar.slider(
    "Inflation Rate (%)",
    1.0,
    10.0,
    5.5
)

gdp = st.sidebar.slider(
    "GDP Growth (%)",
    1.0,
    10.0,
    6.5
)

sector = st.sidebar.selectbox(
    "Sector",
    encoders["Sector"].classes_
)

country = st.sidebar.selectbox(
    "Country",
    encoders["Country"].classes_
)

st.success("✅ Stress scenario loaded successfully.")
# Encode Inputs
sector_encoded = encoders["Sector"].transform([sector])[0]
country_encoded = encoders["Country"].transform([country])[0]

# Prepare Input
sample = np.array([[
    project_cost,
    debt_ratio,
    interest_rate,
    delay,
    inflation,
    gdp,
    sector_encoded,
    country_encoded
]])

# AI Prediction
prediction = model.predict(sample)[0]
probability = model.predict_proba(sample)[0]

risk_label = encoders["Risk_Level"].inverse_transform([prediction])[0]
confidence = probability[prediction] * 100

st.divider()

st.subheader("🤖 AI Stress Test Result")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Predicted Risk",
        risk_label
    )

with col2:
    st.metric(
        "Confidence",
        f"{confidence:.2f}%"
    )

if risk_label == "Low":
    st.success("✅ Low Risk Scenario")

elif risk_label == "Medium":
    st.warning("⚠ Medium Risk Scenario")

else:
    st.error("🚨 High Risk Scenario")
    st.divider()

st.subheader("📊 Stress Impact Analysis")

# Baseline values
baseline_interest = 8.0
baseline_inflation = 5.5
baseline_delay = 6
baseline_gdp = 6.5

interest_change = interest_rate - baseline_interest
inflation_change = inflation - baseline_inflation
delay_change = delay - baseline_delay
gdp_change = gdp - baseline_gdp

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Interest Rate Change",
    f"{interest_rate:.1f}%",
    delta=f"{interest_change:+.1f}%"
)

col2.metric(
    "Inflation Change",
    f"{inflation:.1f}%",
    delta=f"{inflation_change:+.1f}%"
)

col3.metric(
    "Delay Change",
    f"{delay} Months",
    delta=f"{delay_change:+d}"
)

col4.metric(
    "GDP Growth",
    f"{gdp:.1f}%",
    delta=f"{gdp_change:+.1f}%"
)
import plotly.express as px

stress_df = pd.DataFrame({
    "Factor": [
        "Interest Rate",
        "Inflation",
        "Delay",
        "GDP Growth"
    ],
    "Normal": [
        baseline_interest,
        baseline_inflation,
        baseline_delay,
        baseline_gdp
    ],
    "Stress": [
        interest_rate,
        inflation,
        delay,
        gdp
    ]
})

chart_df = stress_df.melt(
    id_vars="Factor",
    var_name="Scenario",
    value_name="Value"
)

fig = px.bar(
    chart_df,
    x="Factor",
    y="Value",
    color="Scenario",
    barmode="group",
    title="Normal vs Stress Scenario"
)

st.plotly_chart(fig, use_container_width=True)
st.divider()

st.subheader("🤖 AI Stress Recommendation")

if risk_label == "High":

    st.error("""
### 🚨 High Stress Scenario

The AI recommends the following actions:

• Reduce Debt Ratio below 60%

• Delay new financing until economic conditions improve

• Increase project contingency reserve

• Re-negotiate loan interest rates

• Improve project execution schedule

• Conduct a detailed financial review

• Closely monitor inflation and GDP trends
""")

elif risk_label == "Medium":

    st.warning("""
### ⚠ Medium Stress Scenario

The AI recommends:

• Monitor project cash flow every month

• Reduce construction delays where possible

• Maintain reserve funds

• Review financing structure

• Monitor macroeconomic indicators regularly
""")

else:

    st.success("""
### ✅ Low Stress Scenario

The AI recommends:

• Continue project as planned

• Maintain current financing strategy

• Monitor quarterly financial performance

• Low probability of financial distress

• Suitable for investment
""")
    st.divider()

st.subheader("📊 Stress Severity")

if confidence < 40:
    severity = 30

elif confidence < 70:
    severity = 65

else:
    severity = 90

st.progress(severity / 100)

st.write(f"### Overall Stress Severity : **{severity}%**")
st.divider()

st.subheader("📋 Executive Summary")

summary = f"""

**Project Risk:** {risk_label}

**Prediction Confidence:** {confidence:.2f}%

**Interest Rate:** {interest_rate}%

**Inflation:** {inflation}%

**GDP Growth:** {gdp}%

**Construction Delay:** {delay} Months

The AI model has evaluated the current economic conditions and generated a stress prediction based on the selected financial parameters.
"""

st.info(summary)
    