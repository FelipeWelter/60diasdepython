from collections import Counter

def contar_ocorrencias(lista):
    """Conta as ocorrências de cada elemento em uma lista."""
    contagem = Counter(lista)


    for elemento, quantidade in Counter(lista).items():
        print(f"{elemento}: {quantidade} vez(es)")

    return "Contagem concluída."

if __name__ == "__main__":
    lista_exemplo = ['maçã', 'banana', 'laranja', 'maçã', 'banana', 'maçã']
    # Exemplo de uso
    print(contar_ocorrencias(lista_exemplo))