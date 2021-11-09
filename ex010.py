print('===== DESAFIO 10 =====')
real = float(input('Quantos reais você tem na sua carteira? R$'))
dolar = real / 3.27
print('Você pode comprar US${:.2f} com R${:.2f}!' .format(dolar, real))
