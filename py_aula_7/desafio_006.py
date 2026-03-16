# CRIE UM ALGORITITMO QUE LEIA UM NUMERO E MOSTRE O SEU DOBRO, TIPLO E RAIZ QUADRADA
from math import sqrt
n = float (input ('Digite um numero: '))
dobro = n*2
triplo = n*3
raiz = sqrt(n)
print('O dobro do numero e: {}, triplo e: {} e a raiz quadrada e: {}' .format(dobro, triplo, raiz))