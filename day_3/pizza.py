print("Welcome to python puza deliveries!")
size=input("what size of the pizza do u want? S or M or L ")
pepperoni=input("Do u want pepeeroni on your pizza? Y or no ")
extra_cheese=input("Do u want extra cheese? Y or NO ")
bill=0
if size=='S':
    bill+=15
    if pepperoni=='Y':
        bill+=2
    
elif size=='M':
    bill+=20
    if pepperoni=='Y':
        bill+=3
else:
    bill+=25
    if pepperoni=='Y':
        bill+=3


if extra_cheese=='Y':
    bill+=1


print(f"Your final bill is {bill}")



