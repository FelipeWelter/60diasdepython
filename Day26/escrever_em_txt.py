def escrever_arquivo(nome_arquivo, conteudo):
    """
    Escrever conteudo em um arquivo txt
    Arg:
    nome_arquivo(str): nome do arquivo a ser criado
    conteudo (str): texto que vai ser escrito
    """

    with open(nome_arquivo, 'w') as arquivo: #w = write
        arquivo.write(conteudo)
    
    print(f"O conteudo foi salvo no arquivo: {nome_arquivo}.")

def ler_arquivo(nome_arquivo):
    """
    ler o conteudo do arquivo .txt
    Arg:
    nome_arquivo(str) o nome do arquivo a ser lido
    """
    try:
        with open(nome_arquivo, 'r') as arquivo: # r = read de ler
            conteudo = arquivo.read()
        print(f"Conteudo do arquivo: {conteudo}")
    except FileNotFoundError:
        print("O arquivo nao foi encontrado tente novamente")
def main(nome_arquivo, conteudo):
    """
    Funcao principal que demonstra escrita e leitura do arquivo
    
    Arg:
    nome_arquivo (str): nome do arquivo a ser criado e lido
    conteudo (str): o texto a ser salvo no arquivo
    """

    print("Bem vindos ao nosso programa de escrita e leitura")
    #escrevendo no arquivo
    escrever_arquivo(nome_arquivo, conteudo)
    
    #leitura do arquivo
    print("Fazendo a leitura do arquivo...")
    ler_arquivo(nome_arquivo)

if __name__ == "__main__":
    arquivo = "exemplo.txt"
    texto = "FWGAME"

    main(arquivo, texto)