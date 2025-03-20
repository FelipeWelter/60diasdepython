def tabuada():
    """
    Essa função recebe um número e retorna a tabuada
    """
    
    try:
        #solicitar o numero para o usuario
        
        numero = int(input("Digite o numero para gerar a tabela: "))\
            
        print(f"\nTabuada de {numero}:")
        #Gera a tabuada de 1 a 10
        for i in range(1, 11):
            resultado = numero * i
            print(f"{numero} x {i} = {resultado}")
                
    except ValueError:
        print("Entrada invalida. Digite um numero")
        
if __name__ == "__main__":
    tabuada()