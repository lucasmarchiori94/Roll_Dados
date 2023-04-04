from random import randint
import subprocess
from PySimpleGUI import PySimpleGUI as sg

#layout
sg.theme('DarkAmber')
layout = [
    [sg.Button('D20', size=(3, 2)),sg.Button('D12', size=(3, 2)),sg.Button('D10', size=(3, 2)),
     sg.Button('D08', size=(3, 2)),sg.Button('D06', size=(3, 2)),sg.Button('D04', size=(3, 2))],
    [sg.Output(size=(90, 50,))] # elemento Output
]
#Janela
janela = sg.Window('Roll Dice',layout, size=(1000, 500))
#Eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'D20':
        resultado = randint(1, 20)
        print(resultado)
        if resultado > 10:
            print('Caramba parabens')
        if resultado == 10:
            print('Ná trave')
        if resultado < 10:
            print('uma pena')
    
    if eventos == 'D12':
        resultado = randint(1, 12)
        print(resultado)
        if resultado > 6:
            print('Caramba parabens')
        if resultado == 6:
            print('Ná trave')
        if resultado < 6:
            print('uma pena')        
            
    if eventos == 'D10':
        resultado = randint(1, 10)
        print(resultado)
        if resultado > 5:
            print('Caramba parabens')
        if resultado == 5:
            print('Ná trave')
        if resultado < 5:
            print('uma pena')

    if eventos == 'D08':
        resultado = randint(1, 8)
        print(resultado)
        if resultado > 4:
            print('Caramba parabens')
        if resultado == 4:
            print('Ná trave')
        if resultado < 4:
            print('uma pena')

    if eventos == 'D06':
        resultado = randint(1, 6)
        print(resultado)
        if resultado > 3:
            print('Caramba parabens')
        if resultado == 3:
            print('Ná trave')
        if resultado < 3:
            print('uma pena')

    if eventos == 'D04':
        resultado = randint(1, 4)
        print(resultado)
        if resultado > 2:
            print('Caramba parabens')
        if resultado == 2:
            print('Ná trave')
        if resultado < 2:
            print('uma pena')

janela.close()                                        