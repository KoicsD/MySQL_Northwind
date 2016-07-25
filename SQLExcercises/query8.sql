SELECT
	(
		SELECT
			CategoryName
        FROM
			Categories
		WHERE
			Categories.CategoryID = o.CategoryID
    )
		AS CategoryName,
    ProductName AS CheapestProduct,
    UnitPrice AS MinCategoryPrice
FROM
	Products as o
WHERE
	UnitPrice = (
					SELECT
						MIN(UnitPrice)
					FROM
						Products AS i
					WHERE
						i.CategoryID = o.CategoryID
                )
ORDER BY
	CategoryName;