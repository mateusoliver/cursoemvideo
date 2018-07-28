from random import randint
print('O computador esta pensando em um número')
pcnum = int(randint(0,5))
#print(pcnum)
eunum = int(input('Tente advinhar o número que o computador pensou. Digite: '))
if eunum == pcnum:
    print('Acertou miseravi')
else:
    print('Errou abestado!')
