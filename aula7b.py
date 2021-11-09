n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
a = n1 + n2
s = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}!' .format(a))
print('A subtração é {}!' .format(s))
print('A multiplicação é {}!' .format(m))
print('A divisão é {:.3f}!' .format(d))
print('A divisão inteira é {}!' .format(di))
print('A potência de {} elevado a {} é {}!' .format(n1, n2, e))
