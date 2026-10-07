import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import urllib

params = urllib.parse.quote_plus(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=fpna_analytics;"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

np.random.seed(42)

num_rows = 1000

unit_price = np.random.uniform(100, 2000, num_rows).round(2)
discount_rate = np.random.uniform(0.01, 0.15, num_rows).round(4)
target_gross_margin = np.random.uniform(0.25, 0.65, num_rows).round(4)
net_unit_price = unit_price * (1 - discount_rate)
unit_cost = (net_unit_price * (1 - target_gross_margin)).round(2)
opex_rate = np.random.uniform(0.10, 0.30, num_rows).round(4)

sales_data = pd.DataFrame({
    "sale_id": range(1, num_rows + 1),
    "sale_date": np.random.choice(pd.date_range("2026-01-01", "2026-12-31"), num_rows),
    "customer_id": np.random.randint(101, 131, num_rows),
    "product_id": np.random.randint(1, 31, num_rows),
    "region_id": np.random.randint(1, 9, num_rows),
    "quantity": np.random.randint(1, 100, num_rows),
    "unit_price": unit_price,
    "discount_rate": discount_rate,
    "unit_cost": unit_cost,
    "opex_rate": opex_rate
})

#sales_data.to_sql(
#    "fact_sales_actuals",
#    con=engine,
#    if_exists="append",
#    index=False
#)

#print("1000 raw FP&A sales records inserted successfully!")

# -----------------------------
# CREATE REALISTIC BUDGET & FORECAST FROM ACTUALS
# -----------------------------

actuals_df = pd.read_sql("""
    SELECT
        DATEFROMPARTS(YEAR(transaction_date), MONTH(transaction_date), 1) AS month,
        product_id,
        region_id,
        SUM(net_revenue) AS actual_revenue,
        SUM(cogs) AS actual_cogs,
        SUM(operating_expense) AS actual_opex
    FROM vw_profitability_kpis
    GROUP BY
        DATEFROMPARTS(YEAR(transaction_date), MONTH(transaction_date), 1),
        product_id,
        region_id
""", con=engine)

# -----------------------------
# BUDGET DATA
# -----------------------------

budget_df = actuals_df.copy()

budget_df["budget_id"] = range(1, len(budget_df) + 1)
budget_df["budget_month"] = budget_df["month"]

budget_df["budget_revenue"] = (
    budget_df["actual_revenue"] *
    np.random.uniform(1.05, 1.15, len(budget_df))
)

budget_df["budget_cogs"] = (
    budget_df["actual_cogs"] *
    np.random.uniform(1.02, 1.10, len(budget_df))
)

budget_df["budget_opex"] = (
    budget_df["actual_opex"] *
    np.random.uniform(1.03, 1.12, len(budget_df))
)

budget_df = budget_df[
    [
        "budget_id",
        "budget_month",
        "product_id",
        "region_id",
        "budget_revenue",
        "budget_cogs",
        "budget_opex"
    ]
].round(2)

budget_df.to_sql(
    "fact_budget",
    con=engine,
    if_exists="append",
    index=False
)

print("Realistic budget data inserted successfully!")

# -----------------------------
# FORECAST DATA
# -----------------------------

forecast_rows = []
forecast_id = 1

forecast_versions = ["Q1_FORECAST"]

for version in forecast_versions:

    temp_df = actuals_df.copy()

    if version == "Q1_FORECAST":
        revenue_multiplier = np.random.uniform(0.95, 1.08, len(temp_df))
        cogs_multiplier = np.random.uniform(0.80, 1.05, len(temp_df))
        opex_multiplier = np.random.uniform(0.80, 1.05, len(temp_df))

    else:
        revenue_multiplier = np.random.uniform(0.97, 1.03, len(temp_df))
        cogs_multiplier = np.random.uniform(0.95, 1.08, len(temp_df))
        opex_multiplier = np.random.uniform(0.95, 1.08, len(temp_df))

    temp_df["forecast_revenue"] = temp_df["actual_revenue"] * revenue_multiplier
    temp_df["forecast_cogs"] = temp_df["actual_cogs"] * cogs_multiplier
    temp_df["forecast_opex"] = temp_df["actual_opex"] * opex_multiplier
    temp_df["forecast_month"] = temp_df["month"]
    temp_df["forecast_version"] = version

    temp_df["forecast_id"] = range(
        forecast_id,
        forecast_id + len(temp_df)
    )

    forecast_id += len(temp_df)

    forecast_rows.append(temp_df)

forecast_df = pd.concat(forecast_rows)

forecast_df = forecast_df[
    [
        "forecast_id",
        "forecast_month",
        "product_id",
        "region_id",
        "forecast_revenue",
        "forecast_cogs",
        "forecast_opex",
        "forecast_version"
    ]
].round(2)

forecast_df.to_sql(
    "fact_forecast",
    con=engine,
    if_exists="append",
    index=False
)

print("Realistic forecast data inserted successfully!")
