__author__ = 'KoicsD'
from time import sleep
import menu
import data_handler


main_menu = None


def startup():
    global main_menu
    main_menu = menu.Menu("Menu", "Please, select what you want!")
    menu_point_1 = menu.MenuPoint("From CSV File to MySQL Server", data_handler.Importer.import_all)
    menu_point_2 = menu.MenuPoint("From MySQL Server to CSV File", data_handler.Exporter.export_all)
    main_menu.add_item(menu_point_1)
    main_menu.add_item(menu_point_2)
    data_handler.startup()


def shutdown():
    global main_menu
    main_menu = None
    data_handler.shutdown()


def main():
    global main_menu
    main_menu.load()
    sleep(1)
    menu.system("cls")


if __name__ == "__main__":
    startup()
    try:
        main()
    finally:
        shutdown()
