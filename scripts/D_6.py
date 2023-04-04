#você pode auterar o dado que deseja jogar, basta alterar a variação do numero dentro de "randint()"

from random import randint
from time import sleep
dado = randint(1,  6)
print('Jogando dado D6....')
sleep(5)
print(f'O dado caiu:{dado}')
print('Parabens! ^^,')