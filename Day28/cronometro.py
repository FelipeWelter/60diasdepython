import time

def cronometro(tempo):
    """
    Função que cria um cronometro, que conta ate o tempo especificado pelo usuário.
    """
    print("Iniciando cronometro...")

    for segundo in range(tempo + 1):
        print(f"Tempo: {segundo} segundos", end="\r")
        time.sleep(1)

    print("\nCronometro finalizado!")

if __name__ == "__main__":
    tempo = 10  # Tempo em segundos
    cronometro(tempo) # Inicia o cronometro com o tempo especificado