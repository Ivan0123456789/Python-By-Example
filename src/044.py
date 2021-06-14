people = int(input("How many people do you want to invite to a party? "))

if people < 10:
    for i in range(people):
        name = input("Enter his/her name: ")
        print(name, "has been invited")
else:
    print("too many people")