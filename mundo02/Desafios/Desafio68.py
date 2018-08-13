from random import randint
print('-='*20)
print('Vamos brincar de PAR ou ÍMPAR')
print('-='*20)
num01 = int(input('Entre com o seu valor humano: '))
print(f'Humano você digitou o número : {num01}')
num02 = randint(0,9)
print(f'Eu escolho o número {num02}')
while True:
    if num01 == num02:
        print(f'Você jogou {num01} e eu joguei {num02}.')
        print('VOCÊ VENCEU')
    else:
        print('-='*20)
        print('VOCÊ PERDEU')
        print(f'Você jogou {num01} e eu joguei {num02}.')
        print('-='*20)
        break
