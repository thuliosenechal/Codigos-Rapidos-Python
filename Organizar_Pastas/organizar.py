import os


diretorio = 'c:\\Users\\<usuario>\\Downloads'
nome_arquivo_diretorio = os.listdir(diretorio)
pastas = [
           ['PDFs', '.pdf'],
           ['Executáveis', '.exe'],
           ['Docs', '.docx', '.doc', '.txt'],
           ['Imagens', '.jpg', '.jpeg', '.png', '.bmp', '.gif'],
           ['Videos', '.mp4', '.wmv', '.wma'],
           ['Musicas', '.mp3'],
           ['Planilhas', '.xls', '.xlsx'],
           ['ZIPs', '.zip', '.rar', '.7z']
         ]


def pega_extensao_arquivo(nome_arq):
    ext = os.path.splitext(nome_arq)
    return ext[1]

def cria_pasta(nome_pasta):
    if not os.path.exists(os.path.join(diretorio, nome_pasta)):
        os.mkdir(os.path.join(diretorio, nome_pasta))

def move_arquivo(arquivo, pasta):
    origem = os.path.join(diretorio, arquivo)
    destino = os.path.join(diretorio, pasta, arquivo)
    os.rename(origem, destino)


for arquivo in nome_arquivo_diretorio:
    if os.path.isfile(os.path.join(diretorio, arquivo)):
        extensao_arquivo = pega_extensao_arquivo(arquivo).lower()

        for pasta in pastas:
            if extensao_arquivo in pasta:
                nome_pasta = pasta[0]
                break
            else:
                nome_pasta = 'Outros'

        cria_pasta(nome_pasta)
        move_arquivo(arquivo, nome_pasta)
