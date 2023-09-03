phrase1 = 'Aqui é a primeira frase de um texto qualquer para a disciplina de processamento de linguagem natural. '
phrase2 = "Aqui é a segunda frase de um texto qualquer para a disciplina de processamento de linguagem natural."

stringNew = phrase1[::-1].replace('A', '*').replace('a', '*').replace('E', '+').replace('e', '+')

stringNew2 = phrase2[::-1].replace('A', '*').replace('a', '*').replace('E', '+').replace('e', '+')


print('Primeira frase: ' + stringNew)
print('Segunda frase: ' + stringNew2)
