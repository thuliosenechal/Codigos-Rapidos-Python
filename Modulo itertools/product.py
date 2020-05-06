import itertools

lista_combinacao = ['1', '2']

nova_lista = ['.'.join(lista) for lista in itertools.product(lista_combinacao, repeat =3)]

print(nova_lista)