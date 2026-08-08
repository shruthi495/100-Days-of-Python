MENU={
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee":18,
            "milk":0,
        },
        "cost":150,
    },

    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":24,
        },
        "cost":250,
    },
    "cappuccino":{
        "ingredients":{
            "water":250,
            "milk":100,
            "coffee":24,
        },
        "cost":300
    }

}

resources={
    "water":300,
    "milk":200,
    "coffee":100,
}
def check_resource(choice):
    if resources['water']>=MENU[choice]['ingredients']['water']:
        if resources['milk']>=MENU[choice]['ingredients']['milk']:
            if resources['coffee']>=MENU[choice]['ingredients']['coffee']:
                return "Sufficent resources"
            else:
                return 'sorry there is not enough coffee'
        else:
            return 'Sorry there is not enough milk'
    else:
        return 'Sorry there is not enoguh water'


def check_money(choice,five,tens,fifities,hundreds):
    total=0
    total+=(five*5)
    total+=(tens*10)
    total+=(fifities*50)
    total+=(hundreds * 100)
    cost=MENU[choice]['cost']
    if total>=cost:
        resources['water'] -= MENU[choice]['ingredients']['water']
        resources['milk'] -= MENU[choice]['ingredients']['milk']
        resources['coffee'] -= MENU[choice]['ingredients']['coffee']
        return f"Here is {total-cost} in change\nHere is your {choice}"
    else:
        return "Not enough money. Money refunded"



print("Welcome to the digital coffee machine")
macine_on=True
while macine_on:
    choice=input("Wat would you like?? (espresso/latte/cappuccino): ")
    if choice=='off':
        print("Turning off the coffee machine")
        exit()
    elif choice in MENU:
        result=check_resource(choice)
        if result=="Sufficent resources":
            print("Insert Coins")
            five=int(input("How many fives? "))
            tens=int(input("How many tens? "))
            fifty=int(input("How many fifties? "))
            hundreds=int(input("How many hundreds? "))
            print(check_money(choice,five,tens,fifty,hundreds))
        else:
            print(result)
    elif choice=='report':
        print(resources)
    else:
        print("Invalid choice. Try again")
    
