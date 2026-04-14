import pandas as pd # type: ignore

# load dataset
df = pd.read_csv("train.csv")

df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)
df['Ship Date'] = pd.to_datetime(df['Ship Date'], dayfirst=True)

df['Postal Code'] = df['Postal Code'].fillna(0)

print("Duplicates:", df.duplicated().sum())
df = df.drop_duplicates()

# print(df.info())
# print(df.head())

#total revenue 
total_sales = df['Sales'].sum()
print("\n Total Revenue:", round(total_sales, 2))

#best selling products 
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)

print("\n Top 10 Products by Revenue:")
print(top_products)

#best category 
category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)

print("\n Sales by Category:")
print(category_sales)

#region performance
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)

print("\n Region-wise Sales:")
print(region_sales)

#customer value 
top_customers = df.groupby('Customer Name')['Sales'].sum().sort_values(ascending=False).head(10)

print("\nTop Customers by Revenue:")
print(top_customers)

#monthly trend 
df['Month'] = df['Order Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Sales'].sum()

print("\nMonthly Sales Trend:")
print(monthly_sales)

