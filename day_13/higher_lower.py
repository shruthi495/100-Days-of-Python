import random
data= [
    {
        "name":"instagram",
        "followers":346,
        'description':'Social media platform',
        'country':'united states'

    },
    {
        "name":"Virat Kohli",
        "followers":250,
        'description':'Circketer',
        'country':'India'
    },
    {
        "name":"Ronaldo",
        "followers":321,
        'description':'Footballer',
        'country':'Portugal'
    },
    {
        "name":"Arina Grande",
        "followers":190,
        'description':'Musician',
        'country':'UN\nited States'
    },
    {
        "name" :"swapna",
        "followers":1,
        'description':"designer",
        'country':'India'
    },
    {
        "name":"Alia Bhatt",
        "followers":100,
        'description':'Actress',
        'country':'India'
    }
]

def format_option(option,label):
    return f"{label}:{option['name']},a {option['description']},from {option['country']}"

print("Welcome to the higher lower game")
score=0
isCrct=True
option_1=random.choice(data)
while isCrct:

    option_2=random.choice(data)
    #to avoid duplicates
    while option_2==option_1:
        option_2=random.choice(data)

    print(format_option(option_1,"Compare A"))
    print("VS")
    print(format_option(option_2,"Against B"))
    user_answer=input("Who has more followers. Type 'A' or 'B' ?").upper()
    if option_1["followers"]>option_2["followers"] :
        crct_ans='A'
    else:
        crt_ans='B'

    if(user_answer==crct_ans):
        score+=1
        print("You guessed it right!!")
        print(f"Yor score {score}")
        isCrct=True
        if crct_ans=="B":
            option_1=option_2
    else:
        print("Sorry ur wrong")
        print(f"Your final score {score}")
        exit()