# write a code  to check give word is palindrome or not
# getting input from the user
word = input('enter your input: ')
# check the condition whether user input word is palindrome or not
if word == word[::-1]:
	print ("The word", word, "is palindrome")
else:
	print ("The word", word, "is not a palindrome")
