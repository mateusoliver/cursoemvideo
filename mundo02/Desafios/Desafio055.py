maior = 0
menor = 0
for n in range(1,6):
    peso = float(input('Entre com o peso da {}ª pessoa (Kg): '.format(n)))
    if n == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O peso maior é {}Kg'.format(maior))
print('O peso menor é {}Kg'.format(menor))