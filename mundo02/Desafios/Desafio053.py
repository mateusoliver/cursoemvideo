import time
frase = str(input('Digite uma frase: ')).strip().upper()
separa = frase.split()
junto = ''.join(separa)
inver = frase[::-1]
print('-'*25)
print('Checking your phrase... ')
print('-'*25)
time.sleep(3)
if junto.upper() == junto.upper():
    print('Sua frase é SIM um palíndromo!!')
    print(inver.upper())
    print(frase)
else:
    print('Sua frase NÃO é um palíndromo!!')