## My Sample Files

Here are the content of directory [SampleFiles](SampleFiles/) eplained.

### config*.json:

These are sample configuration files.
Copy any of them into [ProjectRoot/Resources](Resources/),
change the appropriate fields of it
and rename it to *config.json*.
(If you don't want to move or rename them
you can give their path as an optional argument
when invoking [startup](startup.bat) from command line.)

### [just_table_creation_from_mentors.sql](SampleFiles/just_table_creation_from_mentors.sql):

This is the creational part of [02_Northwind.MySQL5.sql](Description/02_Northwind.MySQL5.sql)
-- the data-dumper script-file provided by mentors.

### [table_creations_modified_for_csv.sql](SampleFiles/table_creations_modified_for_csv.sql)

This is the modified version of the above file,
[just_table_creation_from_mentors.sql](SampleFiles/just_table_creation_from_mentors.sql).
The csv-files provided by mentors was incompatible with the database structure
described by their [data-dumper](Description/02_Northwind.MySQL5.sql) file.
This is the reason why I modified [creation-script](SampleFiles/just_table_creation_from_mentors.sql).

### *_sent.csv

These files are the modified version of the csv-files provided by mentors.
As the original files contained lots of duplicate entries for primary key,
I had to edit them before sending them to database server.

Note:

In case of *Orders*,
you have to modify date-format from *%Y-%m-%d* to *%Y.%m.%d %H:%M*
in [abstract_record.py](PythonSource/abstract_record.py)
and you also have to insert a new field-tuple into [order.py](PythonSource/order.py)
when practicing with *_sent.csv and *_received.csv.
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

And [abstract_record.py](PythonSource/abstract_record.py):

```Python
__author__ = 'KoicsD'
import mysql.connector as sql
from datetime import datetime

# date_format = "%Y-%m-%d"  # original
date_format = "%Y.%m.%d %H:%M"  # new version

```

As mentioned above, you also have to use
[table_creations_modified_for_csv.sql](SampleFiles/table_creations_modified_for_csv.sql)
instead of
[just_table_creation_from_mentors.sql](SampleFiles/just_table_creation_from_mentors.sql).
This is simply because mentors attached wrong csv-data to our task.

### *_received.csv

These files contains the same data, as *_sent.csv
but this is the version after regaining data from database server.

### *_from_mentors_sql.csv

These files contains the data from database server
after running original creation and data-dumper script
[02_Northwind.MySQL5.sql](Description/02_Northwind.MySQL5.sql)
Note, that to reproduce this file, you don't have to modify
either [order.py](PythonSource/order.py)
or [abstract_record.py](PythonSource/abstract_record.py).
