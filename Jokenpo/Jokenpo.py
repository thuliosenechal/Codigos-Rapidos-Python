# Desafio 45

'''Crie um programa que faça o computador jogar Jokenpô com você.'''

import random
import time
import sys


opcoes = {0: 'PEDRA', 1: 'PAPEL', 2: 'TESOURA'}

def menu():
    print('''Escolha uma das opções abaixo:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
[ 3 ] QUIT GAME''')

    jogador = int(input('\nQual a sua jogada? '))

    return jogador


print('Vamos jogar...')

jogador = menu()

while True:
    if jogador == 3:
        print('Até logo...')
        break
    elif jogador == 0:
        jogador = opcoes[0]
    elif jogador == 1:
        jogador = opcoes[1]
    elif jogador == 2:
        jogador = opcoes[2]
    else:
        print('\nOpção inválida. Tente novamente. \n')
        time.sleep(1)
        jogador = menu()
    
    print(' ')
    print('JOKENPO! ')
    time.sleep(1.5)

    print(' ')

    computador = random.choice(opcoes)

    print(f'Computador escolheu {computador}.')
    print(f'Jogador escolheu {jogador}.')
    print('\nComputando resultado...\n')

    time.sleep(3)


    if jogador == 'PEDRA' and computador == 'TESOURA':
        print('JOGADOR VENCEU')
    elif jogador == 'TESOURA' and computador == 'PAPEL':
        print('JOGADOR VENCEU')
    elif jogador == 'PAPEL' and computador == 'PEDRA':
        print('JOGADOR VENCEU')
    elif computador == 'TESOURA' and jogador == 'PAPEL':
        print('COMPUTADOR VENCEU')
    elif computador == 'PAPEL' and jogador == 'PEDRA':
        print('COMPUTADOR VENCEU')
    elif computador == 'PEDRA' and jogador == 'TESOURA':
        print('COMPUTADOR VENCEU')
    else:
        print('EMPATE')

    print(' ')
    print("Aperte ENTER para jogar novamente ou 'Q' para sair do jogo.")
    opcao = input()

    if opcao.lower() == 'q':
        print('Até logo...')
        break
    else:
        print('Reiniciando o jogo...')
        jogador = menu()


