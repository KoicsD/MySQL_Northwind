__author__ = 'KoicsD'
from abstract_record import *
from decimal import Decimal


class OrderDetail(Record):
    table_name = "OrderDetails"
    fields = (("OrderID", int), ("ProductID", int), ("UnitPrice", Decimal), ("Quantity", int), ("Discount", float))
