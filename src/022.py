firstname = input("Enter your first name in lower case: ")
surname = input("Enter your surname in lower case: ")

firstname = firstname.title()
surname = surname.title()

name = firstname + " " + surname

print(name)