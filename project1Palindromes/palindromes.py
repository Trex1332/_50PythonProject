word = input("Word to check: ")

wordBackword = word[::-1]

print(word)
print(wordBackword)

if word == wordBackword:
    print("is Palindrome")
else:
    print("Is not a palindrome")