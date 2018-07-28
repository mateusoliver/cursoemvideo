from datetime import date
ano = int(input('Qual o ano do seu nascimento: '))
atual = (date.today().year)
if atual - ano <= 9:
    print('MIRIM')
elif atual - ano <= 14:
    print('INFANTIL')
elif atual - ano <= 19:
    print('JUNIOR')
elif atual - ano <= 20:
    print('SÊNIOR')
elif atual - ano > 20:
    print('MASTER')