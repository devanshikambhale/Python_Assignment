# Find the average of price for each cut of diamonds in the given DataFrame above.
import pandas as pd

df = pd.read_csv('diamonds.csv')

mean_price = df.groupby('cut')['price'].mean()
print("Mean price for each cut:")
print(mean_price)
# Also find count of diamond, minimum and maximum price for each cut of diamonds in the above given DataFrame.
import pandas as pd
df = pd.read_csv('diamonds.csv')
price_stats = df.groupby('cut')['price'].agg(['count', 'min', 'max'])
print("Count, Min, Max price for each cut:")
print(price_stats)
# Calculate and print average value of parameters x, y, and z separately.
import pandas as pd
df = pd.read_csv('diamonds.csv')
avg_x = df['x'].mean()
avg_y = df['y'].mean()
avg_z = df['z'].mean()
print(f"Average of x is : {avg_x:.2f}")
print(f"Average of y is : {avg_y:.2f}")
print(f"Average of z is : {avg_z:.2f}")