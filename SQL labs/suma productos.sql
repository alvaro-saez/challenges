SELECT   p.name, COUNT(*) AS 'Total Orders'
FROM SalesLT.Product AS p
    INNER JOIN SalesLT.SalesOrderDetail AS sod ON p.ProductID = sod.ProductID
GROUP BY  p.Name
ORDER BY 'Total Orders' DESC