# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
n = int(input('Digite um número: '))
if n%2 == 0:
    print(f'{n} É PAR!')
else:
    print(f'{n} É IMPAR!')