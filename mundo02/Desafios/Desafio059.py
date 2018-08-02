resp = 1
while resp != 'S':
    print('Programa Iniciado!!')
    num01 = int(input('Entre com o primeiro valor: '))
    num02 = int(input('Entre com o segundo valor: '))
    print('######## MENU ########')
    print('Digite [1]-Somar os valores!')
    print('Digite [2]-Multiplicar os valores')
    print('Digite [3]-Qual o maior valor!')
    print('Digite [4]-Digitar novos valores!')
    print('Digite [5]-Sair do programa!')
    menu = int(input('Digite o que deseja: '))
    if menu == 1: 
        print('A soma dos valores é: {}'.format(num01+num02))
    if menu == 2:
        print('A multiplicação dos valores é = {}!'.format(num02*num01))
    if menu == 3:
        if num01 > num02:
            print('O número {} é maior do que o número {}.'.format(num01,num02))
        else:
            print('O número {} é maior do que o número {}.'.format(num02,num01))
    if menu == 4:
        print('Solicitação de incerir novos valores!!')
        pass
    if menu == 5:
        print('Programa finalizado com sucesso! Volte sempre!')
        exit()
