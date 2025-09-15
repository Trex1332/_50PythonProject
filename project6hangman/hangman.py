import random
def getword():
    #open file
    file = open("word.txt")
    #each line into a list
    words = file.readlines()

    #need to remove newline
    for i in range(len(words)):
        words[i] = words[i].rstrip()
    #gets a random word
    word = random.choice(words)
    #print word
    print(word)
    print(len(word))

getword()
