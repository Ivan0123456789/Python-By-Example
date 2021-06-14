firstname = input("Enter your firstname: ")

if len(firstname) < 5:
    surname = input("Enter your surname: ")
    name = firstname + surname
    name = name.upper()
    print(name)
else:
    firstname = firstname.lower()
    print(firstname)