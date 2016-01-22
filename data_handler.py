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
cursor = None

employees = []
customers = []
orders = []
order_details = []


def startup():
    global connection, cursor
    with open("connection.json") as config_file:
        file_content = config_file.read()
        parsed_params = json.loads(file_content)
        connection = sql.connect(**parsed_params)
        cursor = connection.cursor()
        record_template.cursor_obj = cursor
        record_template.cursor_obj = cursor
        record_template.cursor_obj = cursor
        record_template.cursor_obj = cursor


def shutdown():
    global connection, cursor
    record_template.cursor_obj = None
    record_template.cursor_obj = None
    record_template.cursor_obj = None
    record_template.cursor_obj = None
    cursor.close()
    cursor = None
    connection.close()
    connection = None


def csv_to_sql(file_path: str, record_list: list, record_class):
    global connection
    with open(file_path, encoding="utf-8", newline='') as file_obj:
        csv_reader = csv.DictReader(file_obj, delimiter=';')
        for row in csv_reader:
            new_record = record_class.parse(row)
            new_record.persist()
            record_list.append(new_record)
            connection.commit()


def import_employees():
    global employees, employees_path
    csv_to_sql(employees_path, employees, Employee)


def import_customers():
    global customers, customers_path
    csv_to_sql(customers_path, customers, Customer)


def import_orders():
    global orders, orders_path
    csv_to_sql(orders_path, orders, Order)


def import_order_details():
    global order_details, order_details_path
    csv_to_sql(order_details_path, order_details, OrderDetail)


def import_all():
    import_employees()
    import_customers()
    # import_orders()
    # import_order_details()


def sql_to_csv():
    global employees, customers, orders, order_details

    # employees:
    employees += Employee.select()
    with open(employees_path, "w", encoding="utf-8", newline='') as employee_file:
        csv_writer = csv.DictWriter(employee_file, Employee.get_fields(), delimiter=';')
        csv_writer.writeheader()
        for emp in employees:
            csv_writer.writerow(emp.to_csv())

    # customers:
    customers += Customer.select()
    with open(customers_path, "w", encoding="utf-8", newline='') as customer_file:
        csv_writer = csv.DictWriter(customer_file, Customer.get_fields(), delimiter=';')
        csv_writer.writeheader()
        for customer in customers:
            csv_writer.writerow(customer.to_csv())


def demo():
    global cursor
    cursor.execute("SELECT * FROM Employees")
    for item in cursor:
        print(item)
