import math

def raiz_quadrada(numero):
    """Calcula a raiz quadrada de um número."""
    if numero < 0:
        raise ValueError("Não é possível calcular a raiz quadrada de um número negativo.")
    return round(math.sqrt(numero), 2)

if __name__ == "__main__":
    print(raiz_quadrada(4))