from controls import *
from models import *


def run():
    info = Sales()
    order = Order()
    while True:
        main_menu()
        choice = check_for_input(0, 3)
        if choice == 1:
            order_menu()
            pizza_man = Topping()
            choice1 = check_for_input(1, 3)
            if choice1 == 1:
                pizza_list()
                choice2 = check_for_input(1, 5)
                if choice2 == 1:
                    order.add_order(pizza_man.add_topping("tomato sauce")
                                    .add_topping("mozzarella")
                                    .add_topping("basil").make_pizza())
                elif choice2 == 2:
                    order.add_order(pizza_man.add_topping("tomato sauce")
                                    .add_topping("mozzarella")
                                    .add_topping("pepperoni").make_pizza())
                elif choice2 == 3:
                    order.add_order(pizza_man.add_topping("tomato sauce")
                                    .add_topping("mozzarella")
                                    .add_topping("gorgonzola")
                                    .add_topping("edam")
                                    .add_topping("parmesan").make_pizza())
                elif choice2 == 4:
                    order.add_order(pizza_man.add_topping("tomato sauce")
                                    .add_topping("mozzarella")
                                    .add_topping("ham")
                                    .add_topping("mushrooms")
                                    .add_topping("olives").make_pizza())
                elif choice2 == 5:
                    order.add_order(pizza_man.add_topping("tomato sauce")
                                    .add_topping("mozzarella")
                                    .add_topping("spicy salami").make_pizza())
            elif choice1 == 2:
                while True:
                    ingrediant = chose_ingredinet(Filemanager.load_ingredients().keys())
                    pizza_man.add_topping(ingrediant)
                    if input("is it all? ").lower() == "y":
                        order.add_order(pizza_man.make_pizza())
                        break       #order
            elif choice1 == 3:
                show_order(order)
        elif choice == 2:
            choice2 = check_for_input(1, 2)
            if choice2 == 1:
                Payment.cash_order(order)
            elif choice2 == 2:
                Payment.card_order(order)
            sucess_sale(info, order)
            Filemanager.save(Parses.order_saves(order))     #payment
        elif choice == 3:       #admin access
            if check_admin(get_admin_id()):
                while True:
                    menu_admin()
                    choice1 = check_for_input(0,2)
                    if choice1 == 1:
                        Filemanager.add_ingredient(get_ingredient(),float(get_profit()),float(get_price()))
                    elif choice1 == 2:
                        Filemanager.del_ingredient(chose_ingredinet(Filemanager.load_ingredients().keys()))
                    else:
                        break


run()
