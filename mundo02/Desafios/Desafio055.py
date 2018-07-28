maior = 0
menor = 0
for n in range(1,6):
    peso = int(input('Entre com o seu peso: '))
    if peso > maior:
        maior = peso
    else:
        menor = peso
print('O peso maior é {}'.format(maior))
print('O peso menor é {}'.format(menor))