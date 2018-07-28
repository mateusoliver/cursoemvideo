peso = float(input('Qual é o seu peso? '))
altura = float(input('Qual é sua altura? '))
imc = peso / (altura**2)
print('seu imc é de: {:.2f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif imc > 18.5 and imc <= 25:
    print('Ideal')
elif imc > 25 and imc <= 30:
    print('Sobrepeso')
elif imc > 30 and imc <= 40:
    print('Obesidade')
elif imc > 40:
    print('Obesidade mórbida')