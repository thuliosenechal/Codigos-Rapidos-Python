'''Descriptografar mensagem.
   Regras: - Apenas letras minúsculas
           - Desconsiderar espaços, virgulas e pontos
'''

import string


alfabeto = string.ascii_lowercase
tamanho_lista_alfabeto = len(alfabeto)            
cifrado = 'the older i get, the more i believe that the only way to become a better programmer is by not programming. jeff atwood'
chave_cripto = 12
decifrado = ''

def criptografia(mensagem):
    global decifrado

    for letra in mensagem:
        if letra.isalpha():
            indice = alfabeto.index(letra)
            nova_letra = alfabeto[(indice + chave_cripto)%tamanho_lista_alfabeto]
        else:
            nova_letra = letra

        decifrado = decifrado + nova_letra

    return decifrado


if __name__ == '__main__':
    print(cifrado)
    print(criptografia(cifrado))
#sha1: 8730745d6517c91b4a4627be58c2142fc81b4224