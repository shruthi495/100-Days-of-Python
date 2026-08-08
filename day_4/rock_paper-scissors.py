import random
print("Welcome to rock paper scissors wolrd")
user_index=input("type 1 for rock 2 for paper 3 scissors")
computer_index=random.randint(1,3)
if computer_index==1:
    computer_choice="rock"
elif computer_index==2:
    computer_choice="paper"
else:
    computer_choice="scissor"

if user_index==1:
    user_choice="rock"
elif user_index==2:
    user_choice="paper"
else:
    user_choice="scissor"
print(f"You chose  {user_choice}")
print(f"Computer chose {computer_choice}")
if (user_choice=="scissor" and computer_choice=="paper") or (user_choice=="rock" and computer_choice=="scissor") or(user_choice=="paper" and computer_choice=="rock") :
    print("User wom")

elif (user_choice==computer_choice):
    print("DRAW!!")
else:
    print("Computer won")