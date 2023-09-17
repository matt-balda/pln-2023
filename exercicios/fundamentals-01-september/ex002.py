string = 'Aqui é zero(0), outro zero(0) e mais outro zero(0)'

novaString = string.split('0')
novaString = '1'.join(novaString)

novaString2 = ''

for l in string:
    if l == '0':
        novaString2 += '1'
    else:
        novaString2 += l

print('Usando split e join: ' + novaString)
print('Usando for in' + novaString2)