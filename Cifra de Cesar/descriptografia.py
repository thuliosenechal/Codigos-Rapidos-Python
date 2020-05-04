'''Descriptografar mensagem.
   Regras: - Apenas letras minúsculas
           - Desconsiderar espaços, virgulas e pontos
'''

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

tamanho_lista_alfabeto = len(alfabeto)            
cifrado = "ftq axpqd u sqf, ftq yadq u nqxuqhq ftmf ftq azxk imk fa nqoayq m nqffqd bdasdmyyqd ue nk zaf bdasdmyyuzs. vqrr mfiaap"
chave_cripto = 12
decifrado = ''

def descriptografia(mensagem):
    global decifrado

    for letra in mensagem:
        if letra.isalpha():
            indice = alfabeto.index(letra)
            nova_letra = alfabeto[(indice - chave_cripto)%tamanho_lista_alfabeto]
        else:
            nova_letra = letra

        decifrado = decifrado + nova_letra
    
    return decifrado

if __name__ == '__main__':
    print(cifrado)
    print(descriptografia(cifrado))
#sha1: 8730745d6517c91b4a4627be58c2142fc81b4224