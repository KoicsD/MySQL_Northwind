__author__ = 'KoicsD'
import json
import re
import csv
import mysql.connector as sql
import abstract_record
from constraints import ConstraintWarning
from employee import Employee
from customer import Customer
from order import Order
from order_detail import OrderDetail
from os.path import abspath
from warnings import warn


employees_path = "Data/employees.csv"
customers_path = "Data/customers.csv"
orders_path = "Data/orders.csv"
order_details_path = "Data/order_details.csv"


connection = None

employees = []
customers = []
orders = []
order_details = []


def set_paths(root=None, employees=None, customers=None, orders=None, order_details=None):
    global employees_path, customers_path, orders_path, order_details_path
    if root is not None and \
            (employees is not None or customers is not None or orders is not None or order_details is not None):
        warn("Config-file defines CSV-root and separate CSV file-paths at the same time!", UserWarning)
    if root is not None:
        employees_path = re.sub("^Data", root, employees_path)
        customers_path = re.sub("^Data", root, customers_path)
        orders_path = re.sub("^Data", root, orders_path)
        order_details_path = re.sub("^Data", root, order_details_path)
    if employees is not None:
        employees_path = employees
    if customers is not None:
        customers_path = customers
    if orders is not None:
        orders_path = orders
    if order_details is not None:
        order_details_path = order_details


def startup(config_file_path="config.json"):
    global connection
    global employees_path, customers_path, orders_path, order_details_path
    try:
        with open(config_file_path) as config_file:
            file_content = config_file.read()
            parsed_params = json.loads(file_content)
            if "database" not in parsed_params["sql"]:
                raise LookupError("No database name specified in configuration dictionary")
            if "csv" in parsed_params:
                set_paths(**parsed_params["csv"])
            connection = sql.connect(**parsed_params["sql"])
            abstract_record.cursor_obj = connection.cursor()
            print("Configurations:")
            print("\tEmployees CSV-path: " + abspath(employees_path))
            print("\tCustomers CSV-path: " + abspath(customers_path))
            print("\tOrders CSV-path: " + abspath(orders_path))
            print("\tOrder-details CSV-path: " + abspath(order_details_path))
            print("\tServer host: " + connection.server_host)
            print("\tServer port: " + str(connection.server_port))
            print("\tDatabase: " + connection.database)
    except (Exception, Warning) as err:
        raise RuntimeError("A(n) " + type(err).__name__ + " was raised when processing config-file:\n\t" +
                           abspath(config_file_path)) from err


def shutdown():
    global connection
    abstract_record.cursor_obj.close()
    abstract_record.cursor_obj = None
    connection.close()
    connection = None


class Importer:
    @staticmethod
    def csv_to_sql(file_path: str, record_list: list, record_class: type, to_commit: bool):
        global connection
        with open(file_path, encoding="utf-8", newline='') as file_obj:
            csv_reader = csv.DictReader(file_obj, delimiter=';')
            for row in csv_reader:
                try:
                    new_record = record_class.from_dict(row)
                    new_record.persist()
                    record_list.append(new_record)
                except (Exception, Warning) as err:
                    raise RuntimeError("A(n) " + type(err).__name__ + " was raised when processing file:\n" +
                                       abspath(file_path) + "\nat line " + str(csv_reader.line_num)) from err
            if to_commit:
                connection.commit()

    @staticmethod
    def import_employees(to_commit=True):
        global employees, employees_path
        Importer.csv_to_sql(employees_path, employees, Employee, to_commit)

    @staticmethod
    def import_customers(to_commit=True):
        global customers, customers_path
        Importer.csv_to_sql(customers_path, customers, Customer, to_commit)

    @staticmethod
    def import_orders(to_commit=True):
        global orders, orders_path
        Importer.csv_to_sql(orders_path, orders, Order, to_commit)

    @staticmethod
    def import_order_details(to_commit=True):
        global order_details, order_details_path
        Importer.csv_to_sql(order_details_path, order_details, OrderDetail, to_commit)

    @staticmethod
    def import_all(to_commit=True):
        Importer.import_employees(False)
        Importer.import_customers(False)
        Importer.import_orders(False)
        Importer.import_order_details(to_commit)


class Exporter:
    @staticmethod
    def sql_to_csv(file_path: str, record_list: list, record_class):
        global connection
        record_list += record_class.select()
        with open(file_path, "w", encoding="utf-8", newline='') as file_obj:
            csv_writer = csv.DictWriter(file_obj, record_class.get_field_names(), delimiter=';')
            csv_writer.writeheader()
            for record in record_list:
                csv_writer.writerow(record.to_dict())

    @staticmethod
    def export_employees():
        global employees, employees_path
        Exporter.sql_to_csv(employees_path, employees, Employee)

    @staticmethod
    def export_customers():
        global customers, customers_path
        Exporter.sql_to_csv(customers_path, customers, Customer)

    @staticmethod
    def export_orders():
        global orders, orders_path
        Exporter.sql_to_csv(orders_path, orders, Order)

    @staticmethod
    def export_order_details():
        global order_details, order_details_path
        Exporter.sql_to_csv(order_details_path, order_details, OrderDetail)

    @staticmethod
    def export_all():
        Exporter.export_employees()
        Exporter.export_customers()
        Exporter.export_orders()
        Exporter.export_order_details()
