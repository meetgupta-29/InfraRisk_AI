import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
df = pd.read_csv("data/infrastructure_projects.csv")

# Encode categorical columns
encoders = {}

categorical_cols = [
    "Sector",
    "Country",
    "Risk_Level"
]

for col in categorical_cols:
    encoder = LabelEncoder()
    df[col] = encoder.fit_transform(df[col])
    encoders[col] = encoder

# Features
X = df[
    [
        "Project_Cost_Million_USD",
        "Debt_Ratio",
        "Interest_Rate",
        "Construction_Delay_Months",
        "Inflation_Rate",
        "GDP_Growth",
        "Sector",
        "Country"
    ]
]

# Target
y = df["Risk_Level"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Prediction
pred = model.predict(X_test)

accuracy = accuracy_score(y_test, pred)

print("Model Accuracy:", accuracy)

# Save model
joblib.dump(model, "models/risk_model.pkl")

# Save encoders
joblib.dump(encoders, "models/encoders.pkl")

print("Model Saved Successfully!")