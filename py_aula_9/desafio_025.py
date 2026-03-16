# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str (input('Nome completo: ')).strip()
verif = 'silva' in nome.lower
print(f'Esse nome tem Silva? {verif}')