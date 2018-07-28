from datetime import date
ano_atual = (date.today().year)
for n in range (0,7):
    ano = int(input('Qual o ano do seu nascimento: '))
    if ano_atual - ano >= 21:
        print('Você é maior de idade sim! Você tem {} anos!!'.format(ano_atual-ano))
    else:
        print('você é de menor, tu só tem {} anos pirralho!!'.format(ano_atual-ano))