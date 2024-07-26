from controls import *
import json


def run():
    info = Sales()
    while True:
        main_menu()
        choice = check_for_input(0, 3)
        if choice == 1:
            order_menu()
            choice = check_for_input(1, 2)
            if choice == 1:
                pizza_list()
                choice = check_for_input(1, 5)



run()