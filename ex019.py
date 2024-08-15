import random
nome1 = input('Insira nome 1: ')
nome2 = input('Insira nome 2: ')
nome3 = input('Insira nome 3: ')
nome4 = input('Insira nome 4: ')
nomes = [nome1, nome2, nome3, nome4]
nome_sorteado = random.choice(nomes)
print("O nome sorteado foi:", nome_sorteado)
