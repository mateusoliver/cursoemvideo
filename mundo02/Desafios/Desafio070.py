total_gastos = 0
r = 'S'
while r == 'S':
    nome = str(input('Nome do produto: '))
    preco = int(input('Preço do produto: '))
    # 1 - SOMANDO TODAS AS COMPRAS
    total_gastos = total_gastos + preco
    # 2 - CONTABILIZANDO PRODUTOS ACIMA DE 1 MIL REAIS
    if preco > 1000:
        upmil = upmil + 1

    r == str(input('Deseja continuar? [S/N]'))
print(f'O total de gastos será de R${total_gastos}')
print(f'{upmil} produtos custam mais de R$1000')
#print(f'{p_barato} é o produto mais barato')












#upmil = produtos aciman de mil reais
#p_barato = produto mais barato
