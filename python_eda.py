# Sales Analysis using Python Pandas
import pandas as pd

# Sample Data
data = {'Region':['West','East','West'], 'Sales':[10000,15000,20000], 'Profit':[2000,1500,3500]}
df = pd.DataFrame(data)

# Find top region
top_region = df.groupby('Region')['Profit'].sum().sort_values(ascending=False)
print(top_region)
print("Insight: West region highest profit")
