n = int(input("Digite um valor: "))

fatorial = 1
print('{}! = '.format(n),end='')
while  n > 0 :
    fatorial = fatorial * n
    print(' {} '.format(n), end='')
    print('x' if n > 1 else '= ', end='')
    n -= 1

print(fatorial)

############## USANDO METODO DO PYTHON ###################
'''from math import factorial
n = int(input('Entre com o valor: '))
f = factorial(n)
#print('O fatorial de {} é {}'.format(n,f))
print(f'O fatorial de {n} é {f}')'''