
ALTER VIEW vw_actual_vs_forecast AS 

WITH actual_monthly AS (
        SELECT 
            DATEFROMPARTS(
                            YEAR(transaction_date),
                            MONTH(transaction_date),1
            ) AS actual_month,
            product_id,
            region_id,
            SUM(net_revenue) AS total_actual_net_revenue,
            SUM(cogs) AS total_actual_cogs,
            SUM(operating_expense) AS total_actual_opex,
            SUM(operating_income) AS total_actual_operating_inc
            
        FROM vw_profitability_kpis
        GROUP BY DATEFROMPARTS(YEAR(transaction_date),MONTH(transaction_date),1),
                product_id,
                region_id
)

SELECT
     a.actual_month,
     a.product_id,
     a.region_id,

     a.total_actual_net_revenue,
     f.forecast_revenue,
     a.total_actual_net_revenue-f.forecast_revenue AS revenue_variance,
     100*((a.total_actual_net_revenue/NULLIF(f.forecast_revenue,0))-1) AS revenue_variance_pct,

     a.total_actual_cogs,
     f.forecast_cogs,
     a.total_actual_cogs-f.forecast_cogs AS cogs_variance,

     a.total_actual_opex,
     f.forecast_opex,
     a.total_actual_opex-f.forecast_opex AS opex_variance,

      a.total_actual_operating_inc,
      f.forecast_revenue-f.forecast_cogs-f.forecast_opex AS forecast_operating_inc,
      a.total_actual_operating_inc-(f.forecast_revenue-f.forecast_cogs-f.forecast_opex) AS operating_inc_variance

FROM actual_monthly AS a
INNER JOIN fact_forecast AS f
    ON a.actual_month=f.forecast_month
    AND a.product_id=f.product_id
    AND a.region_id=f.region_id;
