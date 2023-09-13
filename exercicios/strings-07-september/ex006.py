# Crie um programa que solicite ao usuário que insira uma palavra ou
# frase e, em seguida, exiba essa entrada de forma reversa. Por exemplo, se o
# usuário inserir "Python", o programa deve exibir "nohtyP".

phraseOrWord = input('Digite uma frase ou palavra: ')

phraseOrWord = phraseOrWord[::-1]

print(phraseOrWord)