
#lista = [2, 5, 6, 10, 20, 22, 26, 30, 40, 42, 54]
lista = range(257)
target = 256
left_list = 0
right_list = len(lista) - 1
midle_list = (left_list + right_list) // 2
found = False
count = 0

while left_list <= right_list:
    midle_list = int(midle_list)
    element_middle = lista[midle_list]

    if element_middle == target:
        found = True
        break
    elif target < element_middle:
        right_list = midle_list - 1
    elif target > element_middle:
        left_list = midle_list + 1
    
    midle_list = (left_list + right_list) // 2
    count += 1

if found:
    print(f'Número encontrado na posição {midle_list}')    
else:
    print('Número não encontrado na lista.')

print(f'Passei {count} vezes')    
    