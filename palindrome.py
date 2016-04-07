word = raw_input("Enter a valid word: ")
word1 = word[::-1]
if word == word1:
    print("%s is palindrome") % word
else:
    print("%s is not a palindrome") % word

