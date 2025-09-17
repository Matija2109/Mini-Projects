import random

n1 = random.randint(1, 100)
n2 = random.randint(1, 1000)
n3 = random.randint(1, 1000000)

print("----====+====----")
print(" 1. 1 to 100\n 2. 1 to 1000\n 3. 1 to 1000000")
while True:
    try:
        difficulty = int(input("Welcome to number guessing game, whats difficulty would you like:"))
    except ValueError:
        print("----====+====----")
        print("Invalid input, try again!")
        continue
    if difficulty == 1:
        n = n1
        break
    if difficulty == 2:
        n = n2
        break
    if difficulty == 3:
        n = n3
        break
while True:
    try:
        user = int(input("Guess the number:"))
    except ValueError:
        print("Invalid input, try again!")
        continue
    if user != n and user < n:
        print("Wrong guess, number is higher, try again!")
    elif user != n and user > n:
        print("Wrong guess, number is lower, try again!")
    elif user == n:
        print("Thats correct!")
        break
