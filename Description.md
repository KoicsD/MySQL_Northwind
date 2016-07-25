# Task description

---------------

---------------

## Setup sample DB

There is a given database schema named Northwind. You can read an article which explains it here:  
https://theaccessbuddy.wordpress.com/2011/07/03/northwind-database-explained/  
You can find the relational model and the creational scripts below. Before you start to work on the weekly exercises please run these scripts on your machine to create the DB what you will work with.  
Connect to your localhost db as an admin  
Execute [01_Northwind.MySQL5_create_database.sql](Description/01_Northwind.MySQL5_create_database.sql)  
Execute [02_Northwind.MySQL5.sql](Description/02_Northwind.MySQL5.sql)  
Execute [03_Northwind_users_creation_and_grant_access.sql](Description/03_Northwind_users_creation_and_grant_access.sql)  
After this please tries to explore a DB structure and the data it contains. What kind of relationship are between the different tables. On this DB you can practice and repeat the basic SQL queries what you learnt. In the afternoon it will help us to summerize what you learnt about the SQL so far.

![](Description/remote_northwind.png)

-----------

tags:
[DBMS](https://en.wikipedia.org/wiki/Database)
[SQL](https://en.wikipedia.org/wiki/SQL)

------------------

------------------

## ORM

Your task is to do the followings:  
We would like to represent the database content as objects in an object oriented language like the python. [Object-relational mapping](https://en.wikipedia.org/wiki/Object-relational_mapping) (ORM) is a technique (a.k.a. design pattern) of accessing a relational database from an object-oriented language (Java, python for example).  
Application:  
GitHub repository is needed.  
Test are not mandatory.  
Create a python application which can import data from a CSV file, parses the containing data to objects and stores the data in MySQL database. The application has to be able to export data from database to CSV file. The application uses the previusly created NorthwindDB. Import and export functions are limited to use these tables: Employees, Customers, Orders and OrderDetails so you don't need to create a class for every tables in the DB !  
All of the classes should contain a static parse() method which require a string as a parameter (CSV row) and creates (and returns) an object from it.  
The classes should contain a persist() method (procedure) with no parameter.  
Define a to_csv() method which returns a string representation of the current object which can be written out as a CSV row.  
OPTIONAL: Define a function (in every class), called select(), which generates and runs a basic SQL select operation. The method gets a string parameter where you can define which field you want to be selected, a named boolean parameter, called distinct (default False) which means if the selected field should be distinct and a named string parameter where, which means if you want your result to be filtered with the given conditions.  
OPTIONAL: Create a basic menu where user can use the features above.  
E.g.  
Import from CSV : Sub-menu > Employees, Customers, Orders, Orders and details  
Export to CSV : Sub-menu > Employees, Customers, Orders, Orders and details  
List table : Sub-menu > Employees, Customers, Orders, Orders and details  

--------

Attachments:  
[customers.csv](Description/customers.csv)  
[employees.csv](Description/employees.csv)  
[order_details.csv](Description/order_details.csv)  
[orders.csv](Description/orders.csv)  

--------

Tags:
[DBMS](https://en.wikipedia.org/wiki/Database)
[OOP](https://en.wikipedia.org/wiki/Object-oriented_programming)
[*python*](https://en.wikipedia.org/wiki/Python_(programming_language))
[SQL](https://en.wikipedia.org/wiki/SQL)

----------

----------

## Queries for Northwind

Today task is to write some queries for the Northwind database.
If you stuck with a query try to get some help.
If that particular SELECT statement is so stubborn just go to next one.
Maybe later you can solve it.

You will get a Java application wich can validate the query you wrote.
It has a simple help menu but if you need help just contact the mentors.

Your SQL files need to named like this:  
    *"query{number}.sql"*  
where {number} is the number of the given query.

Be aware of the ordering and the requested columns!

-------

{1} Write a query which shows the orders more detailed.

It should contain:
* OrderID
* ProductID
* ProductName: name of the ordered product
* UnitPrice
* Quantity
* Discount
* Total: total price to be paid calculated by unit price, quantity and discount

The list should sort by OrderID.

-------

{2} Write a query which shows the customers and suppliers in single result.

It should contain the columns listed below:
* City
* CompanyName
* ContactName
* Relationship: 'Customer' or 'Supplier'

The result should be sorted by City and ContactName.

HINT: use UNION

-----

{3} There is a recurring request from the customers especially create invoices for them.
So we need to prodive the necessary information.

Write a query which shows all the necessary data for an invoice.
* ShipName:
* ShipAddress:
* ShipCity:
* ShipRegion: 
* ShipPostalCode:
* ShipCountry:
* CustomerID:
* CustomerName: the name of the customer's company
* Address:
* City:
* Region:
* PostalCode:
* Country:
* Salesperson: the fullname of the employee separated by space
* OrderID:
* OrderDate:
* RequiredDate:
* ShippedDate: 
* ShipperName:
* ProductID:
* ProductName: 
* UnitPrice:
* Quantity:
* Discount: 
* Total: see previous query (more detailed orders)
* Freight:

The list should be sorted by CustomerID.

-----

{4} Write a query which lists the total amount to be paid for the different orders.

The result set should contains only two column
* OrderID
* OrderTotal: sum of orderdetails' total

It should be sorted by OrderID.

-----

{5} Write a query that lists total amount of the particular products' sales for each year.

Columns should be listed:
* YearOfIncome: the year when the product was shipped
* CategoryName
* ProductName
* ProductSales: sum of ordertotals

The list should be sorted by ProductName and year.

-----

{6} Write a query which lists all the expensive products.

All product is expensive which price is higher than the average.

* ProductName
* UnitPrice

It should be sorted by UnitPrice.

-----

{7} I would like to see a list with all the products which still are on the market.
Write query which returns the correct result for this.

The result should contain the columns below:
* CategoryName: category of the product
* ProductName
* QuantityPerUnit
* UnitsInStock

The list should be sorted by CategoryName and ProductName.

-----

{8} Write a query which shows the cheapest products on the market by category.

The result should contain:
* CategoryName
* CheapestProduct: name of the cheapest product in that category
* MinCategoryPrice: unit price of the product

It should be sorted by CategoryName.

-----

Attachments:
[*DBCooler.jar*](Description/DBCooler.jar)

-----

tags:
[DBMS](https://en.wikipedia.org/wiki/Database)
[SQL](https://en.wikipedia.org/wiki/SQL)
