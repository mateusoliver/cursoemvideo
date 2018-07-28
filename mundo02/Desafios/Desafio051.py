
a1 = int(input('Digite o primeiro termo da PA:'))
r = int(input('Digite a razão:'))
a10 = a1 + 9 * r

for c in range(a1,a10 + r, r):
    print('{}'.format(c), end=' → ')
print('Acabou!')

