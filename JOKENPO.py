from random import randint
from time import sleep
import color
def linha():
    print('-=-' * 14 )



linha()
print('\033[1;36m JOKENPO \033[m')
linha()
itens = (' pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print(''' Suas Opções
 [0] Pedra
 [1] Papel
 [2] Tesoura''')
 
jogador = int(input(' Qual é a sua Jogada: '))

linha()
print('\033[35m JO')
sleep(1)
print(' KEN')
sleep(1)
print(' PO!!!\033[m')

linha()
print(' O Computador Jogou {} '.format(itens[computador]))
print(' O Jogador Jogou {}'.format(itens[jogador]))
linha()

if  computador == 0:
    if jogador == 0:
        print('\033[1;30m Empatou!')
    elif jogador == 1:
        print('\033[1;32m Ganhou!')
    elif jogador ==2:
        print('\033[1;31m Derota')
    else:
        print(' JOGADA INVALIDA')

elif computador == 1:
    if jogador == 0:
        print('\033[1;32m Ganhou')
    elif jogador == 1:
        print('\033[1;30m Empate!')
    elif jogador == 2:
        print('\033[1;31m Derota')
    else:
        print(' JOGADA INVALIDA')
        
elif computador == 2:
    if jogador == 0:
        print('\033[1;32m Ganhou')
    elif jogador == 1:
        print('\033[1;31m Derota')
    elif jogador == 2:
        print('\033[1;30m Empate')
    else:
        print(' JOGADA INVALIDA')