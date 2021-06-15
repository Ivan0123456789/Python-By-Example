import random

number = random.randint(1, 10)

choice = int(input("Enter a number: "))

correct = False

while correct == False:
    choice = int(input("Enter a number: "))

    if choice == number:
        correct = True
    elif choice > number:
        print("Too high")
    else:
        print("Too low")