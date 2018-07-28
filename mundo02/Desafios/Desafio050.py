somaimpar = 0
somapar = 0
for n in range(1,7):
    num = int(input('Digite o {}º número: '.format(n)))
    if num % 2 == 0:
        somapar += num
    if num % 3 == 1:
        somaimpar += num
print('a soma de todos os numero pares é {}!'.format(somapar))
print('a soma de todos os numero impares é {}!'.format(somaimpar))