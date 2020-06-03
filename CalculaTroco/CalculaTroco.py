from math import floor


notas = [100, 50, 20, 10, 5, 2, 1]
valorcompra = float(input('Entre com o valor da compra: '))
valorrecebido = int(input('Entre com o valor recebido pelo cliente: '))
valortroco = valorrecebido - valorcompra

while valortroco > 0:
    for nota in notas:
        n = valortroco / nota
        valortroco = valortroco % nota
        if int(n) != 0:
            if floor(n) == 1:
                print(f'{floor(n)} nota de R${nota:.2f}')
            else:
                print(f'{floor(n)} notas de R${nota:.2f}')






    
    