a1 = int(input('Digite o primeiro termo da PA :'))
r = int(input('Digite a razão:'))
an = int(input('Digite o ultimo termo que desejas: '))

while an >=1:
    print(a1,end=' -> ')
    a1 = a1 + r
    an -= 1
    if an == 0:
        an = int(input('\nvoce deseja mostrar mais quantos termos?'))
        pass
    if an == 0:
        exit()
print('ACABOU!!')