## My Sample Files

Here are the content of directory [*SampleFiles*](SampleFiles/) eplained.

### *config*no*.json*:

These are sample configuration files.
Copy any of them into [ProjectRoot/*Resources*](Resources/),
change the appropriate fields of it
and rename it to *config.json*.
(If you don't want to move or rename them
you can give their path as an optional argument
when invoking [startup](startup.bat) from command line.)

### [*just_table_creation_from_mentors.sql*](SampleFiles/just_table_creation_from_mentors.sql):

This is the creational part of [*02_Northwind.MySQL5.sql*](Description/02_Northwind.MySQL5.sql)
-- the data-dumper script-file provided by mentors.

### [*table_creations_modified_for_csv.sql*](SampleFiles/table_creations_modified_for_csv.sql)

This is the modified version of the above file,
[*just_table_creation_from_mentors.sql*](SampleFiles/just_table_creation_from_mentors.sql).
The csv-files provided by mentors was incompatible with the database structure
described by their [data-dumper](Description/02_Northwind.MySQL5.sql) file.
This is the reason why I modified [creation-script](SampleFiles/just_table_creation_from_mentors.sql).

### xy*_sent.csv*

These files are the modified version of the csv-files provided by mentors.
As the original files contained lots of duplicate entries for primary key,
I had to edit them before sending them to database server.

Note:

In case of *Orders*,
you have to modify date-format from *%Y-%m-%d* to *%Y.%m.%d %H:%M*
in [*abstract_record.py*](PythonSource/abstract_record.py)
and you also have to insert a new field-tuple into [order.py](PythonSource/order.py)
when practicing with xy*_sent.csv* and xy*_received.csv*.
The name of field is *ContactTitle* and the type is string (*str*).
The modified version of order.py look like this:

```Python

class Order(Record):
    table_name = "Orders"
    fields = (("OrderID", int), ("CustomerID", str), ("EmployeeID", int), ("OrderDate", datetime),
              ("RequiredDate", datetime), ("ShippedDate", datetime), ("ShipVia", int), ("Freight", Decimal),
              ("ShipName", str), ("ShipAddress", str), ("ShipCity", str), ("ShipRegion", str), ("ShipPostalCode", str),
              ("ShipCountry", str), ("ContactTitle", str))  # here is the new field

```

And [*abstract_record.py*](PythonSource/abstract_record.py):

```Python
__author__ = 'KoicsD'
import mysql.connector as sql
from constraints import *
from datetime import datetime
from decimal import Decimal
from abc import ABCMeta
from warnings import warn

# date_format = "%Y-%m-%d"  # original
date_format = "%Y.%m.%d %H:%M"  # new version
data_display_limit = 100

```

As mentioned above, you also have to use
[*table_creations_modified_for_csv.sql*](SampleFiles/table_creations_modified_for_csv.sql)
instead of
[*just_table_creation_from_mentors.sql*](SampleFiles/just_table_creation_from_mentors.sql).
This is simply because mentors attached wrong csv-data to our task.

### xy*_received.csv*

These files contains the same data, as xy*_sent.csv*
but this is the version after regaining data from database server.

### xy*_from_mentors_sql*.csv

These files contains the data from database server
after running original creation and data-dumper script
[*02_Northwind.MySQL5.sql*](Description/02_Northwind.MySQL5.sql)
Note, that to reproduce this file, you don't have to modify
either [*order.py*](PythonSource/order.py)
or [*abstract_record.py*](PythonSource/abstract_record.py).

### xy*.py*

As you can see in [*PythonSource*](PythonSource/),
I've created some classes to describe single-field constraints
(ie. field-constraints that are independent from other fields) of data-tables.
They are located in module [*constraints*](PythonSource/constraints.py).
*.py*-files in directory [*SampleFiles*](SampleFiles/) are the examples how to use them.
Look at how constraints can be listed after each field-type.
If you use these files on such data that does not satisfy these constraints,
my app stops with an error.
You also can degrade these errors to warnings and let my app resuming
by starting it with command-line argument *default*.
Or you even can totally ignore constraints by argument *ignore*.
(This argument sets pythons built-in *warnings-filter action-level*.)

Note, that python-files in [*SampleFiles*](SampleFiles/)
are based on the sql-files privided by mentors, and not on their csv-flies.
(This means, these files accept data only if they are used with
[*just_table_creation_from_mentors.sql*](SampleFiles/just_table_creation_from_mentors.sql)
and xy*_from_mentors_sql.csv*.)

What is more, if you wish to define cross-field constraints,
you can esaly do it by overriding method *ensure_cross_field_constraints*
of abstract *Record* class (module [*abstract_record*](PythonSource/abstract_record.py))
in your own record-class:

```Python
from abstract_record import *


class OrderDetails(Record):
    table_name = "OrderDetails"
    fields = (
              # field names with types and self-constraints
             )
    
    def ensure_cross_field_constraints(self, field_name: str, value):
        problem_found = False
        # some checker logic
        if problem_found:
            # this is the correct syntax of signing the problem:
            warn("Some cross-field constraints were not satisfyed", ConstraintWarning)

```
See also the [official documentation of warning control](https://docs.python.org/3/library/warnings.html)