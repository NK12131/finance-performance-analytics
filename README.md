# FP&A Profitability & Variance Analysis

## Project Overview

This project is an end-to-end FP&A analytics platform built using:

- SQL Server
- SQL
- Python
- Power BI
- GitHub

The objective of this project is to demonstrate how modern finance teams can leverage analytics engineering, automation, AI-enhanced analytics workflows, and business intelligence to improve:

- profitability analysis
- budget monitoring
- forecast performance tracking
- executive decision-making

This project was built as part of my transition into Tech Finance and modern data-driven financial analytics.

---

# Business Problem

Finance teams require scalable analytical solutions to:

- monitor profitability performance
- analyze revenue trends
- compare actuals vs budget
- track forecast accuracy
- identify margin drivers
- support executive decision-making

Traditional spreadsheet-based reporting often creates:

- manual processes
- inconsistent calculations
- limited scalability
- reduced analytical visibility

This project demonstrates how SQL, Python, and Power BI can be integrated into a modern FP&A analytics workflow.

---

# Project Architecture

```text
SQL Server Database
        ↓
SQL Views & Business Logic
        ↓
Python Data Generation & Automation
        ↓
Power BI Dashboarding & Visualization
        ↓
Executive Financial Insights
```

---

# Technology Stack

| Technology | Purpose |
|---|---|
| SQL Server | Data warehouse & storage |
| SQL | Data transformation & KPI calculations |
| Python | Data generation & automation |
| Pandas & NumPy | Financial dataset simulation |
| Power BI | Dashboarding & executive reporting |
| GitHub | Version control & portfolio presentation |

---

# Data Model

The project uses a simplified star-schema-inspired financial model.

## Fact Tables

### fact_sales_actuals

Contains transactional sales data including:

- quantity
- pricing
- discounts
- costs
- operating expense allocations

### fact_budget

Contains budgeted financial metrics:

- budget revenue
- budget COGS
- budget operating expenses

### fact_forecast

Contains forecasted financial metrics:

- forecast revenue
- forecast COGS
- forecast operating expenses

---

## Dimension Tables

### dim_customer

- customer segmentation
- industry classification

### dim_product

- product categories
- product hierarchy

### dim_region

- regional performance analysis

### dim_date

- time intelligence & trend analysis

---

# SQL Business Logic

The project includes layered SQL transformations and reusable analytical views.

## Profitability KPI View

```sql
vw_profitability_kpis
```

Calculates:

- gross revenue
- net revenue
- gross profit
- operating income
- gross margin %
- operating margin %

Uses:

- Common Table Expressions (CTEs)
- layered business logic
- reusable KPI calculations

---

## Budget Variance View

```sql
vw_actual_vs_budget
```

Calculates:

- revenue variance
- revenue variance %
- gross profit variance
- operating expense variance
- margin variance

---

## Forecast Variance View

```sql
vw_actual_vs_forecast
```

Calculates:

- forecast variance
- forecast accuracy
- forecast profitability analysis

---

# Power BI Dashboard Pages

## 1. Executive Overview

Executive-level dashboard focused on:

- profitability KPIs
- revenue trends
- actual vs budget analysis
- monthly variance analysis

Includes:

- KPI cards
- trend analysis
- waterfall variance visualization
- executive performance monitoring

---

## 2. Operational Analysis

Operational reporting focused on:

- regional performance
- product category analysis
- operational profitability
- detailed revenue breakdowns

---

## 3. Forecast & Planning Analytics

Planning-focused dashboard analyzing:

- forecast accuracy
- actual vs forecast trends
- profitability forecasting
- regional forecast performance

---

# Key FP&A Metrics

The project includes calculations for:

- Revenue
- Gross Profit
- Gross Margin %
- Operating Income
- Operating Margin %
- Budget Variance
- Forecast Variance
- Forecast Accuracy
- Revenue Variance %

---

# Python Automation

Python was used to:

- generate realistic FP&A datasets
- simulate budget & forecast scenarios
- automate financial data creation
- support analytical testing

Libraries used:

- pandas
- numpy
- sqlalchemy
- pyodbc

---

# Key Business Insights

The dashboards help identify:

- profitability trends
- margin compression
- regional performance gaps
- budget deviations
- forecast reliability
- operational efficiency opportunities

---

# Challenges Solved

During development, several analytical and modeling challenges were addressed:

- resolving Power BI relationship issues
- correcting forecast duplication problems
- improving forecast realism
- aligning actuals vs forecast calculations
- implementing conditional formatting logic
- optimizing SQL KPI calculations

---

# Future Enhancements

Future versions of the project may include:

- Volume-Price-Mix (VPM) variance analysis
- scenario planning models
- rolling forecasts
- advanced DAX measures
- Power BI drill-through analysis
- dynamic executive commentary
- automated ETL pipelines
- AI-driven financial insights
- predictive forecasting models

---

# Career Transition

This project reflects my transition into Tech Finance, AI-enabled financial analytics, and modern data-driven decision support by combining:

- finance expertise
- SQL analytics
- Python automation
- Power BI storytelling
- business intelligence
- analytics engineering concepts
- AI-enhanced analytics workflows

The objective is to build scalable, automated, and insight-driven financial solutions aligned with modern finance transformation initiatives.

This project demonstrates practical capabilities in:

- financial analytics
- data modeling
- KPI engineering
- reporting automation
- executive dashboard development
- business-oriented data storytelling

---

# Repository Structure

```text
FP&A-SQL-PROFITABILITY-ANALYSIS
│
├── sql/
├── python/
├── powerbi/
├── screenshots/
├── docs/
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Dashboard Screenshots

## Executive Overview

![Executive Overview](screenshots/executive_overview.png)

---

## Operational Analysis

![Operational Analysis](screenshots/operational_analysis.png)

---

## Forecast & Planning Analytics

![Forecast & Planning Analytics](screenshots/forecast_planning_analysis.png)

---

# Author

Samuel Marius Cyril DOUMBE

Finance Professional Transitioning into Tech Finance & AI-Enabled Financial Analytics

SQL | Python | Power BI | Analytics Engineering | Business Intelligence