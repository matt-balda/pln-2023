# Peça ao usuário para inserir uma frase. Seu programa deve
# encontrar e exibir a palavra mais longa na frase. Você pode considerar que as
# palavras são separadas por espaços em branco. Por exemplo, se o usuário inserir
# "Python é uma linguagem de programação poderosa", o programa deve exibir
# "programação" como a palavra mais longa.

phrase = input('Digite uma frase: ').strip()

phrase = phrase.split()

higherNumber = 0
higherWord = ''

for i in range(len(phrase)):
    if len(phrase[i]) > higherNumber:
        higherNumber = len(phrase[i])
        higherWord = phrase[i]

print('A maior palavra é: {}'.format(higherWord))
print('E ela tem {} letras'.format(higherNumber))