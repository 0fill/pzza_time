from controls import *

def run():
    info = Sales()
    order = Order()
    while True:
        main_menu()
        choice = check_for_input(0, 3)
        if choice == 1:
            order_menu()
            pizza_man = Topping()
            choice = check_for_input(1, 2)
            if choice == 1:
                pizza_list()
                choice = check_for_input(1, 5)
                if choice == 1:
                    order.add_order(pizza_man.add_topping("tomato sauce")
                                    .add_topping("mozzarella")
                                    .add_topping("basil").make_pizza())
                elif choice == 2:
                    order.add_order(pizza_man.add_topping("tomato sauce")
                                    .add_topping("mozzarella")
                                    .add_topping("pepperoni").make_pizza())
                elif choice == 3:
                    order.add_order(pizza_man.add_topping("tomato sauce")
                                    .add_topping("mozzarella")
                                    .add_topping("gorgonzola")
                                    .add_topping("edam")
                                    .add_topping("parmesan").make_pizza())
                elif choice == 4:
                    order.add_order(pizza_man.add_topping("tomato sauce")
                                    .add_topping("mozzarella")
                                    .add_topping("ham")
                                    .add_topping("mushrooms")
                                    .add_topping("olives").make_pizza())
                elif choice == 5:
                    order.add_order(pizza_man.add_topping("tomato sauce")
                                    .add_topping("mozzarella")
                                    .add_topping("spicy salami").make_pizza())
            elif choice == 2:
                while True:
                    ingrediant = chose_ingredinet(filemanager.load_ingredients().keys())
                    pizza_man.add_topping(ingrediant)
                    if input("is it all? ").lower() == "y":
                        order.add_order(pizza_man.make_pizza())
                        break


run()
