# 100 days of python, day 15

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0

def checkResources(userOrder):
    for ingredient in MENU[userOrder]["ingredients"]:
        if MENU[userOrder]["ingredients"][ingredient] > resources[ingredient]:
            print(f"I'm sorry, there's not enough {ingredient}.")
            return 0
        else:
            continue

def subtractResources(userOrder):
    for ingredient in resources:
        if ingredient in MENU[userOrder]["ingredients"]:
            resources[ingredient] -= MENU[userOrder]["ingredients"][ingredient]

def checkMoneyReceived(userTotal, orderTotal, userOrder):
    global profit
    global order
    if userTotal == orderTotal:
        print(f"Enjoy your {userOrder}!")
        subtractResources(userOrder)
        profit += orderTotal
        order = False
        return
    elif userTotal > orderTotal: 
        print(f"Here is ${round(userTotal-orderTotal, 2)} change.")
        print(f"Enjoy your {userOrder}!")
        subtractResources(userOrder)
        profit += orderTotal
        order = False
        return
    else: 
        print(f"Sorry, that's not enough money. Money refunded.")
        return 0


keepServing = True
order = False
userOrder = ""
while keepServing: 
    while order == False:
        userOrder = input("What would you like? (espresso/latte/cappuccinos):\n")
        if userOrder == "espresso" or userOrder == "latte" or userOrder == "cappuccino" or userOrder == "report":
            order = True
        elif userOrder == "report":
            for item in resources: 
                print(f"{item}: {resources[item]}")
            print(f"Profit: ${profit}")
        else: 
            print("Please enter a valid option.")
        
    if userOrder == "off":
        print("Goodbye!")
        break

    if checkResources(userOrder) == 0:
        order = False
    else: 
        orderTotal = MENU[userOrder]["cost"]
        print(f"Your total is ${orderTotal}0.")
        userTotal = 0.00
        quarters = int(input("Please enter number of quarters: "))
        userTotal += quarters * .25
        print(f"${userTotal} inserted.")
        dimes = int(input("Please enter number of dimes: "))
        userTotal += dimes * .1
        print(f"${userTotal} inserted.")
        nickels = int(input("Please enter number of nickels: "))
        userTotal += nickels * .05
        print(f"${userTotal} inserted.")
        pennies = int(input("Please enter number of pennies: "))
        userTotal += pennies * .01
        print(f"${userTotal} inserted.")

        if checkMoneyReceived(userTotal, orderTotal, userOrder) == 0:
            order == False
    


    
    

