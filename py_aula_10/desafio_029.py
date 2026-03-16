#  Escreva um programa que leia a velocidade de um carro.
#  Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

v = int(input('Km/h: '))
abaixo = 80-v
exesso = v-80
multa = exesso*7
if v>80:
    print(f'Você foi multado no valor de {multa}R$')
    print(f'Com uma velocidade de {exesso}Km/h acima do permitido!')
else:
    print(f'Sem multa.')
    print(f'Velocidade de {abaixo}Km/h abaixo do permitido, Continue assim!')
print('Tenha um bom dia! Dirija com segurança.')
