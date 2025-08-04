import time

def cronometro():
    """
    Função que cria um cronômetro, que conta até 10 segundos.
    """
    print("Iniciando cronômetro...")

    tempo = 10  # Tempo em segundos

    while tempo > 0:
        print(f"Tempo restante: {tempo} segundos", end="\r", flush=True)
        time.sleep(1)
        tempo -= 1

    print("\nCronômetro finalizado!")

if __name__ == "__main__":
    cronometro()  # Inicia o cronômetro com o tempo especificado