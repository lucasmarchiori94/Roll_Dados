
                                         # JOGO DE DADOS #

#Bibliotecas importadas
from random import randint
from time import sleep

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

#Dados
d6 = randint(1, 6)
d8 = randint(1, 8)
d10 = randint(1, 10)
d12 = randint(1, 12)
d20 = randint(1, 20)

e:str = 'ESCOLHA SEU DADO! -=>:'
print('-=' * 30)
sleep(1)

#Condições
num1 = int(input(e))
print('-=' * 30)
if num1==6:
    print('O dado escolhido foi D6, Jogando dado......')
    sleep(3)
    print(f'          O valor do dado é:{d6}')
if num1==8:
    print('O dado escolhido foi D8, Jogando dado......')
    sleep(3)
    print(f'          O Valor do dado é:{d8}')
if num1==10:
    print('O dado escolhido foi D10, Jogando dado......')
    sleep(3)
    print(f'          O Valor do dado é:{d8}')
if num1==12:
    print('O dado escolhido foi D12, Jogando dado......')
    sleep(3)
    print(f'          O Valor do dado é:{d12}')
if num1==20:
    print('O dado escolhido foi D20, jogando dado......')
    sleep(3)
    print(f'          O Valor do dado é:{d20}')

print('-=-=-=-=-=-=-=-=-=-=-FIM DE JOGO ^^,-=-=-=-=-=-=-=-=-=-=-=-=')















