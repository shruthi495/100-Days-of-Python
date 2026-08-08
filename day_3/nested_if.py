print("Welcome to the rollercoaster!")
height=int(input("ENter your height"))
if height>=120:
    print("You can njoy the ride")
    age=int(input("What is your age"))
    if age<12:
        print("Your ticket price is 5$")
    elif age>=12 and age<18:
        print("Your ticket price is 7$")
    else:
        print("Your ticket price is 12$")
else:
    print("Sorry you are not allowed")