#Bibliotecas importadas
from random import randint
from time import sleep

    
sair = input("Você realmente quer jogar? S/N ")
if sair.lower() == 'n':
    exit()

#instruções
print(' == Escolha 4 para D4 ==\n'
      ' == Escolha 6 para D6 ==\n'
      ' == Escolha 8 para D8 ==\n'
      '== Escolha 10 para D10 ==\n'
      '== Escolha 12 para D12 ==\n'
      '== Escolha 20 para D20 == ')
sleep(1)

e = 'ESCOLHA SEU DADO! ===>:'

sleep(1)
numeros_validos = [4,6,8,10,12,20];

#Condições
num1 = int(input(e))
if num1 in numeros_validos :
    print(f'O dado escolhido foi D{num1}, Jogando dado......')
    sleep(3)
    print(f' O valor do dado é:{randint(1,num1)}')
else:
    print(f'O número {num1} não é um dado válido')

#bucefalo












