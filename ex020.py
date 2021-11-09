from random import shuffle
print('===== DESAFIO 20 =====')
nome1 = str(input('Digite o nome do aluno 1: '))
nome2 = str(input('Digite o nome do aluno 2: '))
nome3 = str(input('Digite o nome do aluno 3: '))
nome4 = str(input('Digite o nome do aluno 4: '))
nomes = [nome1, nome2, nome3, nome4]
(shuffle(nomes))
print('A ordem de apresentação é:')
print(nomes)
