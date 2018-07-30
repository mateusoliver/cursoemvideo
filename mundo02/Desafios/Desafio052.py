n = int(input('Digite um número: '))
cont = 0
for c in range(1, n + 1):
    if n % c == 0:
        cont += 1
        print('\033[;1m\033[1;34m{}'.format(c),end=' ')
    else:
        print('\033[1;31m{}'.format(c),end=' ')
print('\n\033[0;0mO número {0} possui {1} divisões.'.format(n, cont))
if cont == 2:
    print('O número {0} é primo.'.format(n))
else:
    print('O número {0} não é primo!'.format(n))