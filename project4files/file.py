
while(True):
    name = input("Whos Entry is it: ")

    name = name + ".txt"
    try:
        file = open(name)
        print(file.read())
        userInput = input("Would you like to append to this file? Y/N:").lower()
        if userInput == "y":
            text = input("Write what you want to add: ")
            text = "\n" + text
            file = open(name,"a")

            file.write(text)
            file = open(name)
            print(file.read())
        else:
            pass

    except:
        file = open(name,"x")
        print("No File of that Name one has been Created Would you like to Edit it? Y/N")
        userInput = input(":").lower()
        if userInput == "y":
            text = input("Write what you want to add: ")
            file = open(name,"a")

            file.write(text)
            file = open(name)
            print(file.read())
        elif userInput == "n":
            print("finished")