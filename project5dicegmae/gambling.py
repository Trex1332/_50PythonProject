import random

money = int(input("Money to lose: "))

while True:
    roll = random.randrange(1,20)
    hope = int(input("Money to lose: "))

    money -= hope
    persentge = int(input("How much by: 1-20: "))
    if persentge <= roll:
        print(roll)
        print("X",persentge)
        money += hope * persentge
    else:
        print(roll," you lost ",hope)
    print(money)