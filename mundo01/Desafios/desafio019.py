import random
aluno1 = input('Entre com o primeiro aluno, por favor: ')
aluno2 = input('Entre com o segundo aluno, por favor: ')
aluno3 = input('Entre com o terceiro aluno, por favor: ')
aluno4 = input('Entre com o quarto aluno, por favor: ')

pessoas = [aluno1, aluno2, aluno3, aluno4]
#pessoas = ['carlos','marcos','silvana','carol']
print('O sortudo foi o {}'.format(random.choice(pessoas)))