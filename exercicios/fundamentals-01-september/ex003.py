name = 'MATEUS'
nameNew = ''

for l in name:
    n = l.replace(l, l.lower())
    nameNew += n

print('Usando lower(): ' + name.lower())
print('Usando for in: ' + nameNew) 