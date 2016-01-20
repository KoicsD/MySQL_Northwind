__author__ = 'KoicsD'


fields = ["CustomerID", "CompanyName", "ContactName", "Address", "City", "Region", "PostalCode", "PostalCode",
          "Country", "Phone", "Fax"]


cursor_obj = None


class Customer:
    CustomerID_type = str
    CompanyName_type = str
    ContactName_type = str
    ContactTitle_type = str
    Address_type = str
    City_type = str
    Region_type = str
    PostalCode_type = str
    Country_type = str
    Phone_type = str
    Fax_type = str

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
