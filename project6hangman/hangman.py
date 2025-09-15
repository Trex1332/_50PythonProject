import random
def getword():
    #open file
    file = open("word.txt")
    #each line into a list
    words = file.readlines()

    #need to remove newline
    for i in range(len(words)):
        words[i] = words[i].rstrip().lower()
    #gets a random word
    word = random.choice(words)
    #print word
    print(word)
    print(len(word))
    return word

def hideword(word):
    #gets word
    hidden = []
    #makes a list of hidden letters
    for i in range(len(word)):
        hidden.append("_")
    return hidden

def letterInWord(guess):
    global word
    global hidden
    global lives
    print(guess)
    #if letter in word add to hidden to show
    if guess in word:
        for i in range(len(hidden)):
            if word[i] == guess:
                hidden[i] = guess
    else:
        lives -= 1
word = getword()
hidden = hideword(word)
lives = len(hidden)

print("Welcome to hangman")
while True:
    #shows amout of letters
    print(hidden)
    #if the hidden put togther = the words end game
    x = ''.join(hidden) 
    if x == word:
        print("You Win")
        break
    #show lives
    print(f"you have {lives} lives")

    #user inputs guess
    guess = input("Guess a letter or word: ")
    if len(guess) == 1:
        letterInWord(guess)
    else:
        if guess == word:
            print("You Win")
            break
        else:
            lives -= 1