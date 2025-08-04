import json
from typing import Any

def salvar_dados(arquivo: str, dados: Any)-> None:
    """
    Salva dados em um arquivo JSON.
    :param arquivo: Caminho do arquivo onde os dados serão salvos.
    :param dados: Dados a serem salvos no arquivo.

    """

    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

def carregar_dados(arquivo: str) -> Any:
    """
    Carrega dados de um arquivo JSON.
    :param arquivo: Caminho do arquivo de onde os dados serão carregados.
    :return: Dados carregados do arquivo.

    """
    
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Arquivo {arquivo} não encontrado.")
        return {}
    
dados_exemplo = {
    "nome": "Felipe",
    "idade": "24",
}
nome_arquivo = "felipe.json"

salvar_dados(nome_arquivo, dados_exemplo)
dados_carregados = carregar_dados(nome_arquivo)
print("Dados carregados:", dados_carregados)