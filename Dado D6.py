from random import randint
from time import sleep
d6 = randint(1, 6)
print('Jogando dado D6....')
sleep(5)
print(f'O dado caiu:{d6}')
if d6>3:
    print('Parabens! ^^, Bela jogada')
else:
    print('Caramba por pouco em. Tente novamente !')