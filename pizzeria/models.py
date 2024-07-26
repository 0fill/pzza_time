import json
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


class Pizza():
    def __init__(self, ingredients):
        self.ingredients: list = ingredients

    def __str__(self):
        return f'{self.ingredients}'


class Order:
    def __init__(self):
        self.orders: list = []

    def add_order(self, order: Pizza):
        self.orders.append(order)


class Payment:
    @staticmethod
    def cash_order(order: Order):
        print(f'you payed {get_check(order)} throu cash')

    @staticmethod
    def card_order(order: Order):
        print(f"you payed {get_check(order)} throu card")


class Parses:

    @staticmethod
    def order_saves(order: Order):
        return_value: str = ""
        for pizza in order.orders:
            return_value += pizza.ingredients + '\n'

class filemanager:

    @staticmethod
    def save(data):
        with open("pizzas/oreder.txt", 'w') as f:
            f.write(data)

    @staticmethod
    def load_ingredients():
        return json.load(open("pizzas/ingredients.json", 'r'))

    @staticmethod
    def add_ingredient(ingredient, profit):
        ingredients = filemanager.load_ingredients().update({ingredient: profit})
        json.dump(ingredients, open("pizzas/ingredients.json", 'w'))
