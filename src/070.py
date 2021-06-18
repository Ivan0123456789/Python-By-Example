countries = ("Mexico", "Chile", "Spain", "Tunisia", "Morocco")

print(countries)

country = input("Enter one of the countries: ")
number = int(input("Enter a number between 0 and 4: "))

print(country, "has the position", countries.index(country))
print("Country in position", number, "is", countries[number])
