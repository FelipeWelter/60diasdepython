def transpor_matriz(matriz):
    """
    GERAR UMA MATRIZ TRANSPOSTA DE 3X3
    Substitui colunas horizontais por verticais
    
    [1 ,2 ,3] 
    [1 ,2 ,5]
    [1 ,2 ,3]
    
    ex:
    
    [1 ,1 ,1]
    [2 ,2 ,2]
    [3 ,5 ,3]
    
    Arg: Matriz que serao lista de 3 numeros na horizontal e na vertical
    return: Matriz transposta
    Raises: ValueError: se a matriz nao for 3x3
    """

    #verifica se a matriz e 3x3
    if len(matriz) != 3 or not all(len(linha) == 3 for linha in matriz):
        raise ValueError("A matriz nao possui o tamanho 3x3")
    
    transposta = [[matriz[j][i] for j in range(3)] for i in range(3)]
    
    return transposta
#explicacao da matriz utilizando iteradores e listas
    
matriz = [
    [1, 5, 8],
    [4, 6, 7],
    [9, 1, 3]
]
    
transposta = []

for i in range(3):
    nova_linha = []
    
    for j in range(3):
        nova_linha.append(matriz[j][i])
    
    
    
    
    print(nova_linha)
    transposta.append(nova_linha)