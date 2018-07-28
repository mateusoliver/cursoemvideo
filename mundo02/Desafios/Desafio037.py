num = int(input('Entre com algum número: '))
escolha = int(input('Digite 1 - (Binário), 2 - (Octal) e 3 - (Hexadecimal)'))
if escolha == 1:
    print('o valor em binario é: {} '.format(bin(num)))
elif escolha == 2:
    print('o valor em binario é {} '.format(oct(num)))
elif escolha == 3:
    print('o valor em binario é {} '.format(hex(num)))
else:
    print('Valor inválido!')