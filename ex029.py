print('===== DESAFIO 29 =====')
velocidade = float(input('Digite a velocidade do carro: '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Ora ora, temos um infrator aqui!')
    print('Você está sendo MULTADO por excesso de velocidade e o valor da multa é de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
