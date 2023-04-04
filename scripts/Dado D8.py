from random import randint
from time import sleep
d8 = randint(1, 8)
print('Jogando dado D8....')
sleep(5)
print(f'O dado caiu:{d8}')
if d8>4:
    print('Parabens! ^^, Bela jogada')
else:
    print('Caramba por pouco em. Tente novamente !')