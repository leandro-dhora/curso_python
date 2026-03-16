# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math
opo = float (input('Qual valor do cateto oposto? '))
adj = float (input('Qual o valor do cateto adjacente? '))
hip = math.hypot(opo, adj)
print(hip)
