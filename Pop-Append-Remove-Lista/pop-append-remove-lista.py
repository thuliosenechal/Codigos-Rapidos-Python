import funcao_lista
import time


lista = ['joão', 'antonio', 'maria', 'ana']

while lista:
    print(f'Lista: {lista}'.title())
    print('''
             - Pressione Enter para remover o ultimo nome da lista
             - Insira um novo nome para adicionar na lista
             - Informe um nome para remover da lista
             - Pressione 'q' para sair do programa
          ''')
    opcao_usuario = input('/>: ').title()          
    
    if opcao_usuario.lower() != 'q':
        msg = funcao_lista.edita_lista(lista, opcao_usuario)
        print(msg)
        time.sleep(2)
    else:
        break
