import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number bwtween 1 and 100")
answer=random.randint(1,100)

level=input("Choose a difficulty. Type 'easy' or 'hard': ")


if level=='easy':
    print("You have 10 attempts remaining to guess the number")
    attempts=10
elif level=='hard':
    print("You have 5 attempts remaining to guess the number")
    attempts=5
else:
    exit()
while attempts>0: 
    guess=int(input("Make a guess: "))
    if guess<answer:
        print("Too Low")
        
    elif guess>answer:
        print("Too high")
    else:
        print("Perfect Guess")
        exit()
    attempts-=1
    print("Guess again")
    print(f"You have {attempts} remaining to guess the number")

print("Ooopssssiiiii!!! your attempts ave been completed try again")