__author__ = 'KoicsD'


class OrderDetail:
    def __init__(self):
        self.OrderID = 0
        self.ProductID = 0
        self.UnitPrice = 0
        self.Quantity = 0
        self.Discount = 0.0

    @classmethod
    def parse(cls, csv_row: str):
        pass

    def persist(self, cursor_obj):
        pass

    def to_csv(self):
        pass

    @classmethod
    def select(cls):
        pass
