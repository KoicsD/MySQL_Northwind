SELECT
	OrderID,
    ProductID,
    (
		SELECT ProductName FROM Products
        WHERE Products.ProductID = OrderDetails.ProductID
	) AS ProductName,
    UnitPrice,
    Quantity,
    Discount,
	Quantity * UnitPrice * (1 - Discount) AS Total
FROM OrderDetails;