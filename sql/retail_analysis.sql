-- Drop null records
DELETE FROM retail_data
WHERE Category IS NULL OR SubCategory IS NULL OR UnitPrice IS NULL OR UnitCost IS NULL;

-- Add a Profit column if not already added
ALTER TABLE retail_data ADD COLUMN Profit FLOAT;

-- Update Profit = (Selling Price - Cost Price) * Units Sold
UPDATE retail_data
SET Profit = (UnitPrice - UnitCost) * UnitsSold;

-- Profit margins by Category and SubCategory
SELECT 
  Category,
  SubCategory,
  SUM(Profit) AS TotalProfit,
  ROUND(AVG((UnitPrice - UnitCost) / NULLIF(UnitPrice, 0)), 2) AS AvgProfitMargin
FROM retail_data
GROUP BY Category, SubCategory
ORDER BY TotalProfit ASC;

-- Average inventory days
SELECT 
  Category,
  SubCategory,
  AVG(InventoryDays) AS AvgInventoryDays
FROM retail_data
GROUP BY Category, SubCategory;
