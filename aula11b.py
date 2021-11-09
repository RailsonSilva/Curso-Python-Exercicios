print('\033[7;30mOlá, Mundo!\033[m')

# Cancelar formatação
a = 4
b = 6
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))

# .format()
nome = 'Railson'
print('Muito prazer em te conhecer {}{}{}!!!'.format('\033[1;30;41m', nome, '\033[m'))

# Predefinir cores
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}

print('Muito prazer em te conhecer {}{}{}!!!'.format(cores['pretoebranco'], nome, cores['limpa']))