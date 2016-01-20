__author__ = 'KoicsD'
from datetime import datetime


date_format = "%Y-%m-%d"


class Employee:
    EmployeeID_type = int
    LastName_type = str
    FirstName_type = str
    Title_type = str
    TitleOfCourtesy_type = str
    BirthDate_type = str
    HireDate_type = datetime
    Address_type = str
    City_type = str
    Region_type = str
    PostalCode_type = str
    Country_type = str
    HomePhone_type = str
    Extension_type = str
    Photo_type = str
    Notes_type = str
    ReportsTo_type = int
    PhotoPath_type = str
    Salary_type = float

    def __init__(self):
        self.EmployeeID = None
        self.LastName = None
        self.FirstName = None
        self.Title = None
        self.TitleOfCourtesy = None
        self.BirthDate = None
        self.HireDate = None
        self.Address = None
        self.City = None
        self.Region = None
        self.PostalCode = None
        self.Country = None
        self.HomePhone = None
        self.Extension = None
        self.Photo = None
        self.Notes = None
        self.ReportsTo = None
        self.PhotoPath = None
        self.Salary = None

    @classmethod
    def parse(cls, csv_row: dict):
        new_obj = cls()
        for key, value in csv_row.items():
            type_of_attr = getattr(cls, key + "_type")
            if value != "NULL":
                if type_of_attr == datetime:
                    parsed_value = datetime.strptime(value, date_format)
                else:
                    parsed_value = type_of_attr(value)
                setattr(new_obj, key, parsed_value)
        return new_obj

    def persist(self, cursor_obj):
        pass

    def to_csv(self):
        pass

    @classmethod
    def select(cls):
        pass
