name = 'Mateus'
surname = 'Balda'
lastname = 'Mota'

nameNew = ' '.join([name, surname, lastname])

nameNew2 = nameNew.split()
nameNew2 = nameNew2[0] + ' ' + nameNew2[2]

print(nameNew2)