#write a code  to check give word is palindrome or not
word = input('enter your input: ')
if word == word[::-1]:
	print ("The word", word, "is palindrome")
else:
	print ("The word", word, "is not a palindrome")
