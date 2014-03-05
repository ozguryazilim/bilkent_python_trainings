people = [{
	'name': 'Oguz',
	'surname': 'Bilgener',
	'age': 18
},
{'name': 'Ozan Can',
	'surname': 'Altıok',
	'age': 20
},
{'name': 'Abdullah',
	'surname': 'Atalar',
	'age': 60
}]


pfile = open('people.txt', 'w')

for person in people:
	pfile.write(person['name'] + ' ' + person['surname'] + ' ' + str(person['age']) + '\n')

pfile.close()



	


