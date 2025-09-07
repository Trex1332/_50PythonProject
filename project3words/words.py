import string

paragraph = open("words.txt")
words = paragraph.read().lower().translate(str.maketrans('', '', string.punctuation))
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

default = 0
most = ""
for i in dict.keys():
    if dict[i] >= default:
        most = i
        default = dict[i]
print(most,default)
print(amountOfWords)