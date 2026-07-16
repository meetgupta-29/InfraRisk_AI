import pandas as pd
import random

random.seed(42)

countries = [
    "India", "USA", "Germany", "Brazil", "UAE",
    "Singapore", "Japan", "Australia", "Canada", "UK"
]

sectors = [
    "Transport",
    "Energy",
    "Water",
    "Telecom",
    "Urban",
    "Manufacturing"
]

projects = []

for i in range(1, 1001):

    project_id = f"P{i:04d}"

    project_name = f"Project_{i}"

    sector = random.choice(sectors)

    country = random.choice(countries)

    cost = random.randint(100, 3000)

    debt = round(random.uniform(0.30, 0.90), 2)

    interest = round(random.uniform(3.0, 12.0), 1)

    delay = random.randint(0, 24)

    inflation = round(random.uniform(2.0, 8.0), 1)

    gdp = round(random.uniform(1.0, 8.0), 1)

    # Random coordinates based on country
    coordinates = {
        "India": (20.5937, 78.9629),
        "USA": (37.0902, -95.7129),
        "Germany": (51.1657, 10.4515),
        "Brazil": (-14.2350, -51.9253),
        "UAE": (23.4241, 53.8478),
        "Singapore": (1.3521, 103.8198),
        "Japan": (36.2048, 138.2529),
        "Australia": (-25.2744, 133.7751),
        "Canada": (56.1304, -106.3468),
        "UK": (55.3781, -3.4360)
    }

    latitude, longitude = coordinates[country]

    # Simple rule for risk label
    if debt > 0.75 or interest > 10 or delay > 15:
        risk = "High"
    elif debt > 0.55 or delay > 7:
        risk = "Medium"
    else:
        risk = "Low"

    projects.append([
        project_id,
        project_name,
        sector,
        country,
        latitude,
        longitude,
        cost,
        debt,
        interest,
        delay,
        inflation,
        gdp,
        risk
    ])

columns = [
    "Project_ID",
    "Project_Name",
    "Sector",
    "Country",
    "Latitude",
    "Longitude",
    "Project_Cost_Million_USD",
    "Debt_Ratio",
    "Interest_Rate",
    "Construction_Delay_Months",
    "Inflation_Rate",
    "GDP_Growth",
    "Risk_Level"
]

df = pd.DataFrame(projects, columns=columns)

df.to_csv("data/infrastructure_projects.csv", index=False)

print("✅ Dataset generated successfully!")
print(f"Total projects: {len(df)}")