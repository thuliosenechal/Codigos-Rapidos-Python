import itertools


lista_combinacao = ['BL', 'VF', 'CEL', 'TV']

for combinacao in itertools.combinations(lista_combinacao, 3):
    print('_'.join(combinacao))


