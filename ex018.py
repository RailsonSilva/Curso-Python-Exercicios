from math import sin, cos, tan, radians
print('===== DESAFIO 18 =====')
x = int(input('Digite um Ângulo: '))
print('O seno do ângulo de {}° é {:.2f}.'.format(x, sin(radians(x))))
print('O cosseno do ângulo de {}° é {:.2f}.' .format(x, cos(radians(x))))
print('E a tangente do ângulo de {}° é {:.2f}.' .format(x, tan(radians(x))))
