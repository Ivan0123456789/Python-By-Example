count = 0
another = "yes"

while another == "yes":
    name = input("Who do you want to invite to a party? ")
    print(name, "has now been invited")
    count = count + 1
    another = input("Invite another one? (yes/no) ")

print("You have", count, "people coming to your party")