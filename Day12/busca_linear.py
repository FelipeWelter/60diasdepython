def busca_linear(lista, numero_procurado):
    """
    Procurar um número dentro de uma lista utilizando busca linear
    :param lista: lista de numeros
    :param numero_procurado: o numero que procura
    """
    for i, numero in enumerate(lista): #funcao nativa do python enumerate, passa por itens dentro da lista
        if numero == numero_procurado:
            return i
    return -1

lista = ["teste", "curso", "felipe", "gta 6", 1000,5,6,7,87,98,90]
numero_procurado = 1000

buscando_o_numero = busca_linear(lista, numero_procurado)

if buscando_o_numero != -1:
    print(f"O numero está no indice: {buscando_o_numero}")
else:
    print("numero nao encontrado")