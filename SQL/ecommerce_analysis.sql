1--Basic exploration
select count(*)from ecommerce;
select * from ecommerce limit 5;

2--Top 10 product categories by revenue
select product_category_name,
round(sum(price)::numeric,2)as revenue
from ecommerce
group by product_category_name
order by revenue desc limit 10;

3--Month-over-month revenue comparison(LAG)
with monthly_sales as(
select date_trunc('month',order_purchase_timestamp::timestamp)as month,
round(sum(price)::numeric,2)as revenue
from ecommerce
group by month

)
select month,
revenue,
lag(revenue)over(order by month)as prev_revenue,
round(revenue - lag(revenue)over(order by month),2)as revenue_change
from monthly_sales;

4--Total 5 states by revenue
select customer_state,
round(sum(price)::numeric,2)as revenue
from ecommerce
group by customer_state
order by revenue desc
limit 5;

5--Running total revenue
with monthly_sales as(
select date_trunc('month',order_purchase_timestamp::timestamp)as month,
sum(price)as revenue
from ecommerce
group by month
)
select month,
round(revenue::numeric,2)as revenue,
round(sum(revenue)over(order by month)::numeric,2)as cumulative_revenue
from monthly_sales;

6--Customer ranking
select customer_unique_id,
round(sum(price)::numeric,2)as total_spent,
dense_rank()over(order by sum(price)desc)as customer_rank
from ecommerce
group by customer_unique_id
order by customer_rank
limit 10;

7--Payment type analysis
select payment_type,
count(*)as total_orders,
round(sum(payment_value)::numeric,2)as revenue
from ecommerce
group by payment_type
order by revenue desc;

8--Average delivery time
select round(avg(order_delivered_customer_date::date - 
order_purchase_timestamp::date),2)
as avg_delivery_days
from ecommerce;

--Insights:
--Top product categories generated the highest revenue.
--Revenue showed month to month changes with overall growth.
--sp state contributed the highest revenue.
--Top customers contributed signficantly to total sales.
--Credit card was the most prefferd payment method.
--Average delivery time was 12.42 days.

--Recommendations:
--Focus on high-performing product categories.
--Strengthen customer retention strategies.
--Increase marketing during low-sales periods.
--Expand business efforts in high revenue states.
--Improve delivery efficiency to enhance customer satisfaction.


















