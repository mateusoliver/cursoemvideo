'''enquanto não maçã       while not maçã:
    se chao                 if chao
        passo
    se vazio
        pula
    se modda
        pega
pega'''

#c =1
#while c <=10:
#    print(c)
#    c += 1
#print('FIM')

##################################3
'''n = 1
while n != 0:
    n = int(input('Digite um valor'))
print('FIM')'''
##################################3

##################################3
'''r = 'S'
while r == 'S':
    n = int(input('Digite um valor'))
    r = str(input('Quer continuar? [S/N}')).upper()
print('FIM')'''
##################################

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 ==0:
            par += 1
        else:
            impar += 1
print('Você digitou {} numero pares e {} numeros impares'.format(par,impar))