# Peça ao usuário que insira uma string que contenha espaços em
# branco extras no início ou no final. Crie um programa que remova esses espaços
# extras e exiba a string resultante.

string = input('Digite uma frase com espaço branco no início ou final: ')
print('Com os espaços:'+string+'.')
print('!'+string.strip()+'!')