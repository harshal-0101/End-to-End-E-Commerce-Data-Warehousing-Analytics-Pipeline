select * from customer_revenue order by total_revenue DESC limit 10;
select * from monthly_revenue  order by total_revenue DESC limit 10;
select * from product_revenue order by total_revenue limit 10;
select * from state_revenue order by total_revenue limit 10;
select * from order_summary order by total_order_value DESC limit 10;


-- Top 10 Customers

SELECT *
FROM customer_revenue
ORDER BY total_revenue DESC
LIMIT 10;


-- Top 10 Products

SELECT *
FROM product_revenue
ORDER BY total_revenue DESC
LIMIT 10;

-- Revenue By State

SELECT *
FROM state_revenue
ORDER BY total_revenue DESC;

-- Average Order Value

SELECT
    ROUND(AVG(total_order_value)::numeric,2) AS avg_order_value
FROM order_summary;


-- Monthly Revenue Trend

SELECT *
FROM monthly_revenue
ORDER BY month_year DESC;


SELECT *
FROM order_summary
WHERE TO_CHAR(order_purchase_timestamp,'YYYY-MM')='2018-09';



SELECT
    TO_CHAR(order_purchase_timestamp, 'YYYY-MM') AS month_year,
    COUNT(*) AS total_orders
FROM order_summary
GROUP BY 1
ORDER BY 1 DESC;


ALTER TABLE order_summary
ALTER COLUMN order_purchase_timestamp
TYPE TIMESTAMP
USING order_purchase_timestamp::TIMESTAMP;

SELECT column_name, data_type
FROM information_schema.columns
WHERE table_name = 'order_summary';

SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public';