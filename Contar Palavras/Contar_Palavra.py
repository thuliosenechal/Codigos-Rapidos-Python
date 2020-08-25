
dir_path = 'C:\\Users\\Etica\\Documents\\VisualStudioCode\\'
file_name = 'arquivo.txt'

contagem_palavras = {}
contagem_total = 0

with open(dir_path + file_name, 'r') as arq:
    texto = arq.read()

# Tratar caracteres
texto = texto.replace(',', '')
texto = texto.replace('.', '').lower()

texto_fragmentado = texto.split()
contagem_total = len(texto_fragmentado)

for palavra in texto_fragmentado:
    if palavra in contagem_palavras.keys():
        contagem_palavras[palavra] += 1
    else:
        contagem_palavras[palavra] = 1

print(f'\nTotal de palavras: {contagem_total}\n')

for k, v in contagem_palavras.items():
    print(f'{v}x {k}')