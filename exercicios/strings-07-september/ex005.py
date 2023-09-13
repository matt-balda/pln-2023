# Desenvolva um programa que verifique se uma palavra ou frase
# inserida pelo usuário é um palíndromo. Um palíndromo é uma palavra, frase ou
# sequência de caracteres que permanece a mesma quando lida de trás para frente.
# Por exemplo, "radar" é um palíndromo. O programa deve informar se a entrada é
# ou não um palíndromo.

phraseOrWord = input('Digite uma frase ou palavra: ').lower()

phraseOrWord = phraseOrWord.replace(' ', '')   

if phraseOrWord == phraseOrWord[::-1]:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')
