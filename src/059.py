import random

colour = random.choice(["red", "blue", "green", "white", "pink"])

print("Select from red, blue, green, white or pink")

tryagain = True

while tryagain == True:
    theirchoice = input("Enter a colour: ")
    theirchoice = theirchoice.lower()

    if colour == theirchoice:
        print("Well done")
        tryagain = False
    else:
        if colour == "red":
            print("I bet you are seeing RED right now!")
        elif colour == "blue":
            print("Don't feel BLUE.")
        elif colour == "green":
            print("I bet you are GREEn with envy right now.")
        elif colour == "white":
            print("Are you WHITE as a sheet, as you didn't guess correctly?")
        elif colour == "pink":
            print("Shame you are not feeling in the PINK, as you got it wrong!")