SELECT
	YEAR(ShippeDate) AS YearOfIncome,
	CategoryName,
	ProductName,
	SUM(OrderDetails.UnitPrice * Quantity * (1 - Discount)) AS Sales
FROM Categories
JOIN Products ON Categories.CategoryID = Products.CategoryID
JOIN OrderDetails ON Products.ProductID = OrderDetails.ProductID
JOIN Orders ON OrderDetails.OrderID = Orders.OrderID
ORDER BY ProductName, YearOfIncome;

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
