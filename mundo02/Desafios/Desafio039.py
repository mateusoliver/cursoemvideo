from datetime import date
ano = int(input('Entre com o ano do seu nascimento, por favor.'))

ano_atual = (date.today().year)
#print(type(date.today().year))

print('Sua idade é de {} aninhos'.format(ano_atual-ano))
print('-'*20)
if ano_atual - ano < 18:
    print('Você ainda vai se alistar no exército! Boa sorte!')
    print('Falta {} anos para você se alistar!! '.format(18-(ano_atual-ano)))
elif ano_atual - ano == 18:
    print('Esta na hora de se alistar no exército! Corre la, é obrigatório!')
elif ano_atual - ano > 18:
    print('Já passou da hora de se alistar, certamente ja fez isso!')
    print('Já se passaram {} anos do seu alistamento'.format((ano_atual-ano)-18))