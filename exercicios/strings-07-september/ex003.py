# Solicite ao usuário que insira uma frase e, em seguida, peça que ele
# forneça duas palavras: uma palavra a ser substituída e uma palavra de
# substituição. Seu programa deve substituir todas as ocorrências da primeira
# palavra na frase pela segunda palavra e exibir a frase resultante. Por exemplo, se
# o usuário inserir a frase "Eu gosto de programar em Python" e escolher "Python"
# como palavra a ser substituída e "Java" como palavra de substituição, o programa
# deve exibir "Eu gosto de programar em Java".

phrase = input('Digite uma frase: ')
print('Frase:\n'+phrase)
word = input('Digite uma palavra a ser substituída: ')
newWord = input('Digite uma palavra de substituição: ')
newPhrase = phrase.replace(word, newWord)

print(newPhrase)