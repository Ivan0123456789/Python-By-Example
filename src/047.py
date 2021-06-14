number1 = int(input("Enter a number: "))
total = number1
option = "yes"

while option == "yes":
    number2 = int(input("Enter another number: "))
    total = total + number2
    option = input("Enter another number? (yes/no) ")

print("Total is...", total)
