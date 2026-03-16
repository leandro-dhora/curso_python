# CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE:
# O NOME COM TODAS AS LETRAS MAIUSCULAS
# O NOME COM TODAS MINUSCULAS
# QUANTAS LETRAS AO TODO (SEM CONSIDERAR ESPACOS)
# QUANTAS LETRAS TEM O PRIMEIRO NOME

nome = str (input('Qual o seu nome completo? ')).strip()
maiusculo = nome.upper()
minusculo = nome.lower()
sem_espaco = len(nome) - nome.count(' ')
primeiro = nome.split()

print(f'Seu nome todo em MAIUSCULO: {maiusculo}')
print(f'Seu nome todo em minusculo: {minusculo}')
print(f'Seu nome tem {sem_espaco} letras')
print(f'Seu primeiro nome e {primeiro[0]} e tem {len(primeiro[0])} letras')