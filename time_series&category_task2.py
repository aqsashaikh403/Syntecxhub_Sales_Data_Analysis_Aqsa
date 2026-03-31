import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("sales_data.csv")

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'])



# ---------------- LINE CHART ----------------
daily_sales = df.groupby('Date')['Sales'].sum()

plt.figure(8.5)
daily_sales.plot(marker='o')
plt.title("Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.savefig("line_chart.png")
plt.show()
# ---------------- MONTHLY ----------------
monthly_sales = df.resample('ME', on='Date')['Sales'].sum()

plt.figure()
monthly_sales.plot()
plt.title("Monthly Sales")
plt.savefig("monthly_chart.png")
plt.show()
# ---------------- BAR CHART ----------------
category_sales = df.groupby('Category')['Sales'].sum()

plt.figure()
category_sales.plot(kind='bar')
plt.title("Sales by Category")
plt.savefig("bar_chart.png")
plt.show()
#-----------------REGION BAR CHART-------------
region_sales=df.groupby("Region")['Sales'].sum()

plt.figure(figsize=(10,6))
region_sales.plot(kind='bar')
plt.title('Sales by Region')
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.grid(alpha=0.2)
plt.savefig("Region_bar_chart.png")
plt.show()

#-----------------REGION PIE CHART-------------
plt.figure(figsize=(8,6))
region_sales.plot(kind='pie',
autopct='%1.1f%%')
plt.title("Region Share")
plt.ylabel("")
plt.savefig("region_pie_chart.png")
#----------------MONTH BAR-------------
plt.figure(figsize=(10,6))
monthly_sales.plot(kind='bar')
plt.title("Sales by Month")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid(alpha=0.3)
plt.savefig("monthly_bar_chart.png")

month_order=['January','February','March','April','May','june','July','August','September','October','November','December']
monthly_sales=df.groupby('Month')['Sales'].sum()

monthly_sales=monthly_sales.reindex(month_order).fillna(0)
#------------------MONTH LINE CHART-------
plt.figure(figsize=(10,6))
monthly_sales.plot(kind='line',marker='o',linewidth=3)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(alpha=0.3)
plt.savefig("monthly_line_chart.png")
# ---------------- PIE CHART ----------------
plt.figure(figsize=(10,6))
category_sales.plot(kind='pie', autopct='%1.1f%%')
plt.title("Category Share")
plt.ylabel("")
plt.savefig("pie_chart.png")
plt.show()
print("Charts created successfully!")

