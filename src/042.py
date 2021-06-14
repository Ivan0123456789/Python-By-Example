total = 0

for i in range(0,5):
    number = int(input("Enter a number: "))
    option = input("Do you want the number included? (yes/no) ")

    if option == "yes":
        total = total + number
    else:
        total= total

print("Total is:", total)