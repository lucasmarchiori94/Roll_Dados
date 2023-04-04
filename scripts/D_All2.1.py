from random import randint
from time import sleep
#from file import function

print('Bem vindo ao Roll_Dados.\n ')
sleep(3)
print('Vamos Jogar!!!')
sleep(3)
print(' == Escolha 4 para D4 ==\n'
      ' == Escolha 6 para D6 ==\n'
      ' == Escolha 8 para D8 ==\n'
      '== Escolha 10 para D10 ==\n'
      '== Escolha 12 para D12 ==\n'
      '== Escolha 20 para D20 == ')
sleep(3)

ecolha_dado = 'ESCOLHA SEU DADO! ===>:'
numeros_validos = [4, 6, 8, 10, 12, 20]
sleep(3)

numero_escolhido = int(input(ecolha_dado))
if numero_escolhido in numeros_validos:
      print(f'O dado escolhido foi: {numero_escolhido}, Jogando Dado.........')
      sleep(3)
      print(f' O valor do dado é:{randint(1, numero_escolhido)}')

else:
    print(f'O número {numero_escolhido} não é um dado válido')




