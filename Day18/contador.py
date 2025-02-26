def contar_palavras(texto):
    """contar palavras em uma string
    :param texto: string de entrada
    :return: numero de palavras
    """
    
    palavras = texto.split()
    return len(palavras)
print(contar_palavras("ola mundo, estou aprendendo python"))