#Um professor quer sortear um dos seus quatro alunos para apagar um quadro. faça um programa que ajude ele, lendo o nome deles e escrevendo na tela.
from random import choice
#a biblioteca 'choice' faz uma escolha aleatoria dentro de uma lista.
aluno1 = input('Digite um nome: ')
aluno2 = input('Digite outro nome: ')
aluno3 = input('Digite outro nome: ')
aluno4 = input('Digite outro nome: ')
print(f'O aluno escolhido foi o: {choice([aluno1, aluno2, aluno3, aluno4])}')