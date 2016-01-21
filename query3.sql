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
	Customers.CompanyName AS CustomerName, -- the name of the customer's company
	Address,
	City,
	Region,
	PostalCode,
	Country,
    -- exception:
	-- Salesperson, -- the fullname of the employee separated by space
    -- from Customers again
	Orders.OrderID AS OrderID,
	OrderDate,
	RequiredDate,
	ShippedDate,
    -- from Shippers:
	-- ShipperName,
    -- from OrderDetails:
	ProductID,
	-- ProductName, -- exception
	UnitPrice,
	Quantity,
	Discount
	-- Total -- see previous query (more detailed orders)
	-- WTF?:
    -- Freight
FROM Customers
	JOIN Orders
		ON Customers.CustomerID = Orders.CustomerID
	JOIN OrderDetails
		ON Orders.OrderID = OrderDetails.OrderID;
