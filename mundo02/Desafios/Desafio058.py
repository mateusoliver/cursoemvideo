import time
from random import randint

cont = 0
print('O computador esta pensando em um número')
pcnum = int(randint(0,9))
#time.sleep(4)
eunum = 's'
while pcnum != eunum:
    eunum = int(input('Tente advinhar o número que o computador pensou. Digite: '))
    if pcnum != eunum:
        cont += 1
        print('O pc pensou no número {}'.format(pcnum))
        print('tente novamente!')
    elif pcnum == eunum:
        print('Errou {} vezes, até acertar!!'.format(cont))
        print('O pc pensou no número {} e você disse o número {}.'.format(pcnum,eunum))