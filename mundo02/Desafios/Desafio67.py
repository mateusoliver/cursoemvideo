while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('='*40)
    if num < 0:
        print('O PROGRAMA FOI ENCERRADO! VOLTE SEMPRE!')
        break
    for c in range(1,11):
        print(f'{num} * {c} = {num*c}')
    print('='*40)