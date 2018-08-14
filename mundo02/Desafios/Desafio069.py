r = 'S'
maior = 0
homens = 0
mulheres = 0
while r == 'S':
    idade = int(input('Entre com sua idade: '))
    sexo = str(input('Qual seu sexo [M/F]: ')).upper()
    if idade > 18:
        maior = maior + 1
    if sexo == 'M':
        homens = homens + 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    r = str(input('Quer continuar [S/N]')).upper()
print(f'{idade} {sexo} {r}')
print(f'{maior} pessoa(s) tem maior que 18 anos')
print(f'{homens} homens foram cadastrados!')
print(f'{mulheres} mulheres tem menos de 20 anos')
