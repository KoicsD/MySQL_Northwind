__author__ = 'KoicsD'
from abstract_record import *


class Customer(Record):
    table_name = "Customers"
    fields = (("CustomerID", str, Size(5), NotNull),
              ("CompanyName", str, Size(40), NotNull),
              ("ContactName", str, Size(30)),
              ("ContactTitle", str, Size(30)),
              ("Address", str, Size(60)),
              ("City", str, Size(15)),
              ("Region", str, Size(15)),
              ("PostalCode", str, Size(10)),
              ("Country", str, Size(15)),
              ("Phone", str, Size(24)),
              ("Fax", str, Size(24)))
