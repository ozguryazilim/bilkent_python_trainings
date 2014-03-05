people = []

while True:
	name = input('Bir kişi ismi girin (-1=çık): ')
	if(name == '-1'):
		break

	surname = input('Bu kişi için bir soyisim girin: ')
	age = int(input('Bu kişi için bir yaş girin: '))

	person = {
		'name': name,
		'surname': surname,
		'age': age
	}

	people.append(person)

oldestPeople = []
maxAge = 0
for person in people:
	if(person['age'] >= maxAge):
		maxAge = person['age']

print('Bu gruptaki en büyük yaş: ', maxAge)
print('Bu kişiler: ')

for person in people:
	if(person['age'] == maxAge):
		oldestPeople.append(person)
	print(person['name'] + ' ' + person['surname'])
	


