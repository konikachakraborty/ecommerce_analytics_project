import pandas as pd
df = pd.read_csv("Data/cleaned_ecommerce_dataset.csv")
print(df.shape)
print(df.columns)
print(df.head())
print(df.info())

#Total Revenue
total_revenue = df['payment_value'].sum()
print("Total Revenue:",total_revenue)

#Total orders 
total_orders = df['order_id'].nunique()
print("Total Orders:",total_orders)

#Total Cuatomers 
total_customers = df['customer_unique_id'].nunique()
print("Total Customer:",total_customers)

#Average Order Value (AOV)
AOV = total_revenue/total_orders
print("Average Order Value:", round(AOV,2))

print(df.info())

#convert date columns into datetime format
df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
df['Month'] = df['order_purchase_timestamp'].dt.to_period('M')
monthly_sales = df.groupby('Month')['payment_value'].sum()
print(monthly_sales)

#visualization
import matplotlib.pyplot as plt
#Monthly sales line chart
monthly_sales.index= monthly_sales.index.astype(str)
monthly_sales.plot(kind='line', marker='o',figsize=(10,5))
plt.title('Monthly Sales Trend')
plt.xlabel('Months')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

#Insights:
#Montly revenue showed a strong upward trend from 2016 to 2018,reaching its peak in late 2017 \
#maintaining stable performance throughout 2018.
#the sharp decline in september 2018 is likely caused by incomplete data rather than a true drop in sales.

#Recommendation:
#The business should leverage the factors behind peak sales period,strengthen customer retention strategies.
#ensure data completeness before making strategic decisions.

#Top product categories by revenue
top_categories = df.groupby('product_category_name')['payment_value'].sum().sort_values(ascending=False).head(10)

top_categories.plot(kind='bar',figsize=(10,5))
plt.title('Top 10 Product Categories by Revenue')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.show()

#Insights:
#Home & Bath (case_banho)category generated the highest revenue.
#Revenue is concentrated in a few categories,with Home,Beauty,and Acessories leading sales.
#Categories like Automotive and Garden contributed comparatively lower revenue.

#Recommedations:
#Increase inventory and marketing efforts for top-performing categories.
#Use proportion and discount to improve sales in lowo-performing categories.

#Payment type distribution
payment_distribution = df['payment_type'].value_counts()

payment_distribution.plot(kind='pie',autopct = '%1.1f%%',figsize=(6,6))
plt.title('payment type distribution')
plt.ylabel('')
plt.show()

#Insights:
#Credit card dominate transactions,contributing 73.8% of all payments.
#Boleto is the second most preferred payment method.while voucher and debit card usage remains low.

#Recommendation:
#optimize the credit card payment experience.
#encourage alternative payment method through discounts and cashback offers/

#Top states by revenue
top_states = df.groupby('customer_state')['payment_value'].sum().sort_values(ascending=False).head(10)

top_states.plot(kind='bar',figsize=(10,5))
plt.title('Top States by Revenue')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.show()

#Insights:
#SP generated the highest revenue among all states.
#Revenue is highly concentrated in a few states,with SP,RJ and MG leading sales.
#Other states contribute comparatively lower revenue.

#Recommendations:
#Focus marketing and inventory efforts on high-revenue state.
#Explore growth opportunities in lower performing states through targeted compaigns.

#Order status distribution 
order_status = df['order_status'].value_counts()

order_status.plot(kind='bar',figsize=(8,5))
plt.title('Order Status Distribution')
plt.xlabel('Order status')
plt.ylabel('Number of orders')
plt.xticks(rotation=45)
plt.show()

#Insights:
#Most orders were successfully delivered,indicating an efficient order fullfillment process.
#The high delivery success rate reflects effective inventory and logistics management.

#Recommendation:
#Maintain the high delivery success rate through efficient inventory and inventory management.
#Analyze the reasons behind canceled and unavailable orders to further improve customer satisfaction.
#Continue monitor order processing to minimize delays and ensure timely deliveries.

#firstly convert into datetime
df['order_purchase_timestamp']= pd.to_datetime(df['order_purchase_timestamp'])
df['order_delivered_customer_date'] = pd.to_datetime(df['order_delivered_customer_date'])
#Delivery time analysis
df['delivery_days'] = (df['order_delivered_customer_date'] - df['order_purchase_timestamp']).dt.days
df['delivery_days'].hist(bins=20,figsize=(8,5))
plt.title('Delivey Time Distribution')
plt.xlabel('Delivery days')
plt.ylabel('Number of orders')
plt.show()

#Insights:
#Most orders were delivered within a relatively short period,indicating efficient logistics operations.
#Only a small number of orders faced delivery delays.

#Recommendations:
#Monitor delayed orders to improve delivery performance.
#Optimize shipping process to reduce delivery delays.

#Conclusion:
