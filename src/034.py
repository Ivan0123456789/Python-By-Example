print("1. Square")
print("2. Triangle")
print("")
option = int(input("Enter an option: "))

if option == 1:
    side = int(input("Enter the side of the square: "))
    area = side**2
    print("The are of the square is:", area)
elif option == 2:
    base = int(input("Enter the base of the triangle: "))
    height = int(input("Enter the height of the triangle: "))
    area = base * height / 2
    print("The are of the triangle is: ", area)
else:
    print("Error")