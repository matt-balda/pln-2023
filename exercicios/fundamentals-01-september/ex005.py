list = ['Mateus', 23, 29, 'Paulo', 'Maria', 'Balda', 'Ana', 'Lucas', 'João', 'Pedro']
print('Tamanho da lista: ' + str(list.__len__()))
print('Lista: '+ str(list))

list.pop(4)
list.pop(4)
list.pop(4)

print('Tamanho da lista: ' + str(list.__len__()))
print('Lista atualizada: '+ str(list))