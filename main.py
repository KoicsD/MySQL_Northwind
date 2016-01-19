__author__ = 'KoicsD'
import menu
import data_handler


main_menu = None


def startup():
    global main_menu
    main_menu = menu.Menu("Menu", "Please, select what you want!")
    menu_point_1 = menu.MenuPoint("From CSV File to MySQL Server", data_handler.csv_to_sql)
    menu_point_2 = menu.MenuPoint("From MySQL Server to CSV File", data_handler.sql_to_csv)
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
    shutdown()


if __name__ == "__main__":
    startup()
    main()
