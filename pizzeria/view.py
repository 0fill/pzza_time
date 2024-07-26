def main_menu():
    print(f"""
--------MENU---------
|   1 - make order  |
|   2 - pay         |
|   3 - admin       |   
|   0 - quit        |
---------------------""")


def order_menu():
    print(f"""
    1 -  chose pizza
    2 -  costum pizza""")


def pizza_list():
    print(f"""
1 - Margherita (tomato sauce, mozzarella, basil)
2 - Pepperoni (tomato sauce, mozzarella, pepperoni)
3 - Quattro Formaggi (tomato sauce, mozzarella, gorgonzola, edam, parmesan)
4 - Capricciosa (tomato sauce, mozzarella, ham, mushrooms, olives)
5 - Diavola (tomato sauce, mozzarella, spicy salami)
    
    """)


def pay_menu():
    print(f"""
    1- cash
    2- card    
    """)


def get_input():
    return input("What do you want? ")


def error_massage_NotNumber():
    print(f"enter a valid number")


def error_massage_OutOfRange(minn, maxx):
    print(f"enter a number between {minn} and {maxx}")


def chose_ingredinet(ingrediants: list):
    for ingrediant in ingrediants:
        print(ingrediant, end=" ")
    choice = input("chose ingredient")
    if choice in ingrediants:
        return choice
    else:
        for ingrediant in ingrediants:
            if choice in ingrediant:
                if input(f"did you mean {ingrediant}?") == "y":
                    return ingrediant
