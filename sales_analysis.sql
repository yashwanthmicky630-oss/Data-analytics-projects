-- Project 1: Sales Profit Analysis
-- By Yashwanth - Data Analyst Portfolio

-- Q1: Find top 3 regions by profit
SELECT Region, SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY Region
ORDER BY Total_Profit DESC
LIMIT 3;

-- Q2: Most profitable product category
SELECT Category, SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY Category
ORDER BY Total_Profit DESC;

-- Q3: Monthly sales trend
SELECT MONTH(OrderDate) AS Month, SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY Month
ORDER BY Month;

-- Insight: West region generates 35% profit
-- Insight: Technology is highest profit category
