from random import randint
from time import sleep
d10 = randint(1, 10)
print('Jogando dado D10....')
sleep(5)
print(f'O dado caiu:{d10}')
if d10>5:
    print('Parabens! ^^, Bela jogada')
else:
    print('Caramba por pouco em. Tente novamente !')