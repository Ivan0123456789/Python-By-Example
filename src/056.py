import random

number = random.randint(1, 10)

choice = int(input("Enter a number: "))

while choice != number:
    choice = int(input("Enter a number: "))