n = int(input("Digite um valor: "))

fatorial = 1
print('{}! = '.format(n),end='')
while  n > 0 :
    fatorial = fatorial * n
    if n > 1:
        print('{}x'.format(n),end='')
    elif n == 1:
        print('{} = '.format(n),end='')
    n -= 1

print(fatorial)