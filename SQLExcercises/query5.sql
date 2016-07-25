SELECT
	YearOfIncome,
    CategoryName,
    ProductName,
    SUM(OrderTotal) AS ProductSales
FROM
	(
		SELECT
			YEAR(ShippedDate) AS YearOfIncome,
			(
				SELECT
					CategoryName
				FROM
					Categories
				WHERE
					Categories.CategoryID = Products.CategoryID
			)
			AS CategoryName,
			ProductName,
			(
				OrderDetails.UnitPrice * Quantity * (1 - Discount)
			)
			AS OrderTotal,
            OrderDetails.ProductID AS ProductID
		FROM
			Products
		JOIN
			OrderDetails
				ON Products.ProductID = OrderDetails.ProductID
		JOIN
			Orders
				ON OrderDetails.OrderID = Orders.OrderID
	)
    AS OrderSeparated
GROUP BY
	ProductID, YearOfIncome
ORDER BY
	ProductName, YearOfIncome;


/*SELECT
    Products.ProductName,
	-- Orders.CustomerID,
    OrderDetails.Quantity,
    Orders.ShippedDate
FROM
	Products
JOIN
	OrderDetails
		ON Products.ProductID = OrderDetails.ProductID
JOIN
	Orders
		ON OrderDetails.OrderID = Orders.OrderID;  -- returns NULL as ShippedDate

SELECT
    Products.ProductName,
	Orders.CustomerID,  -- here is the difference
    OrderDetails.Quantity,
    Orders.ShippedDate
FROM
	Products
JOIN
	OrderDetails
		ON Products.ProductID = OrderDetails.ProductID
JOIN
	Orders
		ON OrderDetails.OrderID = Orders.OrderID;  -- returns ShippedDate properly
-- WHY???!!!*/