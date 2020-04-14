
def edita_lista(lista, opcao_usuario):
    if opcao_usuario:
        if opcao_usuario in lista:
            lista.remove(opcao_usuario)
            return opcao_usuario + ' removido da lista'
        else:
            lista.append(opcao_usuario)
            return opcao_usuario + ' adicionado na lista'
        
    else:
        nome = lista.pop()
        return nome + ' removido do final da lista' 