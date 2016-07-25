SELECT
	OrderID,
    (
		SELECT SUM(Quantity * UnitPrice * (1 - Discount))
        FROM OrderDetails
        WHERE OrderDetails.OrderID = Orders.OrderID
    )
    AS Total
FROM Orders
ORDER BY OrderID;