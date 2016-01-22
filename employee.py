__author__ = 'KoicsD'
from datetime import datetime


date_format = "%Y-%m-%d"


cursor_obj = None


class Employee:
    fields = (("EmployeeID", int), ("LastName", str), ("FirstName", str), ("Title", str), ("TitleOfCourtesy", str),
              ("BirthDate", datetime), ("HireDate", datetime), ("Address", str), ("City", str), ("Region", str),
              ("PostalCode", str), ("Country", str), ("HomePhone", str), ("Extension", str), ("Photo", str),
              ("Notes", str), ("ReportsTo", int), ("PhotoPath", str), ("Salary", float))

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

    @classmethod
    def get_fields(cls):
        return [f for f, t in cls.fields]

    @classmethod
    def get_type(cls, field_name: str):
        for f, t in cls.fields:
            if f == field_name:
                return t

    def __init__(self):
        for field in self.get_fields():
            setattr(self, field, None)

    @classmethod
    def parse(cls, csv_row: dict):
        new_obj = cls()
        for key, value in csv_row.items():
            type_of_attr = cls.get_type(key)
            if value != "NULL":
                if type_of_attr == datetime:
                    parsed_value = datetime.strptime(value, date_format)
                else:
                    parsed_value = type_of_attr(value)
                setattr(new_obj, key, parsed_value)
        return new_obj

    def persist(self):
        global cursor_obj
        not_null_fields = []
        values = []
        for field in self.get_fields():
            current_value = getattr(self, field)
            if current_value is not None:
                not_null_fields.append(field)
                values.append(current_value)
        command = "INSERT INTO Employees (" +\
                  ", ".join(not_null_fields) +\
                  ") VALUES (" +\
                  ", ".join(["%s"] * len(values)) + ")"
        cursor_obj.execute(command, tuple(values))

    def to_csv(self):
        new_dict = {}
        for field in self.get_fields():
            value = getattr(self, field)
            if value is None:
                new_dict[field] = "NULL"
            elif type(value) is datetime:
                new_dict[field] = value.strftime(date_format)
            else:
                new_dict[field] = str(value)
        return new_dict

    @classmethod
    def compose(cls, values: tuple):
        new_obj = cls()
        field_names = cls.get_fields()
        for i in range(len(field_names)):
            setattr(new_obj, field_names[i], values[i])
        return new_obj

    @classmethod
    def select(cls):
        global cursor_obj
        querry = "SELECT " + ", ".join(cls.get_fields()) + " FROM Employees"
        cursor_obj.execute(querry)
        new_objects = []
        for record in cursor_obj:
            new_objects.append(cls.compose(record))
        return new_objects

