__author__ = 'KoicsD'
from datetime import datetime


date_format = "%Y-%m-%d"
fields = ["OrderID", "CustomerID", "EmployeeID", "OrderDate", "RequiredDate", "ShippedDate", "ShipVia", "Freight",
          "ShipName", "ShipAddress", "ShipCity", "ShipRegion", "ShipPostalCode", "ShipCountry"]


cursor_obj = None


class Order:
    OrderID_type = int
    CustomerID_type = str
    EmployeeID_type = int
    OrderDate_type = datetime
    RequiredDate_type = datetime
    ShippedDate_type = datetime
    ShipVia_type = int
    Freight_type = int
    ShipName_type = str
    ShipAddress_type = str
    ShipCity_type = str
    ShipRegion_type = str
    ShipPostalCode_type = str
    ShipCountry_type = str

    def __init__(self):
        self.OrderID = None
        self.CustomerID = None
        self.EmployeeID = None
        self.OrderDate = None
        self.RequiredDate = None
        self.ShippedDate = None
        self.ShipVia = None
        self.Freight = None
        self.ShipName = None
        self.ShipAddress = None
        self.ShipCity = None
        self.ShipRegion = None
        self.ShipPostalCode = None
        self.ShipCountry = None

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
