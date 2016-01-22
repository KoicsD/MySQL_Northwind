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


def csv_to_sql():
    global employees, customers, orders, order_details

    # employees:
    with open(employees_path, encoding="utf-8", newline='') as employees_file:
        csv_reader = csv.DictReader(employees_file, delimiter=';')
        for item in csv_reader:
            new_employee = Employee.parse(item)
            employees.append(new_employee)
    for emp in employees:
        emp.persist()
        connection.commit()

    # customers:
    with open(customers_path, encoding="utf-8", newline='') as customers_file:
        csv_reader = csv.DictReader(customers_file, delimiter=';')
        for item in csv_reader:
            new_customer = Customer.parse(item)
            customers.append(new_customer)
    for customer in customers:
        customer.persist()
        connection.commit()

    # order?
    # order_details?


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
