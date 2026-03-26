# Import sales data of a Cosmetic Company. Analyze it using visualization with Matplotlib:
# a) Read the total profit of all the months and visualize it using a Line Plot.
# b) Read all product sales data and show it using a Multiline Plot.
# c) Read face cream and face wash product sales data and show it using a Bar chart.
# d) Calculate total sale data for last year for each product and show it using a Pie chart.
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("company_sales_data.csv")

x = df["month_number"]

# a) total profit line plot
plt.plot(x, df["total_profit"], marker="o")
plt.title("Total Profit per Month")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.grid(True)
plt.show()

# b) multiline plot all products
plt.plot(x, df["facecream"], label="Face Cream")
plt.plot(x, df["facewash"], label="Face Wash")
plt.plot(x, df["toothpaste"], label="Toothpaste")
plt.plot(x, df["bathingsoap"], label="Bathing Soap")
plt.plot(x, df["shampoo"], label="Shampoo")
plt.plot(x, df["moisturizer"], label="Moisturizer")

plt.title("All Product Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)
plt.show()

# c) bar chart facecream and facewash
plt.bar(x-0.2, df["facecream"], width=0.4, label="Face Cream")
plt.bar(x+0.2, df["facewash"], width=0.4, label="Face Wash")

plt.title("Face Cream vs Face Wash Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)
plt.show()

# d) pie chart yearly sales
sales = [
    df["facecream"].sum(),
    df["facewash"].sum(),
    df["toothpaste"].sum(),
    df["bathingsoap"].sum(),
    df["shampoo"].sum(),
    df["moisturizer"].sum()
]

names = ["Face Cream", "Face Wash", "Toothpaste", "Bathing Soap", "Shampoo", "Moisturizer"]

plt.pie(sales, labels=names, autopct="%0.1f%%")
plt.title("Total Sales in Last Year")
plt.show()