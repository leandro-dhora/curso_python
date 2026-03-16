# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
angulo = float (input('Digite um angulo em graus: '))
rad = math.radians(angulo) 
sin = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)
print(f'Seno = {sin:.2f}\nCosseno = {cos:.2f}\nTangente = {tan:.2f}')