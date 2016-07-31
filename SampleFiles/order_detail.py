__author__ = 'KoicsD'
from abstract_record import *
from decimal import Decimal


class OrderDetail(Record):
    table_name = "OrderDetails"
    fields = (("OrderID", int, NotNull),
              ("ProductID", int, NotNull),
              ("UnitPrice", Decimal),
              ("Quantity", int),
              ("Discount", float))
