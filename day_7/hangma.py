import random
list_items=['virat','rohit','dhoni','shreyas','bhuvi','bumrah']
choosen_word=random.choice(list_items)
print(choosen_word)
res = ["_"] * len(choosen_word)
print(" ".join(res))
game_over=False
letters_to_guess=len(res)
lives=6

while lives>0:
    letter=input("Guess a letter: ")
    isFound=False
    for i in range(len(choosen_word)):
        if choosen_word[i] == letter:
            if res[i] == "_":   # ✅ prevents double counting
                res[i] = letter
                isFound=True
                letters_to_guess -= 1
                print(f"You ned to guess more {letters_to_guess} letters.")
            
    if not isFound:
        lives-=1
        print(f"Sorry that letter is not present in the word.TRY AGAIN")

        
        
    print(" ".join(res))

    if "_" not in res:
        game_over=True
        print("YOU WON")

    print(f"Your remaining {lives} lives")

if not game_over:
    print(f"YOU'VE LOST!!The word was {choosen_word}")
    

        

        

