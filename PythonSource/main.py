__author__ = 'KoicsD'
import menu
import data_handler
from sys import argv
from msvcrt import getch
from os import system
from warnings import simplefilter


main_menu = None


def startup():
    global main_menu
    if len(argv) == 1:
        simplefilter("error", data_handler.ConstraintWarning)
        print()
        print("ConstraintWarning action-level: error")
        print()
        data_handler.startup()
    elif len(argv) == 2:
        simplefilter(argv[1], data_handler.ConstraintWarning)
        print()
        print("ConstraintWarning action-level: " + argv[1])
        print()
        data_handler.startup()
    elif len(argv) == 3:
        simplefilter(argv[1], data_handler.ConstraintWarning)
        print()
        print("ConstraintWarning action-level: " + argv[1])
        print()
        data_handler.startup(argv[2])
    else:
        raise RuntimeError("Only two optional arguments are allowed: " +
                           "ConstraintWarning action-level and config-file path")
    print("\nPress any key to continue...")
    getch()
    main_menu = menu.Menu("Menu", "Please, select what you want!")
    sub_menu_1 = menu.Menu("From CSV File to MySQL Server", "Please, select what you want!")
    sub_menu_2 = menu.Menu("From MySQL Server to CSV File", "Please, select what you want!")
    main_menu.add_item(sub_menu_1)
    main_menu.add_item(sub_menu_2)
    menu_point_1_1 = menu.MenuPoint("Employees", lambda: do_task(data_handler.Importer.import_employees))
    menu_point_1_2 = menu.MenuPoint("Customers", lambda: do_task(data_handler.Importer.import_customers))
    menu_point_1_3 = menu.MenuPoint("Orders", lambda: do_task(data_handler.Importer.import_orders))
    menu_point_1_4 = menu.MenuPoint("OrderDetails", lambda: do_task(data_handler.Importer.import_order_details))
    menu_point_1_5 = menu.MenuPoint("All", lambda: do_task(data_handler.Importer.import_all))
    sub_menu_1.add_item(menu_point_1_1)
    sub_menu_1.add_item(menu_point_1_2)
    sub_menu_1.add_item(menu_point_1_3)
    sub_menu_1.add_item(menu_point_1_4)
    sub_menu_1.add_item(menu_point_1_5)
    menu_point_2_1 = menu.MenuPoint("Employees", lambda: do_task(data_handler.Exporter.export_employees))
    menu_point_2_2 = menu.MenuPoint("Customers", lambda: do_task(data_handler.Exporter.export_customers))
    menu_point_2_3 = menu.MenuPoint("Orders", lambda: do_task(data_handler.Exporter.export_orders))
    menu_point_2_4 = menu.MenuPoint("OrderDetails", lambda: do_task(data_handler.Exporter.export_order_details))
    menu_point_2_5 = menu.MenuPoint("All", lambda: do_task(data_handler.Exporter.export_all))
    sub_menu_2.add_item(menu_point_2_1)
    sub_menu_2.add_item(menu_point_2_2)
    sub_menu_2.add_item(menu_point_2_3)
    sub_menu_2.add_item(menu_point_2_4)
    sub_menu_2.add_item(menu_point_2_5)


def shutdown():
    global main_menu
    main_menu = None
    data_handler.shutdown()


def do_task(fun: callable):
    fun()
    print("Success!")
    getch()


def main():
    global main_menu
    main_menu.load()
    system("cls")


if __name__ == "__main__":
    startup()
    try:
        main()
    finally:
        shutdown()
