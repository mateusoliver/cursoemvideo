alt = float(input('Qual a altura da parede: '))
lar = float(input('Qual a largura da parede: '))
area = alt * lar
print('A área da parede é {}m²'.format(area))
print('Então podemos pintar toda a parede com {:.2} Litros de tinta'.format(area/2))