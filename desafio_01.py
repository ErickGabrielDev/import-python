#Crie um programa que leia um número real e mostrem na tela a sua porção inteira. ex:6.127, porção inteira é 6.
from math import trunc 
#através da biblioteca trunc oque vier depois da ', ou .' não sera mostrado.
num = float(input('Digite um número: '))
print(f'O número digitado foi {num} e a sua parte inteira é igua a: {trunc(num)}')
