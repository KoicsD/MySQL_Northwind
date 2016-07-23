__author__ = 'KoicsD'
import mysql.connector as sql
from datetime import datetime

date_format = "%Y-%m-%d"

cursor_obj = None


class Record:
    table_name = ""
    fields = ()

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
            if type_of_attr is None:
                raise KeyError("Unknown field '" + key + "' for record-type '" + cls.__name__ + "'")
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
        command = "INSERT INTO " + self.table_name + " (" +\
                  ", ".join(not_null_fields) +\
                  ") VALUES (" +\
                  ", ".join(["%s"] * len(values)) + ")"
        try:
            cursor_obj.execute(command, tuple(values))
        except sql.Error as err:
            raise RuntimeError("An SQL-Error was raised when inserting into table '" + self.table_name + "'\n" +
                               "Command:\n" + command + "\n" + "Values:\n" + str(values)) from err

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
        if len(field_names) != len(values):
            raise TypeError("Inappropriate number of arguments for composing '" + cls.__name__ + "' record-object")
        for i in range(len(field_names)):
            if type(values[i]) != cls.get_type(field_names[i]):
                raise TypeError("Inappropriate type of argument for composing '" + cls.__name__ + "' record-object")
            setattr(new_obj, field_names[i], values[i])
        return new_obj

    @classmethod
    def select(cls):
        global cursor_obj
        query = "SELECT " + ", ".join(cls.get_fields()) + " FROM " + cls.table_name
        try:
            cursor_obj.execute(query)
            new_objects = []
            for record in cursor_obj:
                new_objects.append(cls.compose(record))
            return new_objects
        except sql.Error as sql_err:
            raise RuntimeError("An SQL-Error was raised when selecting from table '" + cls.table_name + "'\n" +
                               "Command:\n" + query) from sql_err
        except Exception as err:
            if record is not None:
                raise RuntimeError("An Exception was raised during restoring '" + cls.__name__ +
                                   "' object from database\n" + "Raw data:\n" + str(record)) from err
            else:
                raise
