str1 = input('bir string girin: ')
str2 = input('başka bir string girin: ')

set1 = set(str1)
set2 = set(str2)

unique1 = set1 - set2
unique2 = set2 - set1

uniqueAll = set1 & set2

print('yalnızca ilk stringde bulunan karakterler: ')
print(unique1)

print('yalnızca ikinci stringde bulunan karakterler')
print(unique2)

print('iki stringde birden bulunan karakterler: ')
print(uniqueAll)