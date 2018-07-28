nome = str(input('Entre com seu nome: '))
if nome.lower() == 'mateus':
    print('Nome belo!')
elif nome in 'ana rafael lucas':
    print('seu nome é tao normal.')
else:
    print('é, então ta!')
print('Tenha um bom trabalho {}!'.format(nome))