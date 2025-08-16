import os

diretorio = "./" # Defina o diretório desejado
arquivos_pasta = os.listdir(diretorio)

for arquivo in arquivos_pasta:
    caminho_completo = os.path.join(diretorio, arquivo)  # Exemplo de como usar join para criar um caminho completo
    if os.path.isdir(caminho_completo):
        print(f"Pasta que conmtem arquivo: {arquivo}")
        print(os.listdir(arquivo))  # Lista os arquivos dentro do diretório
    elif os.path.isfile(caminho_completo):
        print(arquivo)
