# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
from time import sleep
numero = random.randint(0,5)
escolhido = int(input('Escolha um número entre 0 e 5: '))
print('E você...')
sleep(2)
if escolhido == numero:
    print(f'Acertou! o número foi {numero}')
else:
    print(f'Errou otário! O número era {numero}')