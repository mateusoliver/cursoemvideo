a1 = int(input('Digite o primeiro termo da PA :'))
r = int(input('Digite a razão:'))
an = int(input('Digite o ultimo termo que desejas: '))
termos = an
while an >=1:
    print(a1,end=' -> ')
    a1 = a1 + r
    an -= 1
    if an == 0:
        an = int(input('\n^Você deseja mostrar mais quantos termos?'))
        termos = termos + an
        pass
    if an == 0:
        print('Voce exibiu {} termos!'.format(termos))
        exit()
print('ACABOU!!')