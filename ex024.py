print('===== DESAFIO 24 =====')
print('Sua cidade começa com a palavra "SANTO"?')
cidade = str(input('Digite o nome da sua cidade: '))
inicio = cidade.split()
inicio[0] = inicio[0].upper()
print("SANTO" in inicio[0])

# ooouu
# cidade = str(input('Digite o nome da sua cidade: ')).strip()
# print(cid.[:5].upper() == 'SANTO')
