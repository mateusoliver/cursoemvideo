preco = float(input('Entre com o preço do produto: '))
print('-'*48)
print('-'*5, 'Escolha a forma de pagamento:', '-'*5)
print('1 - À vista, espécie ou cheque: 10% de desconto.')
print('2 - à vista no cartão: 5% de desconto.')
print('3 - 2x no cartão: preço normal.')
print('4 - 3x ou mais no cartão: 20% de juros')
print('-'*48)
forma = int(input('Escolha o número da forma de pagamento, por favor: '))

if forma == 1:
    print('Você irá pagar R$ {}'.format(preco-(preco*10/100)))
elif forma == 2:
    print('Você irá pagar R$ {}'.format(preco - (preco * 5/100)))
elif forma == 3:
    print('Você ira pagar em 2 X de R$ {}, totalizando R$ {} '.format(preco/2,preco))
elif forma == 4:
    parcelas = int(input('Informe a quantidade de parcelas: '))
    print('Você irá pagar em {} parcelas com 20% de juros.'.format(parcelas))
    print('Seu pagamento irá ficar em {} parcelas de R$ {}'.format(parcelas,(preco+(preco*20/100))/parcelas))
    print('Totalizando {}'.format((preco+(preco*20/100))))
else:
    print('Valor inválido!')



# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condições
# de pagamento:
# - à vista dinheiro e cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros