__author__ = 'KoicsD'
import data_handler


def startup():
    data_handler.startup()


def shutdown():
    data_handler.shutdown()


if __name__ == "__main__":
    startup()
    data_handler.demo()
    shutdown()
