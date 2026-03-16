# Desenvolva um programa que pergunte a distância de uma viagem em Km. 
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

d = int(input('Quantos Km foram percorridos durante a viagem? '))
if d<=200:
    print(f'O preço da passagem corresponde a: {d*0.50:.2f}R$')
else:
    print(f'O preço da passagem corresponde a: {d*0.45:.2f}R$')
print('Tenha um ótimo dia!')