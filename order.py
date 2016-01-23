__author__ = 'KoicsD'
from record_template import *


class Order(Record):
    table_name = "Orders"
    fields = (("OrderID", int), ("CustomerID", str), ("EmployeeID", int), ("OrderDate", datetime),
              ("RequiredDate", datetime), ("ShippedDate", datetime), ("ShipVia", int), ("Freight", float),
              ("ShipName", str), ("ShipAddress", str), ("ShipCity", str), ("ShipRegion", str), ("ShipPostalCode", str),
              ("ShipCountry", str))
