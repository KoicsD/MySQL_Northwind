__author__ = 'KoicsD'
from abstract_record import *


class Employee(Record):
    table_name = "Employees"
    fields = (("EmployeeID", int), ("LastName", str), ("FirstName", str), ("Title", str), ("TitleOfCourtesy", str),
              ("BirthDate", datetime), ("HireDate", datetime), ("Address", str), ("City", str), ("Region", str),
              ("PostalCode", str), ("Country", str), ("HomePhone", str), ("Extension", str), ("Photo", bytes),
              ("Notes", str), ("ReportsTo", int), ("PhotoPath", str), ("Salary", float))
