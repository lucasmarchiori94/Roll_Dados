1    #Bibliotecas importadas
from random import randint
from time import sleep

sair = input("Você realmente quer jogar? S/N ")
if sair.lower() == 'n':
    exit()

#instruções
print(' == Escolha 6 para D6 ==')
sleep(1)
print(' == Escolha 8 para D8 ==')
sleep(1)
print('== Escolha 10 para D10 ==')
sleep(1)
print('== Escolha 12 para D12 ==')
sleep(1)
print('== Escolha 20 para D20 ==')
sleep(1)

e:str = 'ESCOLHA SEU DADO! ===>:'
sleep(1)

numerosValidos = [6,8,10,12,20];

def pega_valor_rolagem(lados):
    return randint(1, lados)

def pega_mensagem_customizada(lados, rolagem):
    sleep(1)
    if rolagem > 1:
        if rolagem == lados:
            print(f"Nossa! Tirou {lados} incrível!")
        elif rolagem > (lados / 2):
            print("Essa foi mais pra mais!")
        else:
            print("Essa foi mais pra menos!")
    else:
        print("Tirou 1! Que pena!")
#Condições
num1 = int(input(e))
if num1 in numerosValidos:
    print(f'O dado escolhido foi D{num1}, Jogando dado......')
    sleep(3)
    rolagem = pega_valor_rolagem(num1)
    print(f'O valor do dado é:{rolagem}')
    pega_mensagem_customizada(num1, rolagem)
        
else:
    print(f'O número {num1} não é um dado válido')

