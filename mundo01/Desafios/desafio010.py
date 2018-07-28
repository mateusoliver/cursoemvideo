valor = int(input('Quantos reais(R$) você tem em sua carteira: '))
dolar = 3.27
print(type(dolar))
print('Com R${} você pode comprar ${:.2f} dolares'.format(valor,valor/dolar))