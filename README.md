# 🏗️ InfraRisk AI
### Infrastructure Finance Risk Modelling & Credit Assessment using Machine Learning

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-green)
![Random Forest](https://img.shields.io/badge/Model-Random%20Forest-orange)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)

---

# 📖 Project Overview

InfraRisk AI is an AI-powered Infrastructure Finance Risk Assessment System developed to analyze infrastructure projects and predict their financial risk using Machine Learning.

The system combines data analytics, geospatial visualization, predictive modeling, stress testing, and portfolio analysis into a single interactive Streamlit application.

This project demonstrates how Artificial Intelligence can support financial institutions and infrastructure investors in evaluating project risk before investment decisions.

---

# 🚀 Features

## 📊 Executive Dashboard
- Infrastructure project overview
- KPI metrics
- Interactive dataset table
- Download dataset (CSV)

---

## 🌍 Geospatial Risk Analysis
- Interactive world map
- Risk-based project visualization
- Sector filtering
- Risk-level filtering

---

## 🤖 AI Credit Risk Assessment
- Random Forest Machine Learning Model
- Predicts:
  - Low Risk
  - Medium Risk
  - High Risk
- Prediction confidence
- Feature Importance visualization
- Risk Probability Analysis
- AI Recommendation Engine

---

## 📉 Financial Stress Testing
Simulates financial scenarios using:

- Interest Rate
- Debt Ratio
- Inflation
- GDP Growth
- Construction Delay

---

## 📁 Portfolio Analytics
Analyze the complete infrastructure portfolio using:

- Risk Distribution
- Sector Distribution
- Country Distribution
- Investment Analysis
- Interactive Charts

---

## 📄 Report Generation

Generate:

- Executive PDF Report
- AI Prediction PDF Report
- CSV Prediction Report

---

# 🧠 Machine Learning

Model Used:

- Random Forest Classifier

Features Used:

- Project Cost
- Debt Ratio
- Interest Rate
- Construction Delay
- Inflation Rate
- GDP Growth
- Sector
- Country

Prediction Output:

- Low Risk
- Medium Risk
- High Risk

---

# 🛠️ Tech Stack

Frontend
- Streamlit

Backend
- Python

Machine Learning
- Scikit-learn
- Random Forest

Visualization
- Plotly
- Folium
- Streamlit-Folium

Data Processing
- Pandas
- NumPy

Model Storage
- Joblib

Report Generation
- ReportLab

---

# 📂 Project Structure

```
InfraRisk_AI/

│
├── assets/
├── data/
│   └── infrastructure_projects.csv
│
├── models/
│   ├── risk_model.pkl
│   ├── encoders.pkl
│   └── train_model.py
│
├── pages/
│   ├── 1_Executive_Dashboard.py
│   ├── 2_Geospatial_Risk.py
│   ├── 3_Credit_Risk_AI.py
│   ├── 4_Financial_Stress_Test.py
│   └── 5_Portfolio_Analytics.py
│
├── reports/
├── utils/
│   ├── generate_dataset.py
│   └── report_generator.py
│
├── app.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

Clone Repository

```bash
git clone https://github.com/meetgupta-29/InfraRisk_AI.git
```

Open Project

```bash
cd MATRISK----AI
```

Install Requirements

```bash
pip install -r requirements.txt
```

Run Application

```bash
streamlit run app.py
```

---

# 📸 Application Screens

Add screenshots here:

- Executive Dashboard
- Geospatial Risk
- Credit Risk AI
- Financial Stress Test
- Portfolio Analytics

---

# 📊 Dataset

The project uses a synthetic infrastructure finance dataset containing **1000 projects**.

Dataset includes:

- Project Cost
- Sector
- Country
- Debt Ratio
- Interest Rate
- Inflation
- GDP Growth
- Construction Delay
- Risk Level

---

# 🎯 Future Improvements

- Deep Learning Models
- Real-world API Integration
- Live Financial Data
- Cloud Deployment
- User Authentication
- AI Chat Assistant
- Time-Series Forecasting

---

# 👨‍💻 Developer

**Meet Gupta**

Data Science & AI Internship Project

---

# 📜 License

This project is developed for educational and internship purposes.