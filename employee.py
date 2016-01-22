__author__ = 'KoicsD'
from record_template import *


class Employee(Record):
    fields = (("EmployeeID", int), ("LastName", str), ("FirstName", str), ("Title", str), ("TitleOfCourtesy", str),
              ("BirthDate", datetime), ("HireDate", datetime), ("Address", str), ("City", str), ("Region", str),
              ("PostalCode", str), ("Country", str), ("HomePhone", str), ("Extension", str), ("Photo", str),
              ("Notes", str), ("ReportsTo", int), ("PhotoPath", str), ("Salary", float))
