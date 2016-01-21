/*SELECT
	YearOfINcome,
    CategoryName,
    ProductName,
    ProductSales
FROM
	Products
JOIN
	OrderDetails
		ON Products.ProductID = OrderDetails.ProductID
JOIN
	Orders
		ON OrderDetails.OrderID = Orders.OrderID;*/

SELECT
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
-- WHY???!!!