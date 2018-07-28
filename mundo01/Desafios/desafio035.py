a = int(input('entre com o primeiro lado: '))
b = int(input('entre com o terceiro lado: '))
c = int(input('entre com o segundo lado: '))
#nome = 'mateus oliveira'
#cores = {'limpa':'\033[m',
#         'azul':'\33[34m',
#         'amarelo':'\033[7;30m'}
#print('olá mundo. prazer em te conhecer, {}{}{}'.format(cores['azul'],nome,cores['limpa']))

if a < b + c and b < a + c and c < a + b:
    print('\033[31m Existe um triangulo')
else:
    print('\033[4;30;45m Não existe triangulo\033[m!!!')