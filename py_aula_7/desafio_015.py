# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float (input ('Km percorridos: '))
d = int (input('Dias de aluguel: '))
ckm = km*0.15
cdia = d*60
t = ckm + cdia

print(f'O valor gasto com KM foi de: {ckm}R$\nO valor gasto com aluguel foi de: {cdia}R$\nTotal = {t}R$')