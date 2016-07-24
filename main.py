__author__ = 'KoicsD'
from time import sleep
import menu
import data_handler


main_menu = None


def startup():
    global main_menu
    data_handler.startup()
    main_menu = menu.Menu("Menu", "Please, select what you want!")
    sub_menu_1 = menu.Menu("From CSV File to MySQL Server", "Please, select what you want!")
    sub_menu_2 = menu.Menu("From MySQL Server to CSV File", "Please, select what you want!")
    main_menu.add_item(sub_menu_1)
    main_menu.add_item(sub_menu_2)
    menu_point_1_1 = menu.MenuPoint("Employees", data_handler.Importer.import_employees)
    menu_point_1_2 = menu.MenuPoint("Customers", data_handler.Importer.import_customers)
    menu_point_1_3 = menu.MenuPoint("Orders", data_handler.Importer.import_orders)
    menu_point_1_4 = menu.MenuPoint("OrderDetails", data_handler.Importer.import_order_details)
    menu_point_1_5 = menu.MenuPoint("All", data_handler.Importer.import_all)
    sub_menu_1.add_item(menu_point_1_1)
    sub_menu_1.add_item(menu_point_1_2)
    sub_menu_1.add_item(menu_point_1_3)
    sub_menu_1.add_item(menu_point_1_4)
    sub_menu_1.add_item(menu_point_1_5)
    menu_point_2_1 = menu.MenuPoint("Employees", data_handler.Exporter.export_employees)
    menu_point_2_2 = menu.MenuPoint("Customers", data_handler.Exporter.export_customers)
    menu_point_2_3 = menu.MenuPoint("Orders", data_handler.Exporter.export_orders)
    menu_point_2_4 = menu.MenuPoint("OrderDetails", data_handler.Exporter.export_order_details)
    menu_point_2_5 = menu.MenuPoint("All", data_handler.Exporter.export_all)
    sub_menu_2.add_item(menu_point_2_1)
    sub_menu_2.add_item(menu_point_2_2)
    sub_menu_2.add_item(menu_point_2_3)
    sub_menu_2.add_item(menu_point_2_4)
    sub_menu_2.add_item(menu_point_1_5)


def shutdown():
    global main_menu
    main_menu = None
    data_handler.shutdown()


def main():
    global main_menu
    main_menu.load()
    print("Success!")
    sleep(1)
    menu.system("cls")


if __name__ == "__main__":
    startup()
    try:
        main()
    finally:
        shutdown()
