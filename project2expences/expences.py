
while(True):


    try:
        budget = int(input("Whats your Budget: "))
        break
    except:
        print("Needs to be a Number!!!")

def expense():
    #takes money from budget
    try:
        expence = int(input("how much spent: "))
        
    except:
        print("Needs to be a Number!!!")
    global budget
    budget -= expence


def addBudget():
    #adds to budget
    try:
        extra = int(input("how much to Add: "))
        
    except:
        print("Needs to be a Number!!!")

    global budget
    budget += extra


while(True):
    if budget <= 0:
        print("Your Over you Budget")
        print("You Have £",budget,"left")
    else:
        print("You Have £",budget,"left")
    
    print("1: Spent Money")
    print("2: add money")
    print("3: Quit")
    try:
        userInput = int(input(" "))
        if userInput == 1:
            expense()
        elif userInput == 2:
            addBudget()
        elif userInput == 3:
            break
        else:
            print("Invalid input")
    except:
        print("Input Please")



