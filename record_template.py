__author__ = 'KoicsD'
import mysql.connector as sql
from datetime import datetime

date_format = "%Y-%m-%d"

cursor_obj = None


class Record:
    table_name = ""
    fields = ()

    @classmethod
    def get_field_names(cls):
        return [f for f, t in cls.fields]

    @classmethod
    def get_field_type(cls, field_name: str):
        for f, t in cls.fields:
            if f == field_name:
                return t

    def __init__(self):
        for field_name in self.get_field_names():
            setattr(self, "_field_" + field_name, None)

    @classmethod
    def from_dict(cls, a_dict: dict):
        new_obj = cls()
        for key, value in a_dict.items():
            type_of_attr = cls.get_field_type(key)
            if type_of_attr is None:
                raise KeyError("Unknown field '" + key + "' for record-type '" + cls.__name__ + "'")
            if value != "NULL":
                if type_of_attr == datetime:
                    parsed_value = datetime.strptime(value, date_format)
                else:
                    parsed_value = type_of_attr(value)
                setattr(new_obj, "_field_" + key, parsed_value)
        return new_obj

    def persist(self):
        global cursor_obj
        field_names = []
        values = []
        for field_name in self.get_field_names():
            current_value = getattr(self, "_field_" + field_name)
            if current_value is not None:
                field_names.append(field_name)
                values.append(current_value)
        command = "INSERT INTO " + self.table_name + " (" +\
                  ", ".join(field_names) +\
                  ") VALUES (" +\
                  ", ".join(["%s"] * len(values)) + ")"
        try:
            cursor_obj.execute(command, tuple(values))
        except sql.Error as err:
            raise RuntimeError("An SQL-Error was raised when inserting into table '" + self.table_name + "'\n" +
                               "Command:\n" + command + "\n" + "Values:\n" + str(values)) from err

    def to_dict(self):
        new_dict = {}
        for field_name in self.get_field_names():
            value = getattr(self, "_field_" + field_name)
            if value is None:
                new_dict[field_name] = "NULL"
            elif type(value) is datetime:
                new_dict[field_name] = value.strftime(date_format)
            else:
                new_dict[field_name] = str(value)
        return new_dict

    @classmethod
    def __from_tuple(cls, values: tuple):
        new_obj = cls()
        field_names = cls.get_field_names()
        if len(field_names) != len(values):
            raise TypeError("Inappropriate number of arguments for composing '" + cls.__name__ + "' record-object\n" +
                            "Expected: " + str(len(field_names)) + ", Actual: " + str(len(values)))
        for i in range(len(field_names)):
            if values[i] is not None and type(values[i]) != cls.get_field_type(field_names[i]):
                raise TypeError("Inappropriate type of " + str(i) + "th argument (of " + str(len(field_names)) +
                                ") for composing '" + cls.__name__ + "' record-object\n" +
                                "Expected: " + str(cls.get_field_type(field_names[i])) +
                                ", Actual: " + str(type(values[i])) +
                                ", Name of field: " + field_names[i])
            setattr(new_obj, "_field_" + field_names[i], values[i])
        return new_obj

    @classmethod
    def select(cls):
        global cursor_obj
        query = "SELECT " + ", ".join(cls.get_field_names()) + " FROM " + cls.table_name
        record = None
        try:
            cursor_obj.execute(query)
            new_objects = []
            for record in cursor_obj:
                new_objects.append(cls.__from_tuple(record))
            return new_objects
        except sql.Error as sql_err:
            raise RuntimeError("An SQL-Error was raised when selecting from table '" + cls.table_name + "'\n" +
                               "Command:\n" + query) from sql_err
        except Exception as err:
            if record is not None:
                raise RuntimeError("An Exception was raised during restoring '" + cls.__name__ +
                                   "' object from database\n" + "Query:\n'" + query + "'\n" +
                                   "Raw response:\n" + str(record)) from err
            else:
                raise
