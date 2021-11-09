from random import randint, choice
from time import sleep
print('===== DESAFIO 28 =====')
numero_escolhido = randint(0, 5) #sorteia um numero entre 0 e 5
print('É capaz de vencer o ''Aleatório''?\nTente vencer o computador, acerte o número...')
x = int(input('Escolha um número de 0 a 5: ')) #usuário entra com o número
print('PROCESSANDO...')
sleep(3) #comando para fazer o programa "dormir"
if x == numero_escolhido:
    print('Parabéns, você conseguiu!')
else:
    elses = ['Perdeu kkkk', 'Ruim demais kkk, perdeu', 'Perdeu pro computador kkkk', 'Tenta denovo, você perdeu kkk']
    print(choice(elses))