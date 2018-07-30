n = int(input('Digite um número: '))
divisoes = 0
for c in range(1, n + 1):
    if n % c == 0:
        divisoes += 1
        print('\033[;1m\033[1;34m{}'.format(c),end=' ')
    else:
        print('\033[1;31m{}'.format(c),end=' ')
print('\n\033[0;0mO número {0} possui {1} divisões.'.format(n, divisoes))
if divisoes == 2:
    print('O número {0} é primo.'.format(n))
else:
    print('O número {0} não é primo!'.format(n))
