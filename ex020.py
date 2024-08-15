import random

num = [1, 2, 3, 4]

nome1 = input('Insira nome 1: ')
num1 = random.choice(num)
num.remove(num1)
print('O aluno {} ficou com a apresentação {}'.format(nome1, num1))

nome2 = input('Insira nome 2: ')
num2 = random.choice(num)
num.remove(num2)
print('O aluno {} ficou com a apresentação {}'.format(nome2, num2))

nome3 = input('Insira nome 3: ')
num3 = random.choice(num)
num.remove(num3)
print('O aluno {} ficou com a apresentação {}'.format(nome3, num3))

nome4 = input('Insira nome 4: ')
num4 = random.choice(num)
print('O aluno {} ficou com a apresentação {}'.format(nome4, num4))