__author__ = 'KoicsD'
from record_template import *


class OrderDetail(Record):
    table_name = "OrderDetails"
    fields = (("OrderID", int), ("ProductID", int), ("UnitPrice", int), ("Quantity", int), ("Discount", float))
