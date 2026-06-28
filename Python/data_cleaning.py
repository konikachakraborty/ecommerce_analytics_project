import pandas as pd

#data load
customers = pd.read_csv("C:/Users/dell/Downloads/archive (2)/olist_customers_dataset.csv")
orders = pd.read_csv("C:/Users/dell/Downloads/archive (2)/olist_orders_dataset.csv")
order_items = pd.read_csv("C:/Users/dell/Downloads/archive (2)/olist_order_items_dataset.csv")
payment = pd.read_csv("C:/Users/dell/Downloads/archive (2)/olist_order_payments_dataset.csv")
products = pd.read_csv("C:/Users/dell/Downloads/archive (2)/olist_products_dataset.csv")

print(customers.head())
print(customers.shape)
print(orders.head())
print(orders.shape)
print(order_items.head())
print(order_items.head())
print(payment.head())
print(payment.shape)
print(products.head())
print(products.shape)
print(customers.info())
print(orders.info())
print(order_items.info())
print(payment.info())
print(products.info())

#check missing value
print(customers.isnull().sum())
print(orders.isnull().sum())
print(order_items.isnull().sum())
print(payment.isnull().sum())
print(products.isnull().sum())

products.dropna(inplace=True)
print(products.isnull().sum)



#merge dataset
#orders + customers
df = orders.merge(customers,on='customer_id', how = 'left')
df = df.merge(order_items,on='order_id', how = 'left')
df = df.merge(payment, on='order_id', how = 'left')
df = df.merge(products, on='product_id', how= 'left')

print(df.head())
print(df.info())


df.dropna(subset=['product_category_name'],inplace= True)
df.dropna(subset=['product_weight_g'],inplace= True)
df.dropna(subset=['product_length_cm'],inplace= True)
df.dropna(subset=['product_height_cm'],inplace= True)
df.dropna(subset=['product_width_cm'],inplace= True)
df.dropna(subset=['payment_sequential'],inplace= True)
df.dropna(subset=['payment_type'],inplace= True)
df.dropna(subset=['payment_installments'],inplace= True)
df.dropna(subset=['payment_value'],inplace= True)

df.dropna(subset=['product_category_name'],inplace= True)
print(df.isnull().sum())
print(df.shape)

df.rename(columns={'product_name_lenght': 'product_name_length'},inplace=True)
df.rename(columns={'product_description_lenght': 'product_discription_length'},inplace=True)
df.rename(columns={'product_lenght_cm': 'product_length_cm'},inplace=True)


print(df.columns)
df.to_csv('Data/cleaned_ecommerce_dataset.csv', index=False)


import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv(r"C:\Users\dell\Documents\ecommerce_analytics_project\Process data\cleaned_ecommerce_dataset.csv")
engine = create_engine("postgresql+psycopg2://postgres:1234@localhost:5432/ecommerce_db")

df.to_sql(
    "ecommerce",
    engine,
    if_exists="replace",
    index=False
)
print("Data loaded successfully:")

df=pd.read_csv(r"C:\Users\dell\Documents\ecommerce_analytics_project\Process data\ecommerce_cleaned.csv.csv")

df.to_excel(r"C:\Users\dell\Documents\ecommerce_analytics_project\Process data\ecommerce_cleaned.xlsx",index=False)
print("Done")