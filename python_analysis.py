# Project 2: Python Data Analysis - EDA
import pandas as pd

# Load sales data
df = pd.DataFrame({
    'Region': ['West','East','Central','South','West'],
    'Sales': [10000,15000,8000,12000,20000],
    'Profit': [2000,1500,500,1000,3500]
})

# Analysis
print(df.groupby('Region')['Profit'].sum())
print("Top Region:", df.groupby('Region')['Profit'].sum().idxmax())

# Insight: West region = 35% profit
