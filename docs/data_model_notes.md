# FP&A Profitability Analysis Project

## Objective
Build an FP&A analytics platform for:
- profitability analysis
- budget vs actual analysis
- forecast reporting
- executive KPI dashboards

## Database
fpna_analytics

## Dimension Tables
- dim_product
- dim_customer
- dim_region
- dim_date

## Fact Tables
- fact_sales_actuals
- fact_budget
- fact_forecast

## Forecast Versions

The `fact_forecast` table contains multiple forecast scenarios used for variance and forecast accuracy analysis.

### Forecast Scenarios

| Forecast Version | Description |
|---|---|
| Q1_FORECAST | Initial forecast prepared early in the fiscal year |
| MID_YEAR_FORECAST | Revised forecast prepared mid-year based on actual business performance |

These forecast versions are intentionally stored in the same table to support:
- rolling forecast analysis
- forecast accuracy tracking
- scenario comparison
- Power BI forecast version filtering

## Analytics Views

### vw_profitability_kpis
Provides transaction-level profitability metrics including:
- gross revenue
- net revenue
- COGS
- gross profit
- operating income
- gross margin %
- operating margin %

Used for profitability analysis and executive KPI reporting.

---

### vw_actual_vs_budget
Compares actual financial performance against budget targets by:
- month
- product
- region

Used for variance analysis, budget performance tracking, and management reporting.

---

### vw_actual_vs_forecast
Compares actual financial performance against multiple forecast scenarios by:
- month
- product
- region
- forecast version

Used for forecast accuracy analysis, rolling forecast reporting, and scenario comparison.
