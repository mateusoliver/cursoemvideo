valor_casa = float(input('Entre com o valor da casa: R$'))
salario = float(input('Entre com o salário do comprador: '))
anos = int(input('Em quantos anos ele irá pagar a casa? '))
prestacao = valor_casa / (anos * 12)
salario_min = salario - (salario * 30/100)
print('Salario menos de 30%: R$' , salario_min)
if salario_min <= prestacao:
    print('Você não esta em condições de comprar a casa.')
else:
    print('Aceito com sucesso! ')
print('O valor da prestação será de {:.2f}'.format(prestacao))