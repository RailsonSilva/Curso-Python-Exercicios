print('===== DESAFIO 11 =====')
altura = float(input('Qual a altura da parede(em metros)? '))
largura = float(input('Qual a largura da parede(em metros)? '))
area = altura * largura
tinta = area / 2
print('A área da parede é: {}m²\nA quantidade de tinta necessária é: {:.3}l' .format(area, tinta))
