salario = float(input('Qual é o seu salário: '))
if salario > 1250.00:
    print('Seu aumento será de {} '.format(salario + salario * 10/100))
else:
    print('Seu salário será de {} '.format(salario + salario * 15/100))