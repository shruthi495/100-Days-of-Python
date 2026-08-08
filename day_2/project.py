print("Welcome to the tip calculator..")
bill=float(input("What was the total bill? "))
tip=int(input("How much tip would you like to give (10 or 15 or 20)"))
share=int(input("how many pople to split the bill? "))

total_amount=float(bill*(tip/100)+bill);
each_amount=total_amount/share
print(f"Each person should pay: {round(each_amount,2)}")
