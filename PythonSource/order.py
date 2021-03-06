__author__ = 'KoicsD'
from abstract_record import *


class Order(Record):
    table_name = "Orders"
    fields = (("OrderID", int), ("CustomerID", str), ("EmployeeID", int), ("OrderDate", datetime),
              ("RequiredDate", datetime), ("ShippedDate", datetime), ("ShipVia", int), ("Freight", Decimal),
              ("ShipName", str), ("ShipAddress", str), ("ShipCity", str), ("ShipRegion", str), ("ShipPostalCode", str),
              ("ShipCountry", str))
