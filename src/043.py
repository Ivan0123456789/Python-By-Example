option = input("up/down: ")

if option == "up":
    up = int(input("Enter the top number: "))

    for i in range(1, up + 1):
        print(i)

elif option == "down": 
    down = int(input("Enter a number below 20: "))

    for i in range(20, down - 1, -1):
        print(i)
else:
    print("I don't understand")

