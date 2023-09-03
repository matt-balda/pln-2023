lista = ['Mateus', 23, 29, 'Paulo', 'Maria', 'Jorge', 'Ana', 'Lucas', 'João', 'Pedro']
print('Tamanho da lista: ' + str(lista.__len__()))
print('Lista: '+ str(lista))

lista.pop(4)
lista.pop(5)
lista.pop(6)

print('Lista atualizada: '+ str(lista))