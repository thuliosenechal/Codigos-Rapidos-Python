import random


def validar_sorteio(embaralhado, participantes):
    for i, _ in enumerate(participantes):
        if embaralhado[i] == participantes[i]:
            return False
    return True

dir_path = 'C:\\Users\\Etica\\Documents\\VisualStudioCode\\Amigo Secreto\\'
qtd_participantes = int(input("Insira a quantidade de participantes: "))
participantes = []
embaralhado = []

for i in range(qtd_participantes):
    nome = input(f'Entre com o nome do {i+1}º participante: ').title()
    participantes.append(nome)

embaralhado = random.sample(participantes, qtd_participantes)

while not validar_sorteio(embaralhado, participantes):
    embaralhado = random.sample(participantes, qtd_participantes)

for i in range(qtd_participantes):
    with open(f'{dir_path}{participantes[i]}.txt', 'w') as arquivo:
        arquivo.write(embaralhado[i])

