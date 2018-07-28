a = int(input('entre com o primeiro lado: '))
b = int(input('entre com o terceiro lado: '))
c = int(input('entre com o segundo lado: '))

if a < b + c and b < a + c and c < a + b:
    print('\033[31m Existe um triangulo! ', end='')

    # VERIFICANDO SE O TRIANGULO É ESCALENO, ISÓCELES OU EQUILÁTERO
    if a != b and a != c:
        print('Triângulo Escaleno!') # todos os lados difetentes
    elif a == b and a != c:
        print('Triângulo isósceles!')#dois lados iguais
    elif a == b and a == c:
        print('Triângulo Equilátero!')

else:
    print('\033[4;30;45m Não existe triangulo\033[m!!!')

