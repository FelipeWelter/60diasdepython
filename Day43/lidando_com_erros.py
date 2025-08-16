def dividir(numerador, denominador):
    try:
        resultado = numerador / denominador
        print(F"Resultado da divisão: {resultado}")
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")
    except TypeError:
        print("Erro: Certifique-se de que ambos os valores são números.")
    print("Operação concluída.")

if __name__ == "__main__":
    dividir(10, 5) #Exemplo de uso com sucesso