import pandas as pd
# Ler um arquivo CSV e exibir as primeiras linhas

def main():
    nome_arquivo = "test.csv"

    df = pd.read_csv(nome_arquivo)

    print(df)

if __name__ == "__main__":
    main()
