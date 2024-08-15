dia = float(input('Quantos dias foi usado: '))
km = float(input('Quantos Km (Quilômetros) foram rodados: '))
preco = (60*dia) + (0.15*km)
print('Com {:.0f}Km rodados e {:.0f} dias de uso, o preço será de: {:.2f}R$ '.format(km,dia,preco))