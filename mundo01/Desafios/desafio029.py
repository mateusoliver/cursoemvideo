print('Qual a velocidade do carro')
velocidade = int(input('Velocivade? '))
if velocidade > 80:
    print('Voce foi multado e recebeu uma multa!')
    valor = (velocidade - 80)
    print('O valor da sua multa sera de  {}'.format(valor*7), 'reais')
else:
    print('Você esta dentro do limite de velocidade')
