SELECT
	City,
    CompanyName,
    ContactName,
    'Customer' AS RelationShip
FROM Customers
UNION
SELECT
	City,
    CompanyName,
    ContactName,
    'Supplier' AS RelationShip
FROM Suppliers
ORDER BY City, ContactName;