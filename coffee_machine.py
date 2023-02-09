
from asyncio import constants


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
profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if resources[item]<=order_ingredients[item]:
            print(f"sorry there is not enough {item}")
            return False
        return True

def process_coins():
     total=0
     total+=int(input("enter your quater coins : "))*0.025
     total+=int(input("enter your dimmes coins : "))*0.10
     total+=int(input("enter your nickel coins : "))*0.05
     total+=int(input("enter your pennies coins : "))*0.01
     return total
def transaction_successful(money_received,costs):
   if money_received>=costs:
       change=money_received-costs
       print(f"the change money will be {change}")
       global profit
       profit+=costs
       return True
   else:
        print(f"u do not have enough money ")
        return False
def make_coffee(name,order_ingredients):
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"your drink name will be {name}")   

is_on=True
while is_on:
    choice=input("which type of coffee u want ? :")

    if choice=="off":
        is_on=False

    elif choice=="report":
        print(f"water : {resources['water']}")
        print(f"milk :  {resources['water']}")
        print(f"coffee :{resources['water']}")
        print(f" money :{profit}")
    else:
        drink=MENU[choice]
        print(drink)
        is_resources_sufficient(drink["ingredients"])
        payment=process_coins()
        if  transaction_successful(payment,drink['cost']):
            make_coffee(choice,drink["ingredients"])




