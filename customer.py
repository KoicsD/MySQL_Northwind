__author__ = 'KoicsD'


class Customer:
    def __init__(self):
        self.CustomerID = ""
        self.CompanyName = ""
        self.ContactName = ""
        self.ContactTitle = ""
        self.Address = ""
        self.City = ""
        self.Region = ""
        self.PostalCode = ""
        self.Country = ""
        self.Phone = ""
        self.Fax = ""

    @classmethod
    def parse(cls, csv_row: str):
        pass

    def persist(self, cursor_obj):
        pass

    def to_csv(self):
        pass

    @classmethod
    def select(self):
        pass
