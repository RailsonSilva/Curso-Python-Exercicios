print('===== DESAFIO 31 =====')
print('===== Valor da passagem =====')
km = float(input('Digite a distância da viagem(km): '))
if km <= 200:
    print('O valor da passagem vai ser de R${:.2f}!'.format(km * 0.5))
else:
    print('O valor da passagem vai ser de R${:.2f}!'.format(km * 0.45))
