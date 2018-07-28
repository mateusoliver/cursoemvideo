n = int(input('Digite um número: '))

divisoes = 0
for c in range(n, 0, -1):
    if n % c == 0:
        divisoes += 1

print('O número {0} possui {1} divisões.'.format(n, divisoes))

if divisoes == 2:
    print('O número {0} é primo.'.format(n))
else:
    print('O número {0} não é primo.'.format(n))

        ###2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79,