from random import randint
from time import sleep
d20 = randint(1, 20)
print('Jogando dado D20....')
sleep(5)
print(f'O dado caiu:{d20}')
if d20>10:
    print('Parabens! ^^, Bela jogada')
else:
    print('Caramba por pouco em. Tente novamente !')



