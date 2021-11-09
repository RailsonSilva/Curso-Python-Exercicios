print('===== DESAFIO 34 =====')
print('===== Aumentando os salários =====')
salario = float(input('Digite o valor do seu salário: '))
if salario > 1250.00:
    aumento = (salario * 0.1) + salario
    print('O seu salário irá aumentar para R${:.2f}!'.format(aumento))
else:
    aumento = (salario * 0.15) + salario
    print('O seu salário irá aumentar para R${:.2f}!'.format(aumento))
