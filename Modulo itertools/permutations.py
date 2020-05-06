import itertools


lista_combinacao = ['BL', 'VF', 'CEL', 'TV']

for combinacao in itertools.permutations(lista_combinacao, 3):
    print('_'.join(combinacao))