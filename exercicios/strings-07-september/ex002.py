# Solicite ao usuário que insira uma frase. Seu programa deve inverter
# a ordem das palavras na frase e exibi-la de trás para frente. Por exemplo, se o
# usuário inserir "Python é divertido", o programa deve exibir "divertido é Python".

string = input('Digite uma frase: ')
words = string.split() ## transforma em uma lista com as palavras
invertedWords = words[::-1]
print(' '.join(invertedWords))


