from random import randint
from time import sleep
d4 = randint(1, 4)
print('Jogando dado D4....')
sleep(5)
print(f'O dado caiu:{d4}')
if d4>2:
    print('Parabens! ^^, Bela jogada')
else:
    print('Caramba por pouco em. Tente novamente !')