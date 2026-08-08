print("Welcome to Treasure Island")
print("Your mission is to find the treassure")
direction=input("You're at a cross road.Wher do u want to go? Type left or right: ")

if direction=="right":
    print("Game over")
else:
    print("You've come to a lake. There is an island in the middle of the lake")
    hw_to_go=input("Type wait to wait for the boat.Type swim to swim across: ")
    if hw_to_go=="swim":
        print("Game over")
    else:
        door=input("You arrived at the island. there is a house with 3 doors. choose one among yellow/blue/red: ")
        if door=="yellow":
            print("YOU WON!!!!")
        else:
            print("Game over")