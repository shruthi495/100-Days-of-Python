print("Welcome to the secret auction program")
toContinue='yes'
dict_bid={}
while toContinue=='yes':
    name=input("What is your name?")
    amount=int(input("What's your bid?"))
    toContinue=input("Are there any other bidders?Type 'yes' or 'no' ")
    dict_bid[name]=amount
    if toContinue=='yes':
        print("\n"*100)


max=0
for name in dict_bid:
    bid=dict_bid[name]
    if bid>max:
        max=bid
        winner=name



print(f"Bidding is completed and winner is {winner} with {max}")



