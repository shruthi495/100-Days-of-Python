import random
friend=["alice","bob","jack","virat"]

random_index=random.randint(0,3)
print(friend[random_index])

#we can also do 
random.choice(friend)