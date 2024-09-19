#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians, sin, cos, tan
#a biblioteca 'radians' é usada para converter para radiano, e o 'sin' calcula o seno, o 'cos' o cosseno e o 'ran' calcula a tangente.
ângulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(ângulo))
print(f'O ângulo de: {ângulo} tem o Seno de: {seno:.2f}')
cosseno = cos(radians(ângulo))
print(f'O ângulo de: {ângulo} tem o Cosseno de: {cosseno:.2f}')
tangente = tan(radians(ângulo))
print(f'O ângulo de: {ângulo} tem a tangente de: {tangente:.2f}')