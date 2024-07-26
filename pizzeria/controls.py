from models import *
from view import *


def check_for_input(min_choice, max_choice):
    while True:
        choice = get_input()
        try:
            choice = int(choice)
            if min_choice <= choice <= max_choice:
                return choice
        except ValueError:
            error_massage_NotNumber()
        finally:
            error_massage_OutOfRange(min_choice, max_choice)


def sucess_sale(sale: Sales, order: Order):
    sale.sales += 1
    for item in order:
        for ingredient in item.ingredients:
            sale.profit += filemanager.load_ingredients().get(ingredient)


def costum_pizza():
    while True:
        ingredient = chose_ingredinet(filemanager.load_ingredients().keys())


def get_check(order: Order):
    ingr = filemanager.load_ingredients()
    total = 0
    for a in order:
        for b in a:
            total += ingr.get(b)
