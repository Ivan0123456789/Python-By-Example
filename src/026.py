word = input("Enter a word: ")
first = word[0]
length = len(word)
rest = word[1:length]

if first == "a" or first == "e" or first == "i" or first == "o" or first == "u":
    newword = word + "way"
else:
    newword = rest + first + "ay"

print(newword.lower())