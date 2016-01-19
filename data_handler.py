__author__ = 'KoicsD'
import mysql.connector as sql
from mysql.connector import errorcode
import json


connection = None
cursor = None


def startup():
    global connection, cursor
    with open("connection.json") as config_file:
        file_content = config_file.read()
        parsed_params = json.loads(file_content)
        connection = sql.connect(**parsed_params)
        cursor = connection.cursor()


def shutdown():
    global connection, cursor
    cursor.close()
    cursor = None
    connection.close()
    connection = None


def demo():
    global cursor
    cursor.execute("SELECT * FROM Employees")
    for item in cursor:
        print(item)
