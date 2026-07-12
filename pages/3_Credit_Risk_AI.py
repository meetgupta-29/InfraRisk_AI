import streamlit as st
import pandas as pd
import numpy as np
import joblib


# Page Configuration
st.set_page_config(
    page_title="Credit Risk AI",
    page_icon="🏦",
    layout="wide"
)

st.title("🏦 AI Credit Risk Assessment")
st.subheader("Infrastructure Finance Risk Prediction using Machine Learning")

# Load Model
model = joblib.load("models/risk_model.pkl")
encoders = joblib.load("models/encoders.pkl")

# User Inputs

st.sidebar.header("Project Details")

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

# Encode Inputs

sector_encoded = encoders["Sector"].transform([sector])[0]
country_encoded = encoders["Country"].transform([country])[0]

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

prediction = model.predict(sample)[0]
probability = model.predict_proba(sample)[0]

risk_label = encoders["Risk_Level"].inverse_transform([prediction])[0]

confidence = probability[prediction] * 100


# Dashboard


col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Predicted Risk",
        risk_label
    )

with col2:

    st.metric(
        "Prediction Confidence",
        f"{confidence:.2f}%"
    )

st.divider()

if risk_label == "Low":
    st.success("✅ Low Credit Risk")

elif risk_label == "Medium":
    st.warning("⚠ Medium Credit Risk")

else:
    st.error("🚨 High Credit Risk")

st.divider()

st.subheader("Project Summary")

summary = pd.DataFrame({

    "Feature":[
        "Project Cost",
        "Debt Ratio",
        "Interest Rate",
        "Construction Delay",
        "Inflation",
        "GDP Growth",
        "Sector",
        "Country"
    ],

    "Value":[
        project_cost,
        debt_ratio,
        interest_rate,
        delay,
        inflation,
        gdp,
        sector,
        country
    ]

})

st.dataframe(summary, use_container_width=True)

st.divider()

st.subheader("Model Information")

st.info("""
This prediction is generated using a Random Forest Machine Learning model
trained on the infrastructure project dataset.

The model considers:

- Project Cost
- Debt Ratio
- Interest Rate
- Construction Delay
- Inflation
- GDP Growth
- Sector
- Country

to predict the infrastructure project's Credit Risk Level.
""")