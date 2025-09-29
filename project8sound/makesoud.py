import time
import sys


helloworld = "Hey i just you!!"

for char in helloworld:
    print(char, end='',flush=True )
    time.sleep(0.06)
print("\n")

time.sleep(1)

helloworld = "And this is crazy!!"

for char in helloworld:
    print(char, end='',flush=True )
    time.sleep(0.06)