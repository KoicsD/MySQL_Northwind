SELECT
	-- from Orders:
	ShipName,
	ShipAddress,
	ShipCity,
	ShipRegion,
	ShipPostalCode,
	ShipCountry,
	Orders.CustomerID AS CustomerID,
    -- from Customers:
	CompanyName AS CustomerName, -- the name of the customer's company
	Address,
	City,
	Region,
	PostalCode,
	Country,
    -- from Orders:
	(
		SELECT
			CONCAT(FirstName, ' ', LastName)
		FROM
			Employees
		WHERE
			Employees.EmployeeID = Orders.EmployeeID
    )
		AS Salesperson, -- the fullname of the employee separated by space (from Employees)
	Orders.OrderID AS OrderID,
	OrderDate,
	RequiredDate,
	ShippedDate,
	(
		SELECT
			CompanyName
		FROM
			Shippers
		WHERE
			Shippers.ShipperID = Orders.ShipVia
    )
		AS ShipperName, -- from Shippers
    -- from OrderDetails:
	ProductID,
    (
		SELECT
			ProductName
		FROM
			Products
		WHERE
			Products.ProductID = OrderDetails.ProductID
    )
		AS ProductName, -- from Products
	UnitPrice,
	Quantity,
	Discount,
	(
		UnitPrice * Quantity * (1 - Discount)
    )
		AS Total, -- see previous query (more detailed orders)
    -- from Orders:
    Freight
FROM Customers
	JOIN Orders
		ON Customers.CustomerID = Orders.CustomerID
	JOIN OrderDetails
		ON Orders.OrderID = OrderDetails.OrderID
ORDER BY
	Customers.CustomerID;