__author__ = 'KoicsD'
from abstract_record import *


class Employee(Record):
    table_name = "Employees"
    fields = (("EmployeeID", int),
              ("LastName", str, Size(20), NotNull),
              ("FirstName", str, Size(10), NotNull),
              ("Title", str, Size(30)),
              ("TitleOfCourtesy", str, Size(25)),
              ("BirthDate", datetime),
              ("HireDate", datetime),
              ("Address", str, Size(60)),
              ("City", str, Size(15)),
              ("Region", str, Size(15)),
              ("PostalCode", str, Size(15)),
              ("Country", str, Size(15)),
              ("HomePhone", str, Size(24)),
              ("Extension", str, Size(4)),
              ("Photo", bytes),
              ("Notes", str, NotNull),
              ("ReportsTo", int),
              ("PhotoPath", str, Size(255)),
              ("Salary", float))
