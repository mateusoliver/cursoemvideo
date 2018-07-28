import math
cateto01 = float(input('Entre com o primeiro cateto, por favor: '))
cateto02 = float(input('Entre com o segundo cateto, por favor: '))
hipotenusa = math.pow(cateto01,2)+math.pow(cateto02,2)
#hipotenusa = hipotenusa**(1/2)
print('hipotenusa {}'.format(math.sqrt(hipotenusa)))
#print("hipotenusa {}".format(hipotenusa))