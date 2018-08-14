cont = n = s = 0
while True:
    n = int(input('Digite um valor ou 999 para sair: '))
    if n == 999:
        break
    s += n
    cont += 1
print(f'Você digitou {cont} numero e a soma deles é {s}')