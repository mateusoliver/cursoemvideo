ano = int(input('Entre com o ano: '))
teste01 = ano % 4
teste02 = ano % 100
teste03 = ano % 400
#print(teste01)
#print(teste02)
#print(teste03)

if teste02 != 0 and teste01 == 0 or teste03 == 0:

    print('Este ano é bissexto')
else:
    print('Este ano NÃO é bissexto')





#ano = int(input('Digite o ano: '))
#if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
#print('É um ano bissexto')
#else:
#print('Não é bissexto')
