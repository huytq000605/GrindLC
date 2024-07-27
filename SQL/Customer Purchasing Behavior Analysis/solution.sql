# Write your MySQL query statement below
WITH 
cte1 as (
    SELECT customer_id, category, 
        count(*) OVER (PARTITION BY customer_id, category) as no_txn,
        transaction_date

    FROM Transactions t 
    JOIN Products p ON t.product_id = p.product_id
    ORDER BY no_txn DESC, t.transaction_date DESC
),
cte2 as (
    SELECT customer_id, FIRST_VALUE(category) OVER(PARTITION BY customer_id ORDER BY no_txn DESC, transaction_date DESC) as top_category
    FROM cte1
)
SELECT t.customer_id, sum(t.amount) as total_amount, count(*) as transaction_count,
count(distinct(p.category)) as unique_categories, ROUND(avg(amount), 2) as avg_transaction_amount, 
(SELECT top_category from cte2 where customer_id = t.customer_id limit 1) as top_category,
ROUND(10 * count(*) + sum(amount) / 100, 2) as loyalty_score
FROM Transactions t 
LEFT JOIN Products p ON t.product_id = p.product_id
GROUP BY t.customer_id
ORDER BY loyalty_score DESC, customer_id ASC
