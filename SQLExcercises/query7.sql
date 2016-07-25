SELECT
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
    QuantityPerUnit,
    UnitsInStock
FROM
	Products
WHERE
	Discontinued != 1
ORDER BY
	CategoryName,
    ProductName;