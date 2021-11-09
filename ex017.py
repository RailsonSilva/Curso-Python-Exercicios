import math
print('===== DESAFIO 17 =====')
co = float(input('Digite o valor do Cateto Oposto: '))
ca = float(input('Digite o valor do Cateto Adjacente: '))
h = math.hypot(co, ca)
# h = math.sqrt(math.pow(co, 2) + math.pow(ca, 2))
# h = (co ** 2 + ca ** 2) ** (1/2)
print('O valor da hipotenusa é: {}'.format(h))
