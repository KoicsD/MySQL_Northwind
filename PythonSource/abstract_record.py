__author__ = 'KoicsD'
import mysql.connector as sql
from constraints import *
from datetime import datetime
from decimal import Decimal
from abc import ABCMeta
from warnings import warn

date_format = "%Y-%m-%d"
data_display_limit = 500

cursor_obj = None


def bytes_to_hex(bts: bytes):
    hex_str = ""
    for byte_as_int in bts:
        byte_as_hex_str = hex(byte_as_int)[2:]  # hex-format strings always start with '0x' -- let's drop it
        if len(byte_as_hex_str) == 1:
            byte_as_hex_str = "0" + byte_as_hex_str
        hex_str += byte_as_hex_str + " "
    return hex_str[:-1]  # last space is ugly


class Record(metaclass=ABCMeta):
    # fields to be overridden:
    table_name = ""
    fields = ()

    # some auxiliary functions:
    @classmethod
    def get_field_names(cls):
        return [field[0] for field in cls.fields]

    @classmethod
    def get_field_type(cls, field_name: str):
        for field_info in cls.fields:
            f, t = field_info[0:2]
            if f == field_name:
                return t
        raise AttributeError("Unknown field '" + field_name + "' for record-type '" + cls.__name__ + "'")

    @classmethod
    def get_field_constraints(cls, field_name):
        for field in cls.fields:
            f, t = field[0:2]
            constraints = field[2:]
            if f == field_name:
                return constraints
        raise AttributeError("Unknown field '" + field_name + "' for record-type '" + cls.__name__ + "'")

    # initializer, getter, setter:
    def __init__(self):
        for field_name in self.get_field_names():
            setattr(self, "_field_" + field_name, None)

    def get_field(self, field_name: str):
        if field_name not in self.get_field_names():
            raise AttributeError("Unknown field '" + field_name + "' for record-type '" + type(self).__name__ + "'")
        return getattr(self, "_field_" + field_name)

    def set_field(self, field_name: str, value):
        expected_type = self.get_field_type(field_name)
        actual_type = type(value)
        if actual_type != expected_type:
            raise TypeError("Inappropriate type for field '" + field_name +
                            "' of record-type '" + type(self).__name__ + "'\n" +
                            "Expected: " + expected_type + ", Actual: " + actual_type.__name__)
        self.__ensure_single_field_constraints(field_name, value)
        self.ensure_cross_field_constraints(field_name, value)
        setattr(self, "_field_" + field_name, value)

    # from dictionary, to dictionary:
    @classmethod
    def from_dict(cls, a_dict: dict):
        new_obj = cls()
        for key, value in a_dict.items():
            type_of_attr = cls.get_field_type(key)
            if type_of_attr is None:
                raise AttributeError("Unknown field '" + key + "' for record-type '" + cls.__name__ + "'")
            if value != "NULL":
                if type_of_attr == datetime:
                    parsed_value = datetime.strptime(value, date_format)
                elif type_of_attr == bytes:
                    parsed_value = bytes.fromhex(value)
                else:
                    parsed_value = type_of_attr(value)
                cls.__ensure_single_field_constraints(key, parsed_value)
                new_obj.ensure_cross_field_constraints(key, parsed_value)
                setattr(new_obj, "_field_" + key, parsed_value)
        return new_obj

    def to_dict(self):
        new_dict = {}
        for field_name in self.get_field_names():
            value = getattr(self, "_field_" + field_name)
            if value is None:
                new_dict[field_name] = "NULL"
            elif type(value) == datetime:
                new_dict[field_name] = value.strftime(date_format)
            elif type(value) == bytes:
                # new_dict[field_name] = value.hex()  # only from python 3.5
                new_dict[field_name] = bytes_to_hex(value)
            else:
                new_dict[field_name] = str(value)
        return new_dict

    # from database, to database:
    @classmethod
    def __from_tuple(cls, values: tuple):
        new_obj = cls()
        field_names = cls.get_field_names()
        if len(field_names) != len(values):
            raise AttributeError("Inappropriate number of fields for composing '" + cls.__name__ + "' record-object\n" +
                                 "Expected: " + str(len(field_names)) + ", Actual: " + str(len(values)))
        for i in range(len(field_names)):
            if values[i] is not None and type(values[i]) != cls.get_field_type(field_names[i]):
                raise TypeError("Inappropriate type of " + str(i) + "th field (of " + str(len(field_names)) +
                                ") for composing '" + cls.__name__ + "' record-object\n" +
                                "Expected: " + str(cls.get_field_type(field_names[i])) +
                                ", Actual: " + str(type(values[i])) +
                                ", Name of field: " + field_names[i])
            cls.__ensure_single_field_constraints(field_names[i], values[i])
            new_obj.ensure_cross_field_constraints(field_names[i], values[i])
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
        except (Exception, Warning) as err:
            if record is not None:
                raw_response = str(record)
                if len(raw_response) > data_display_limit:
                    raw_response = "<Too long to display>"
                raise RuntimeError("A(n) " + type(err).__name__ + " was raised during restoring '" + cls.__name__ +
                                   "' object from database\n" + "Query:\n'" + query + "'\n" +
                                   "Raw response:\n" + raw_response) from err
            else:
                raise

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
            str_values = str(tuple(values))
            if len(str_values) > data_display_limit:
                str_values = "<Too long to display>"
            raise RuntimeError("An SQL-Error was raised when inserting into table '" + self.table_name + "'\n" +
                               "Command:\n" + command + "\n" + "Values:\n" + str_values) from err

    # ensuring database-constraints:
    @classmethod
    def __ensure_single_field_constraints(cls, field_name: str, value):
        for constraint in cls.get_field_constraints(field_name):
            if constraint == NotNull or isinstance(constraint, NotNull):
                if value is None:
                    warn("Field '" + field_name + "' of record-type '" + cls.__name__ +
                         "' cannot be NULL", ConstraintWarning)
            elif isinstance(constraint, Min):
                if value is not None:
                    if not isinstance(value, (int, float, datetime, Decimal)):
                        raise TypeError("Class-definition for record-type '" + cls.__name__ + "' is corrupt:\n" +
                                        "Constraint 'Min' can only be applied to field of type" +
                                        "int, float or datetime\n" +
                                        "Field name: '" + field_name + "', Actual type: " + str(type(value)))
                    if constraint.equality_allowed and value < constraint.value:
                        warn("Field '" + field_name + "' of record-type '" + cls.__name__ +
                             "' cannot be lower than " + str(constraint.value) +
                             "\nFound: " + str(value), ConstraintWarning)
                    elif value < constraint.value:
                        warn("Field '" + field_name + "' of record-type '" + cls.__name__ +
                             "' cannot be lower than or equal to " + str(constraint.value) +
                             "\nFound: " + str(value), ConstraintWarning)
            elif isinstance(constraint, Max):
                if value is not None:
                    if not isinstance(value, (int, float, datetime, Decimal)):
                        raise TypeError("Class-definition for record-type '" + cls.__name__ + "' is corrupt:\n" +
                                        "Constraint 'Max' can only be applied to field of type" +
                                        "int, float, datetime or Decimal\n" +
                                        "Field name: '" + field_name + "', Actual type: " + str(type(value)))
                    if constraint.equality_allowed and value > constraint.value:
                        warn("Field '" + field_name + "' of record-type '" + cls.__name__ +
                             "' cannot be greater than " + str(constraint.value) +
                             "\nActual value: " + str(value), ConstraintWarning)
                    elif value < constraint.value:
                        warn("Field '" + field_name + "' of record-type '" + cls.__name__ +
                             "' cannot be greater than or equal to " + str(constraint.value) +
                             "\nActual value: " + str(value), ConstraintWarning)
            elif isinstance(constraint, Size):
                if value is not None:
                    if not isinstance(value, (str, bytes)):
                        raise TypeError("Class-definition for record-type '" + cls.__name__ + "' is corrupt:\n" +
                                        "Constraint 'Size' can only be applied to field of type str or bytes\n" +
                                        "Field name: '" + field_name + "', Actual type: " + str(type(value)))
                    if len(value) > constraint.value:
                        warn("Length of field '" + field_name + "' of record-type '" + cls.__name__ +
                             "' cannot be longer than " + str(constraint.value) +
                             "\nActual length: " + str(len(value)), ConstraintWarning)
            else:
                raise TypeError("Class-definition for record-type '" + cls.__name__ + "' is corrupt:\n" +
                                "Parameterless single-field constraints must be a subtype of 'SingleFieldConstraint'" +
                                "whereas parametrized single-field constraint " +
                                "must be an instance of a 'SingleFieldConstraint' subclass\n" +
                                "Field: '" + field_name + "'\nConstraint: " + str(constraint))

    def ensure_cross_field_constraints(self, field_name: str, value):
        # to be overridden
        pass
