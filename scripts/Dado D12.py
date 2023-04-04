from random import randint
from time import sleep
d12 = randint(1, 12)
print('Jogando dado D12....')
sleep(5)
print(f'O dado caiu:{d12}')
if d12>6:
    print('Parabens! ^^, Bela jogada')
else:
    print('Caramba por pouco em. Tente novamente !')