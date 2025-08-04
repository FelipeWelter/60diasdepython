from datetime import datetime
import pytz

def exibir_data_atual():
    # Obtém a data e hora atual
    fuso_horaria = pytz.timezone("America/Sao_Paulo")

    data_hora = datetime.now(fuso_horaria)
    formato_data = data_hora.strftime("%d/%m/%Y %H:%M:%S")
    print(f"Data e hora atual: {formato_data}")

if __name__ == "__main__":
    exibir_data_atual()  # Exibe a data e hora atual no formato especificado