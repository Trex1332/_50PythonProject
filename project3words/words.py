

paragraph = open("words.txt")
words = paragraph.read()
amountOfWords = len(words.split())
word = words.split()

dict = {}

for i in word:
    if "." in i:
        i = i.replace(".","")
    if i in dict:
        dict[i] +=1
    else:
        dict.update({i:1})

print(dict)
print(amountOfWords)