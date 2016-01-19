__author__ = 'KoicsD'


class Employee:
    def __init__(self):
        self.EmployeeID = 0
        self.LastName = ""
        self.FirstName = ""
        self.Title = ""
        self.TitleOfCourtesy = ""
        self.BirthDate = None  # datetime
        self.HireDate = None  # datetime
        self.Address = ""
        self.City = ""
        self.Region = ""
        self.PostalCode = ""
        self.Country = ""
        self.HomePhone = ""
        self.Extension = ""
        self.Photo = None  # longblob
        self.Notes = ""
        self.ReportsTo = 0
        self.PhotoPath = ""
        self.Salary = 0.0

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
