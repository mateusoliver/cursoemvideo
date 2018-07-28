nota01 = float(input('Entre com a primeira nota, por favor: '))
nota02 = float(input('Entre com a segunda nota, por favor: '))
media = (nota01+nota02)/2

if media < 5.0:
    print('REPROVADO')
elif media >5 and media <6.9:
    print('RECUPERAÇÃO')
elif media >= 7.0:
    print('APROVADO!! PARABÉNS!!')