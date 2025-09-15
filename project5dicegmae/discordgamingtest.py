import random

def slots(money):
    fruits = ["Apple","Banna","Pair","PinApple","Crown"]
    slot = []
    #choices 3 fuites to fill the thing with.
    while True:
        while len(slot) < 3:
            slot.append(random.choice(fruits))

        print(slot)
        #use slot1 == slot2 == slot3
        if slot[0] == slot[1] == slot[2]:
            if slot[0] == "Crown":
                money *= 10
            else:
                money *= 3
            
            return money
        elif slot[0] == slot[1] or slot[1] == slot[2] or slot[0] == slot[2]:
            money *= 1.5
            return money
        else:
            if money == 0:
                money = -money - 1
                return money
            else:
                money = -money
                return money
        
def addMoney():
    global money
    debt = float(input("a debt please: "))
    money += debt
    print(money)
    return money

money = float(input("add money please: "))

def game():
    global money
    while money >= 0.1:
        amoutPerTur = float(input("add money please!: "))
        if amoutPerTur > money:
            print("Not enough money")
        else:
            money += slots(amoutPerTur)
            print(money)
while True:
    game()

    addMoney()
