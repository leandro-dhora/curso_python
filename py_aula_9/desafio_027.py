# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = str (input('Digite seu nome completo: ')).strip()
primeiro = nome.split()[0]
ultimo = nome.split()[-1]
print(f'Prazer em te conhecer!\nSeu primeiro nome é: {primeiro}\n E seu ultimo nome é: {ultimo}')   