import random

score = 0

for i in range(1,6):
    num1 = random.randint(1,50)
    num2 = random.randint(1,50)
    sum = num1 + num2

    print(num1, "+", num2, "= ")

    answer = int(input("Your answer: "))
    print()

    if answer == sum:
        score = score + 1
    
print("Corrects: ", score)
print("Incorrects: ", 5-score)