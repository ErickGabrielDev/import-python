#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. calcule e mostre o comprimento da hipotenusa.
from math import hypot
#a biblioteca hypot mostra o valor da hipotenusa através dos catetos
co = float(input('informe o valor do cateto oposto: '))
ca = float(input('informe o valor do cateto adjacente: '))
print(f'O comprimento da hipotenusa é igual a: {hypot(co, ca):.2f}')