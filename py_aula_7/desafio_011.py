# FACA UM PROGRAMA QUE LEIA A ALTURA E A LARGURA DE UMA PAREDE EM METROS,
# CALCULE A SUA AREA E A QUANTIDADE DE TINTA NECESSARIA PARA PINTA-LA, SABENDO QUE CADA LITRO DE TINTA, PINTA UMA AREA DE 2m²

h = float (input('Qual a altura da parede em metros? '))
lar = float (input('Qual a largura da parede em metros? '))
area = h*lar
tinta = area/2

print(f'A area da sua parede e: {area}m²\nTinta necessaria: {tinta}L')
