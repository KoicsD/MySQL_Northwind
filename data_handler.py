__author__ = 'KoicsD'
import json
import csv
import mysql.connector as sql
from mysql.connector import errorcode
import employee
import customer
import order
import order_detail


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
        employee.cursor_obj = cursor


def shutdown():
    global connection, cursor
    employee.cursor_obj = None
    cursor.close()
    cursor = None
    connection.close()
    connection = None


def csv_to_sql():
    global employees
    with open(employees_path, encoding="utf-8", newline="") as employees_file:
        csv_reader = csv.DictReader(employees_file, delimiter=";")
        for item in csv_reader:
            new_employee = employee.Employee.parse(item)
            employees.append(new_employee)
    for emp in employees:
        emp.persist()
        connection.commit()


    # with open(customers_path, encoding="utf-8") as customers_file:
    #     raw_content = customers_file.readlines()
    #     raw_content.pop(0)  # dropping header
    #     for row in raw_content:
    #         customers.append(Customer.parse(row))
    #
    # with open(orders_path, encoding="utf-8") as orders_file:
    #     raw_content = orders_file.readlines()
    #     raw_content.pop(0)  # dropping header
    #     for row in raw_content:
    #         orders.append(Order.parse(row))
    #
    # with open(order_details_path, encoding="utf-8") as order_details_file:
    #     raw_content = order_details_file.readlines()
    #     raw_content.pop(0)  # dropping header
    #     for row in raw_content:
    #         order_details.append(OrderDetail.parse(row))


def sql_to_csv():
    global employees
    employees += employee.Employee.select()
    with open(employees_path, "w", encoding="utf-8", newline="") as employee_file:
        csv_writer = csv.DictWriter(employee_file, employee.fields, delimiter=";")
        csv_writer.writeheader()
        for emp in employees:
            csv_writer.writerow(emp.to_csv())


def demo():
    global cursor
    cursor.execute("SELECT * FROM Employees")
    for item in cursor:
        print(item)
