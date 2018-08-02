a1 = int(input('Digite o primeiro termo da PA :'))
r = int(input('Digite a razão:'))
an = int(input('Digite o ultimo termo que desejas: '))
a10 = a1 + (an - 1) * r

for c in range(a1,a10 + r, r):
    print('{}'.format(c), end=' → ')
print('Acabou!')

# a1    -> primeira razão da PA
# r     -> razão da PA
# a10   -> Formula da PA
# an    -> Ultimo termo