__author__ = 'KoicsD'

from os import system
from msvcrt import getch


enum_keys = {"up": 0, "down": 1, "right": 2, "left": 3, "enter": 4, "backspace": 5, "escape": 6}


header = ""


class Index:
    def __init__(self, limit: int):
        self.limit = limit
        self.value = 0

    def increase(self):
        if self.value < self.limit - 1:
            self.value += 1

    def decrease(self):
        if self.value > 0:
            self.value -= 1


def q_input():
    key = ord(getch())
    if key == 224:
        key = ord(getch())
        if key == 72:
            return enum_keys["up"]
        elif key == 80:
            return enum_keys["down"]
        elif key == 77:
            return enum_keys["right"]
        elif key == 75:
            return enum_keys["left"]
        else:
            return None
    elif key == 13:
        return enum_keys["enter"]
    elif key == 8:
        return enum_keys["backspace"]
    elif key == 27:
        return enum_keys["escape"]
    else:
        return None


class MenuItem:
    pass


class Menu(MenuItem):

    def __init__(self, title: str, message=""):
        self.title = title
        self.message = message
        self.items = []

    def add_item(self, item: MenuItem):
        self.items.append(item)

    def load(self):
        index = Index(len(self.items))
        while True:
            system("cls")
            print(header)
            self.list_items(index.value)
            print('-' * 21)
            print("Left arrow, Up arrow: move up; Right arrow, Up arrow: move down")
            print("Enter: select; Backspace: back to parent submenu; Esc: quit menu")
            usr_ans = q_input()

            if usr_ans == enum_keys["up"] or usr_ans == enum_keys["left"]:
                index.decrease()
            elif usr_ans == enum_keys["down"] or usr_ans == enum_keys["right"]:
                index.increase()
            elif usr_ans == enum_keys["enter"]:
                if index.value in range(len(self.items)):
                    if not self.items[index.value].load():
                        break
            elif usr_ans == enum_keys["backspace"]:
                return True  # means: caller must keep loop going on
            elif usr_ans == enum_keys["escape"]:
                return False  # means: caller must return

    def list_items(self, selected):
        print(self.title)
        print()
        print(self.message)
        print()
        for i in range(len(self.items)):
            if i == selected:
                print("\t*\t" + self.items[i].title)
            else:
                print("\t\t" + self.items[i].title)


class MenuPoint(MenuItem):
    def __init__(self, title: str, function):
        self.title = title
        self.function = function

    def load(self):
        system("cls")
        self.function()
        return False  # caller must always return
