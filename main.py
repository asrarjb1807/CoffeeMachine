from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

menu = Menu()
is_ture = True
while is_ture :
    ordername = input(f"What would you like to have ? ({menu.get_items()}) > ")
    if ordername == "report" :
        coffee_maker.report()
        money_machine.report()
    elif ordername == "off" :
        is_ture = False
    else :
        item = menu.find_drink(ordername)
        if coffee_maker.is_resource_sufficient(item) :
            payment = money_machine.make_payment(item.cost)
            if payment :
                coffee_maker.make_coffee(item)
            else :
                print("insufficient money")
        else :
            print("insufficient resource!")
