km = int(input('Qual a distancia da viagem: '))
if km <= 200:
    print('O preço de sua viagem será de R$ {}'.format(km * 0.50), 'reais')
else:
    print('O preço de sua vagem será de R$ {}'.format(km * 0.45), 'reais')
