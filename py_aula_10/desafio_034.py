# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input('Digite seu salario: R$'))
if sal > 1250:
    print(f'Com o aumento seu salario passa a ser R${sal*1.1:.2f}')
else:
    print(f'Com o aumento seu salario passa a ser de {sal*1.15:.2f}')
