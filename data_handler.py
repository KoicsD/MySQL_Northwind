__author__ = 'KoicsD'
import json
import csv
import mysql.connector as sql
from mysql.connector import errorcode
import record_template
from employee import Employee
from customer import Customer
from order import Order
from order_detail import OrderDetail


employees_path = "Data/employees.csv"
customers_path = "Data/customers.csv"
orders_path = "Data/orders.csv"
order_details_path = "Data/order_details.csv"


connection = None

employees = []
customers = []
orders = []
order_details = []


def startup():
    global connection
    with open("connection.json") as config_file:
        file_content = config_file.read()
        parsed_params = json.loads(file_content)
        connection = sql.connect(**parsed_params)
        record_template.cursor_obj = connection.cursor()


def shutdown():
    global connection
    record_template.cursor_obj.close()
    record_template.cursor_obj = None
    connection.close()
    connection = None


class Importer:
    @staticmethod
    def csv_to_sql(file_path: str, record_list: list, record_class):
        global connection
        with open(file_path, encoding="utf-8", newline='') as file_obj:
            csv_reader = csv.DictReader(file_obj, delimiter=';')
            for row in csv_reader:
                new_record = record_class.parse(row)
                new_record.persist()
                record_list.append(new_record)
                connection.commit()

    @staticmethod
    def import_employees():
        global employees, employees_path
        Importer.csv_to_sql(employees_path, employees, Employee)

    @staticmethod
    def import_customers():
        global customers, customers_path
        Importer.csv_to_sql(customers_path, customers, Customer)

    @staticmethod
    def import_orders():
        global orders, orders_path
        Importer.csv_to_sql(orders_path, orders, Order)

    @staticmethod
    def import_order_details():
        global order_details, order_details_path
        Importer.csv_to_sql(order_details_path, order_details, OrderDetail)

    @staticmethod
    def import_all():
        Importer.import_employees()
        Importer.import_customers()
        Importer.import_orders()
        Importer.import_order_details()


class Exporter:
    @staticmethod
    def sql_to_csv(file_path: str, record_list: list, record_class):
        global connection
        record_list += record_class.select()
        with open(file_path, "w", encoding="utf-8", newline='') as file_obj:
            csv_writer = csv.DictWriter(file_obj, record_class.get_fields(), delimiter=';')
            csv_writer.writeheader()
            for record in record_list:
                csv_writer.writerow(record.to_csv())

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


def demo():
    record_template.cursor_obj.execute("SELECT * FROM Employees")
    for item in record_template.cursor_obj:
        print(item)
