valor_casa = float(input('Entre com o valor da casa: R$'))
salario = float(input('Entre com o salário do comprador: '))
anos = int(input('Em quantos anos ele irá pagar a casa? '))
prestacao = valor_casa / (anos * 12)

print('Seu salário menos 30%: R$ {}'.format(salario - (salario * 30/100)))
if (salario - (salario * 30/100)) <= prestacao:
    print('Você não esta em condições de comprar a casa.')
else:
    print('Aceito com sucesso! ')
print('Você irá pagar {} parcelas de R$ {:.2f} reais'.format(anos*12,prestacao))