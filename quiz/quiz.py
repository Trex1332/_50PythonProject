"""
import json
score = {"Sam": 15}

name = "scores.txt"
try:
    file = open(name)
    file = open(name,"a")
    file.write(json.dumps(score)+ "\n")
    file = open(name)

except:
    file = open(name,"x")
"""
import random
import time
#score
score = 0
#lives for game
lives = 3
#methods to choice from
things = ["+","*","-"]

while lives > 0:
    ans = 0
    num1 = 0
    num2 = 0
    meth = ""
    while ans <= 0:
        #get random number
        num1 = random.randrange(1,20)
        num2 = random.randrange(1,20)
        #get random method
        meth = random.choice(things)
        #print(num1,meth,num2)
    
        #do the math of the equation
        if meth == "/":
            ans = num1 // num2
        elif meth == "+":
            ans = num1 + num2
        elif meth == "*":
            ans = num1 * num2
        elif meth == "-":
            ans = num1 - num2
        #print(ans)


    #user inputs awnser 
    guess = f"What is {num1} {meth} {num2}: "
    for char in guess:
        print(char, end='',flush=True)
        time.sleep(0.06)
    question = int(input(f""))

    #checks input and ans
    if question == ans:
        score += 1
        result = f"Correct your score is {score} Points \n"
        for char in result:
            print(char, end='' , flush=True)
            time.sleep(0.06)
    else:
        lives -= 1
        result = f"Incorrect you have {lives} Lives left \n"
        for char in result:
            print(char, end='' , flush=True)
            time.sleep(0.06)


print(f"Your Score was {score} Points")
    
