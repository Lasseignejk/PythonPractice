
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeeMaker = CoffeeMaker()
menu = Menu()
moneyMachine = MoneyMachine()

keepServing = True
while keepServing: 
    order = input(f"What would you like? ({menu.get_items()}):\n")
    if order == "report":
        coffeeMaker.report()
        moneyMachine.report()
    elif coffeeMaker.is_resource_sufficient(menu.find_drink(order)) == True: 
        drink = menu.find_drink(order)
        if moneyMachine.make_payment(drink.cost) == True:
            coffeeMaker.make_coffee(drink)
