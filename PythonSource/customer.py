__author__ = 'KoicsD'
from abstract_record import *


class Customer(Record):
    table_name = "Customers"
    fields = (("CustomerID", str), ("CompanyName", str), ("ContactName", str), ("ContactTitle", str), ("Address", str),
              ("City", str), ("Region", str), ("PostalCode", str), ("Country", str), ("Phone", str), ("Fax", str))
