import random

roll1 = random.randrange(1,5)

guess = int(input("Guess number 1-5: "))

if guess == roll1:
    print("win the number was ", roll1)

else:
    print("incorrect")

usercard = []

while len(usercard) < 3:
    add = int(input("number 1-50: "))
    usercard.append(add)
print(usercard)

attempts = 0
gamble = []

while gamble != usercard:
    attempts += 1
    gamble.clear()
    while len(gamble) < 3:
        num = random.randrange(1,51)
        if num in gamble:
            pass
        else:
            gamble.append(num)   
    print(gamble)

print(attempts)
    

