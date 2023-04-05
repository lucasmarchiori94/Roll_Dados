#Bibliotecas importadas
from random import randint
import random
import subprocess
from PySimpleGUI import PySimpleGUI as sg

#lista de frases com conseguência de acordo com numero tirado no dado
frases_ataque_critico = [
    'CRITOU !', 'DANO CRITICO'
]
frases_ataque_perfeito = [
    'Caramba belo golpe!', 'Você arrancou a cabeça dele', 'O inimigo treme de medo ao ver você sacar sua espada; VOCÊ GOLPEA ELE FIRME E ACERTOU EM CHEIO NA CABEÇA',
    'fantastico você quebrou os ossos do pescoço dele'
]
frases_ataque_bom = [
    'você quase arrancou a cabeça dele', 'você fez um corte profundo mas o unimigo ainda pode te atacar', 'poderia golpear mais forte', 'isso é tudo que tem?',
]
frases_ataque_mediano = [
    'Você causa cortes em seu inimigo'

]
frase_ataque_baixo = [
    'Golpe fraco em, mas conseguiu causar ferimentos leves no inimigo'

]
frases_ruins = [
    'você bate sua espada de raspão no braço dele', 'você acerta o inimigo e escorrega durante o golpe e sua espasa cai proximo de você',
]

#layout
sg.theme('DarkAmber')
layout = [
    [sg.Button('D20', size=(3, 2)),sg.Button('D12', size=(3, 2)),sg.Button('D10', size=(3, 2)),
     sg.Button('D08', size=(3, 2)),sg.Button('D06', size=(3, 2)),sg.Button('D04', size=(3, 2))],
    [sg.Output(size=(90, 50))] # elemento Output
]
#Janela
janela = sg.Window('Roll Dice',layout, size=(400, 300))
#Eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'D20':
        resultado = randint(1, 20)
        print(resultado)
        if resultado == 20:
            frase_critico = random.choice(frases_ataque_critico)
            print(frase_critico)
        if resultado in [17, 18, 19]:
            frase_perfeita = random.choice(frases_ataque_perfeito)
            print(frase_perfeita)
        if resultado in [12, 13, 14, 15, 16]:
            frase_boa = random.choice(frases_ataque_bom)
            print(frase_boa)
        if resultado in [7, 8, 9, 10,11]:
            frase_media = random.choice(frases_ataque_mediano)
            print(frase_media)
        if resultado in [2, 3, 4, 5, 6]:
            frase_baixa = random.choice(frase_ataque_baixo)
            print(frase_baixa)
        if resultado == 1:
            frase_ruin = random.choice(frases_ruins)
            print(frase_ruin)



    if eventos == 'D12':
        resultado = randint(1, 12)
        print(resultado)
        if resultado == 12:
            frase_critico = random.choice(frases_ataque_critico)
            print(frase_critico)
        if resultado in [10, 11]:
            frase_perfeita = random.choice(frases_ataque_perfeito)
            print(frase_perfeita)
        if resultado in [7, 8, 9]:
            frase_boa = random.choice(frases_ataque_bom)
            print(frase_boa)
        if resultado in [5, 6]:
            frase_media = random.choice(frases_ataque_mediano)
            print(frase_media)
        if resultado in [2, 3, 4]:
            frase_baixa = random.choice(frase_ataque_baixo)
            print(frase_baixa)
        if resultado == 1:
            frase_ruin = random.choice(frases_ruins)
            print(frase_ruin)        
            


    if eventos == 'D10':
        resultado = randint(1, 10)
        print(resultado)
        if resultado == 10:
            frase_critico = random.choice(frases_ataque_critico)
            print(frase_critico)
        if resultado in [8, 9]:
            frase_perfeita = random.choice(frases_ataque_perfeito)
            print(frase_perfeita)
        if resultado in [6, 7]:
            frase_boa = random.choice(frases_ataque_bom)
            print(frase_boa)
        if resultado in [4, 5]:
            frase_media = random.choice(frases_ataque_mediano)
            print(frase_media)
        if resultado in [2, 3]:
            frase_baixa = random.choice(frase_ataque_baixo)
            print(frase_baixa)
        if resultado == 1:
            frase_ruin = random.choice(frases_ruins)
            print(frase_ruin)



    if eventos == 'D08':
        resultado = randint(1, 8)
        print(resultado)
        if resultado == 8:
            frase_critico = random.choice(frases_ataque_critico)
            print(frase_critico)
        if resultado in [7]:
            frase_perfeita = random.choice(frases_ataque_perfeito)
            print(frase_perfeita)
        if resultado in [5, 6]:
            frase_boa = random.choice(frases_ataque_bom)
            print(frase_boa)
        if resultado in [3, 4]:
            frase_media = random.choice(frases_ataque_mediano)
            print(frase_media)
        if resultado in [2]:
            frase_baixa = random.choice(frase_ataque_baixo)
            print(frase_baixa)
        if resultado == 1:
            frase_ruin = random.choice(frases_ruins)
            print(frase_ruin)



    if eventos == 'D06':
        resultado = randint(1, 6)
        print(resultado)
        if resultado == 6:
            frase_critico = random.choice(frases_ataque_critico)
            print(frase_critico)
        if resultado == 5: 
            frase_perfeita = random.choice(frases_ataque_perfeito)
            print(frase_perfeita)
        if resultado == 4:
            frase_boa = random.choice(frases_ataque_bom)
            print(frase_boa)
        if resultado == 3:
            frase_media = random.choice(frases_ataque_mediano)
            print(frase_media)
        if resultado == 2:
            frase_baixa = random.choice(frase_ataque_baixo)
            print(frase_baixa)
        if resultado == 1:
            frase_ruin = random.choice(frases_ruins)
            print(frase_ruin)



    if eventos == 'D04':
        resultado = randint(1, 4)
        print(resultado)
        if resultado == 4:
            frase_critico = random.choice(frases_ataque_critico)
            print(frase_critico)
        if resultado == 3:
            frase_perfeita = random.choice(frases_ataque_perfeito)
            print(frase_perfeita)
        if resultado == 2:
            frase_baixa = random.choice(frase_ataque_baixo)
            print(frase_baixa)
        if resultado == 1:
            frase_ruin = random.choice(frases_ruins)
            print(frase_ruin)
janela.close()                                        