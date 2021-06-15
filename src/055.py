import random

number = random.randint(1,5)

choice = int(input("Enter a number: "))

if choice == number:
    print("Well done")
elif choice > number:
    print("Too high")

    second_choice = int(input("Enter a second number: "))

    if second_choice == number:
        print("Correct")
    else:
        print("You lose")
else:
    print("Too low")

    second_choice = int(input("Enter a second number: "))

    if second_choice == number:
        print("Correct")
    else:
        print("You lose")
