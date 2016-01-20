__author__ = 'KoicsD'


fields = ["OrderID", "ProductID", "UnitPrice", "Quantity", "Discount"]


cursor_obj = None


class OrderDetail:
    OrderID_type = int
    ProductID_type = int
    UnitPrice_type = int
    Quantity_type = int
    Discount_type = float

    def __init__(self):
        self.OrderID = 0
        self.ProductID = 0
        self.UnitPrice = 0
        self.Quantity = 0
        self.Discount = 0.0

    @classmethod
    def parse(cls, csv_row: dict):
        new_obj = cls()
        return new_obj

    def persist(self):
        global cursor_obj
        pass

    def to_csv(self):
        pass

    @classmethod
    def compose(cls):
        pass

    @classmethod
    def select(cls):
        global cursor_obj
        pass
