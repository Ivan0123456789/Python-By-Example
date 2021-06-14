raining = input("Is it raining?")

raining = str.lower(raining)

if raining == "yes":
    windy = input("Is it windy?")

    if windy == "yes":
        print("It is too windy for an umbrella")
    else:
        print("Take an umbrella")
else:
    print("Enyou your day")