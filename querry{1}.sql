SELECT
	OrderID,
    ProductID,
    (
		SELECT ProductName FROM Products
        WHERE products.ProductID = orderdetails.ProductID
	) AS ProductName,
    UnitPrice,
    Quantity,
    Discount,
	Quantity * UnitPrice * (1 - Discount) AS Total
FROM OrderDetails;