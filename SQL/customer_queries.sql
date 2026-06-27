

-- 1. View Complete Dataset
SELECT * FROM Customer_Insights_Dataset;

-- 2. Total Sales
SELECT SUM(Amount) AS Total_Sales
FROM Customer_Insights_Dataset;

-- 3. Total Profit
SELECT SUM(Profit) AS Total_Profit
FROM Customer_Insights_Dataset;

-- 4. Total Orders
SELECT COUNT(DISTINCT [Order ID]) AS Total_Orders
FROM Customer_Insights_Dataset;

-- 5. Average Order Value
SELECT AVG(Amount) AS Average_Order_Value
FROM Customer_Insights_Dataset;

-- 6. Top 10 Customers by Sales
SELECT CustomerName,
       SUM(Amount) AS Total_Sales
FROM Customer_Insights_Dataset
GROUP BY CustomerName
ORDER BY Total_Sales DESC
LIMIT 10;

-- 7. State-wise Sales
SELECT State,
       SUM(Amount) AS Sales
FROM Customer_Insights_Dataset
GROUP BY State
ORDER BY Sales DESC;

-- 8. Category-wise Sales
SELECT Category,
       SUM(Amount) AS Sales
FROM Customer_Insights_Dataset
GROUP BY Category;

-- 9. Category-wise Profit
SELECT Category,
       SUM(Profit) AS Profit
FROM Customer_Insights_Dataset
GROUP BY Category
ORDER BY Profit DESC;

-- 10. Top 10 Products
SELECT [Sub-Category],
       SUM(Amount) AS Sales
FROM Customer_Insights_Dataset
GROUP BY [Sub-Category]
ORDER BY Sales DESC
LIMIT 10;

-- 11. Payment Mode Analysis
SELECT PaymentMode,
       COUNT(*) AS Total_Orders,
       SUM(Amount) AS Sales
FROM Customer_Insights_Dataset
GROUP BY PaymentMode
ORDER BY Sales DESC;

-- 12. Monthly Sales
SELECT Month,
       SUM(Amount) AS Sales
FROM Customer_Insights_Dataset
GROUP BY Month
ORDER BY Sales DESC;

-- 13. Monthly Profit
SELECT Month,
       SUM(Profit) AS Profit
FROM Customer_Insights_Dataset
GROUP BY Month
ORDER BY Profit DESC;

-- 14. Average Profit by State
SELECT State,
       AVG(Profit) AS Avg_Profit
FROM Customer_Insights_Dataset
GROUP BY State
ORDER BY Avg_Profit DESC;

-- 15. Highest Selling State
SELECT State,
       SUM(Amount) AS Sales
FROM Customer_Insights_Dataset
GROUP BY State
ORDER BY Sales DESC
LIMIT 1;

-- 16. Customer Purchase Frequency
SELECT CustomerName,
       COUNT([Order ID]) AS Orders
FROM Customer_Insights_Dataset
GROUP BY CustomerName
ORDER BY Orders DESC;

-- 17. Profit Margin
SELECT
ROUND((SUM(Profit)/SUM(Amount))*100,2) AS Profit_Margin
FROM Customer_Insights_Dataset;

-- 18. High Value Orders
SELECT *
FROM Customer_Insights_Dataset
WHERE Amount > 10000;

-- 19. Loss Making Orders
SELECT *
FROM Customer_Insights_Dataset
WHERE Profit < 0;

-- 20. Customer Segmentation
SELECT CustomerName,
       SUM(Amount) AS TotalSpend,
CASE
WHEN SUM(Amount)>=15000 THEN 'High Value'
WHEN SUM(Amount)>=7000 THEN 'Medium Value'
ELSE 'Low Value'
END AS CustomerSegment
FROM Customer_Insights_Dataset
GROUP BY CustomerName
ORDER BY TotalSpend DESC;