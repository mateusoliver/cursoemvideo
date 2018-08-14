upmil = total_gastos = 0
p_barato = 9999999
r = 'S'
while r == 'S':
    nome = str(input('Nome do produto: '))
    preco = int(input('Preço do produto: '))
    # 1 - SOMANDO TODAS AS COMPRAS
    total_gastos = total_gastos + preco
    # 2 - CONTABILIZANDO PRODUTOS ACIMA DE 1 MIL REAIS
    if preco > 1000:
        upmil = upmil + 1
    # 3 - MOSTRAR O NOME DO PRODUTO MAIS BARATO
    if preco < p_barato:
        p_barato = preco
        nome_p_barato = nome
    r = str(input('Deseja continuar? [S/N]')).upper()
print('-'*20)
print(f'O total de gastos será de R${total_gastos}! ')
print('-'*20)
print(f'{upmil} produto(s) custa(m) mais de R$1000! ')
print('-'*20)
print(f'{nome_p_barato} é o produto mais barato que custa R${p_barato} ')
print('-'*20)












#upmil = produtos aciman de mil reais
#p_barato = produto mais barato
