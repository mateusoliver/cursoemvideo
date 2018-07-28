s = 0
cont = 0
for n in range(1,500,2):
    #print(n)
    if n % 3 == 0:
        cont += 1
        s += n
print('{} numeros foram somados'.format(cont))
print('a soma de todos é: {}'.format(s))
print('fim')