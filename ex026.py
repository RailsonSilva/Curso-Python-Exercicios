print("===== DESAFIO 26 =====")
frase = str(input('Digite uma frase: ')).upper().strip()
print('Quantas letras A tem: {}'.format(frase.count('A')))
print('A primeira posição que o A aparece é: {}° posição!'.format(frase.find('A')+1))
print('A ultima posição que o A aparece é: {}° posição!'.format(frase.rfind('A')+1))

