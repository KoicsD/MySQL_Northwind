SELECT
	/*YearOfINcome,
    CategoryName,
    ProductName,
    ProductSales*/
    ProductName,
    -- CustomerID,
    Quantity,
    ShippedDate
FROM
	Products
JOIN
	OrderDetails
		ON Products.ProductID = OrderDetails.ProductID
JOIN
	Orders
		ON OrderDetails.ProductID;