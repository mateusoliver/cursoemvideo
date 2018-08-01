r = 'S'
while r == 'S':
    n = str(input('Digite o seu SEXO [F] ou [M]: ')).upper()
    if n == 'F':
        print('Sexo FEMININO')
    elif n == 'M':
        print('Sexo MASCULINO')
    else:
        print('valor inválido')
    r = str(input('Quer continuar? [S] para sim!!')).upper()
print('FIM')
##