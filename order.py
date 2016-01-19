__author__ = 'KoicsD'


class Order:
    def __init__(self):
        self.OrderID = 0
        self.CustomerID = ""
        self.EmployeeID = 0
        self.OrderDate = None  # datetime
        self.RequiredDate = None  # datetime
        self.ShippedDate = None  # datetime
        self.ShipVia = 0
        self.Freight = 0
        self.ShipName = ""
        self.ShipAddress = ""
        self.ShipCity = ""
        self.ShipRegion = ""
        self.ShipPostalCode = ""
        self.ShipCountry = ""

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
