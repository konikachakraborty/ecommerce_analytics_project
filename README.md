# 🛒 E-Commerce Analytics Project

## 📌 Project Overview

This project analyzes an e-commerce dataset to uncover valuable business insights related to sales performance, customer behavior, product performance, and payment trends.

The project follows a complete data analytics workflow, including data cleaning with Python, business analysis using SQL, and interactive dashboard creation in Power BI.

---

## 🎯 Objectives

- Clean and preprocess raw e-commerce data.
- Analyze sales performance and customer behavior.
- Identify top-performing products and regions.
- Study payment preferences and delivery performance.
- Build an interactive Power BI dashboard for business decision-making.

---

# 🛠️ Tech Stack

- Python (Pandas, Matplotlib)
- PostgreSQL
- SQL
- Power BI
- Excel / CSV
- Git & GitHub

---

# 📂 Project Structure

```text
ecommerce_analytics_project/
│
├── Dashboard/
│   ├── 01_Overview_analysis_dashboard.png
│   ├── 02_Customer_analysis_dashboard.png
│   └── 03_Product & Payment_analysis_dashboard.png
│
├── Data/
│   ├── olist_customers_dataset.csv
│   ├── olist_orders_dataset.csv
│   ├── olist_order_items_dataset.csv
│   ├── olist_order_payments_dataset.csv
│   └── olist_products_dataset.csv
│
├── Process data/
│   └── cleaned_ecommerce_dataset.csv
│
├── Python/
│   ├── data_cleaning.py
│   └── ecommerce_analysis.py
│
├── SQL/
│   └── ecommerce_analysis.sql
│
└── README.md
```

---

# 🔄 Project Workflow

```
Raw Dataset
     │
     ▼
Data Cleaning (Python)
     │
     ▼
Cleaned Dataset
     │
     ▼
PostgreSQL Database
     │
     ▼
SQL Analysis
     │
     ▼
Power BI Dashboard
     │
     ▼
Business Insights & Recommendations
```

---

# 🧹 Data Cleaning

The raw datasets were cleaned and merged using Python.

### Steps Performed

- Loaded multiple datasets
- Checked missing values
- Removed null values
- Merged datasets
- Renamed columns
- Converted date columns into datetime format
- Exported cleaned dataset
- Loaded cleaned dataset into PostgreSQL

---

# 🐍 Python Analysis

Python was used for exploratory data analysis and visualization.

### Analysis Performed

- Total Revenue
- Total Orders
- Total Customers
- Average Order Value (AOV)
- Monthly Revenue Trend
- Sales Trend Visualization

---

# 🗄️ SQL Analysis

Business analysis was performed using PostgreSQL.

### SQL Queries

- Basic Data Exploration
- Top 10 Product Categories by Revenue
- Month-over-Month Revenue Comparison (LAG)
- Top 5 States by Revenue
- Running Total Revenue
- Customer Ranking (DENSE_RANK)
- Payment Type Analysis
- Average Delivery Time

---

# 📊 Power BI Dashboard

The dashboard contains three interactive pages.

## 📈 Overview Dashboard

- Total Revenue
- Total Orders
- Total Customers
- Average Order Value
- Monthly Revenue Trend
- Revenue by State
- Top Product Categories

---

## 👥 Customer Analysis Dashboard

- Customer Distribution
- Top Cities
- Customer States
- Customer Segmentation
- Average Order Value
- Customer Insights

---

## 💳 Product & Payment Analysis Dashboard

- Top Product Categories
- Product Revenue Analysis
- Payment Type Distribution
- Revenue by Payment Method
- Delivery Analysis

---

# 💡 Key Insights

- Top product categories generated the highest revenue.
- Revenue showed consistent growth across most months.
- A few states contributed a major share of total sales.
- Credit Card was the most preferred payment method.
- Top customers generated a significant portion of total revenue.
- Average delivery time was approximately **12.42 days**.

---

# 📌 Business Recommendations

- Focus marketing efforts on high-performing product categories.
- Strengthen customer retention strategies.
- Improve delivery efficiency.
- Increase promotions during low-sales periods.
- Encourage digital payment methods through targeted offers.

---

# 🚀 Skills Demonstrated

- Data Cleaning
- Data Preprocessing
- Exploratory Data Analysis (EDA)
- SQL Queries
- Window Functions
- Common Table Expressions (CTEs)
- Data Visualization
- Dashboard Design
- Business Analysis
- Business Insights
- Power BI
- Python
- PostgreSQL
- Git & GitHub

---

# 📷 Dashboard Preview

### 1. Overview Dashboard

![Overview Dashboard](Dashboard/01_Overview_analysis_dashboard.png)

### 2. Customer Analysis Dashboard

![Customer Analysis Dashboard](Dashboard/02_Customer_analysis_dashboard.png)

### 3. Product & Payment Analysis Dashboard

![Product & Payment Analysis Dashboard](Dashboard/03_Product_Payment_analysis_dashboard.png)

---

# ⭐ Project Outcome

This project demonstrates an end-to-end data analytics workflow, starting from raw data preprocessing to SQL-based business analysis and interactive Power BI dashboards. The project showcases practical skills in Python, SQL, PostgreSQL, Power BI, and business intelligence by transforming raw transactional data into actionable insights.