import random
print("Welcome to te password generator")
letter_cnt=int(input("How many letters would you like in your password? "))
symbol_cnt=int(input("How many sumbols would you like ? "))
number_cnt=int(input("How many numbers would you like? "))

letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*']

password=[]
for _ in range(letter_cnt):
    password.append(random.choice(letters))
for _ in range(symbol_cnt):
    password.append(random.choice(symbols))
for _ in range(number_cnt):
    password.append(random.choice(numbers))

random.shuffle(password)
print(password)
ps="".join(password)

print(f"Your generated password is: {ps}")
