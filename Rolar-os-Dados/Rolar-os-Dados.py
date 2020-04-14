import random
import time
import os


ultimo_dado = 0
rolar_dado = 1
sair_jogo = 2

while True:
    os.system('cls') 
    
    print('\n1 - Rolar dado \n2 - Sair\n')
    opcao_usuario = int(input())

    if opcao_usuario == rolar_dado:
        print('\nRolando o dado...')
        time.sleep(1)
        print()
        dado = random.randint(1, 6)
        
        while dado == ultimo_dado:
            dado = random.randint(1, 6)
        
        print(f'Dado sorteado - Nº {dado}')
        time.sleep(2)

        ultimo_dado = dado

    if opcao_usuario == sair_jogo:
        os.system('cls')
        break
