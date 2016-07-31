__author__ = 'KoicsD'
from abstract_record import *


class Order(Record):
    table_name = "Orders"
    fields = (("OrderID", int),
              ("CustomerID", str, Size(5)),
              ("EmployeeID", int),
              ("OrderDate", datetime),
              ("RequiredDate", datetime),
              ("ShippedDate", datetime),
              ("ShipVia", int),
              ("Freight", Decimal),
              ("ShipName", str, Size(40)),
              ("ShipAddress", str, Size(60)),
              ("ShipCity", str, Size(15)),
              ("ShipRegion", str, Size(15)),
              ("ShipPostalCode", str, Size(10)),
              ("ShipCountry", str, Size(15)))
