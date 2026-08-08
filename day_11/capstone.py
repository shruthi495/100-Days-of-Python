import random


def convert(item):
    if item=='J' or item=='Q' or item=='K':
        return 10
    elif item=='A':
        return 11
    else:
        return int(item)


def calculate_score(cards):
    score=0
    ace_count=0
    for card in cards:
        score+=convert(card)
        if card=='A':
            ace_count+=1
    while score>21 and ace_count:
        score-=10
        ace_count-=1

    return score

def deal_card():
   list_of_cards=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
   return random.choice(list_of_cards)



print("Welcome to blackjack/21")


computer_choice=[deal_card(),deal_card()]
user_choice=[deal_card(),deal_card()]

user_score=calculate_score(user_choice)
cmptr_score=calculate_score(computer_choice)
print(f"Your cards: {user_choice}")
print(f"Your score: {user_score}")
print(f"Computer's first card: {computer_choice[0]}")

if user_score==21:
    print("Hurray!!!!YOU WON")
    exit()



choice='y'
while choice=='y':

    choice=input("Draw another card.Types 'y' for yes 'n' for no: ")
    if choice=='y':
        user_choice.append(deal_card())

    user_score=calculate_score(user_choice)
    print(f"Your cards {user_choice}")
    print(f"Your score {user_score}")
    if user_score==21:
        print("Hurray!!!!YOU WON")
        exit()

    if user_score>21:
        print("Ooopsiii!! you Loose..you exceeded 21")
        exit()

while cmptr_score<17:
    computer_choice.append(deal_card())
    cmptr_score=calculate_score(computer_choice)

print(f"Computer cards {computer_choice}")
print(f"Computer score {cmptr_score}")
if cmptr_score > 21:
        print("Computer went over 21. You win!")
        exit()
        
elif user_score > cmptr_score:
        print("You win!")
elif cmptr_score > user_score:
        print("Computer wins!")
else:
        print("It's a draw!")