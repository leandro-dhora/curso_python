# ESCREVA UM PROGRAMA QUE LEIA UM NUMERO INTEIRO QUALQUER E MOSTRE NA TELA A SUA TABUADA
num = int(input("Digite um número inteiro: "))

print(f"\nTabuada do {num}:\n")

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
