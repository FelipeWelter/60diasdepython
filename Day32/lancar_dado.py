import random

def lancar_dado():
    """Lança um dado de seis lados e retorna o resultado."""
    return random.randint(1, 6)

if __name__ == "__main__":
    print(f"O resultado do lançamento do dado é: {lancar_dado()}")