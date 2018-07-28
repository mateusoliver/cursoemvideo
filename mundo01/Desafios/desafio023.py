numero = int(input('Entre com um numero de 0 - 9999: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('Analisando o numero {}'.format(numero))
print('A unidade do número {} é {}'.format(numero,u))
print('A dezena do número {} é {}'.format(numero,d))
print('A centena do número {} é {}'.format(numero,c))
print('A milhar do número {} é {}'.format(numero,m))