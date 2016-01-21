SELECT
	*
FROM
	(
		SELECT
			CategoryName,
			ProductName,
			UnitPrice
		FROM
			Categories
		NATURAL JOIN
			Products
		ORDER BY
			CategoryName
	)
		AS Joint;