# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str (input('Digite uma frase: ')).strip().upper()
contador = frase.count('A')
inicial = frase.find('A')+1
final = frase.rfind('A')+1

print(f'Na frase "{frase}" encontra-se {contador} letras A')
print(f'A posicao da primeira letra A > {inicial}') 
print(f'A posicao da ulima letra A > {final}')