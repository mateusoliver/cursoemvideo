num01 = int(input('Entre com o primeiro valor: '))
num02 = int(input('Entre com o segundo valor: '))
if num01 > num02:
    print('O número {} é maior do que o número {} '.format(num01,num02))
elif num02 > num01:
    print('O número {} é maior do que o número {} '.format(num02,num01))
elif num01 == num02:
    print('Não existe número maior do que o outro')
else:
    print('Valor inválido!')