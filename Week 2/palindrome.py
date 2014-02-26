testStr = input('Enter a word to test if it is a palindrome: ')

i = 0
palindrome = True

while ( i < len(testStr) / 2 ):
	if testStr[i] != testStr[-(i+1)]:
		palindrome = False	
	i += 1

print(palindrome)