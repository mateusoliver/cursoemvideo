contador = 0
idade = 0
media = 0
for n in range(0,3):
    nome = str(input('Qual é seu nome: '))
    idade = int(input('Qual sua idade: '))
    sexo = str(input('Qual o seu sexo M(masculino) ou F(feminino)'))
    media += idade
    if idade > idade and sexo == 'M':
        idade += idade
        nome += nome
    if sexo == 'F' and idade <= 20:
        contador += 1
print('A média de idade do grupo é: {}'.format(media/2))
print('{} é o mais velhor com {} anos!'.format(nome,idade))
print('A quantidade de mulheres menores de 20 anos é : {}'.format(contador))
