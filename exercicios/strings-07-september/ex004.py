# Peça ao usuário para inserir uma frase ou uma palavra. Em seguida,
# crie um programa que conte quantas vogais e consoantes estão presentes na
# entrada. Exiba os resultados.

phrase = input('Digite uma frase ou palavra: ').lower()

vowels = phrase.count('a') + phrase.count('e') + phrase.count('i') + phrase.count('o') + phrase.count('u')
phraseNotSpace = phrase.replace(' ', '')
consonants =  len(phraseNotSpace) - vowels

print('Vogais: '+str(vowels))
print('Consoantes: '+str(consonants))
