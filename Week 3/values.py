
def charValues(word):	
	word = word.lower()

	value = 0

	for character in word:
		value += ord(character) - ord('a') + 1

	return value

word = input('bir string girin: ')
print(charValues(word))