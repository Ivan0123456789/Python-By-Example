import random

options = ['t','h']

option = random.choice(options)

user_option = input("h/t? ")

if user_option == option:
    print("You win!")
else:
    print("Bad luck")

print("It was", option)