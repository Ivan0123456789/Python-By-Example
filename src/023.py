nursery = input("Type in the firstline of a nursery rhyme: ")
start = int(input("Type in a starting number: "))
end = int(input("Type in a ending number: "))

length = len(nursery) 

print("This has", length, "letters on it")

part = (nursery[start:end])

print(part)