larg = float(input('Insira largura da parede:'))
alt = float(input('Insira altura da parede:'))
area = float(alt * larg)
tinta = area / 2
print('A área será: {}\nQuantidade de baldes necessários: {:.0f}'.format(area,tinta))