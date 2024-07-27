import json
import controls
from controls import *


class Sales:
    def __init__(self):
        self.sales = 0
        self.returns = 0
        self.profit = 0


class Topping:  #pizza factory
    def __init__(self):
        self.toppings = []

    def add_topping(self, ingredient: str):
        self.toppings.append(ingredient)
        return self

    def make_pizza(self):
        return Pizza(self.toppings)


class Pizza:
    def __init__(self, ingredients):
        self.ingredients: list = ingredients

    def __str__(self):
        return f'{self.ingredients}'

    def __getitem__(self, index):
        return self.ingredients[index]


class Order:
    def __init__(self):
        self.orders: list = []

    def add_order(self, order: Pizza):
        self.orders.append(order)

    def __getitem__(self, index):
        return self.orders[index]


class Payment:
    @staticmethod
    def cash_order(order: Order):
        price = controls.get_check(order)
        print(f'you payed {price} $ throu cash')

    @staticmethod
    def card_order(order: Order):
        price = controls.get_check(order)
        print(f"you payed {price} $ throu card")


class Parses:

    @staticmethod
    def order_saves(order: Order):
        return_value: str = ""
        for pizza in order:
            for ingr in pizza:
                return_value += f"{ingr} "
            return_value += "\n"
        return return_value


class Filemanager:

    @staticmethod
    def save(data):  #save order
        with open("pizzas/oreder.txt", 'w') as f:
            f.write(data)

    @staticmethod
    def load_ingredients():
        return json.load(open("pizzas/ingredients.json", 'r'))

    @staticmethod
    def add_ingredient(ingredient, profit, price):
        ingredients: dict = Filemanager.load_ingredients()
        ingredients.update({ingredient: (profit, price)})
        json.dump(ingredients, open("pizzas/ingredients.json", 'w'))

    @staticmethod
    def del_ingredient(ingredient: str):
        ingredients = Filemanager.load_ingredients().pop(ingredient)
        json.dump(ingredients, open("pizzas/ingredients.json", 'w'))
