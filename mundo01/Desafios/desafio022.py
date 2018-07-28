nome = str(input('Entre com seu nome completo, por favor: ')).strip()
#print('Todas as letras em mauísculo: ', nome.upper())
#print('Todas as letras em minusculo: ', nome.lower())
#print('Contando com os espaços: ', len(nome))
#print('Não contando com os espaços: ', len(nome) - nome.count(' '))


print('Todas as letras em maiúsculo: {}'.format(nome.upper()))
print('Todas as letras em minúsculo {}'.format(nome.lower()))
print('Seu nome tem ao total {} letras'.format(len(nome) - nome.count(' ')))
divisao = nome.split()
print(divisao[0])
print('O primeiro nome é >> {} << e tem {} letras'.format(divisao[0], len(divisao[0])))

