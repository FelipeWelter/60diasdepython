def celsius_para_fahrenheit(celsius):
    """
    Converte a temperatura de Celsius para Fahrenheit.
    :param celsius: Temperatura em graus Celsius
    :return: Temperatura em graus Fahrenheit
    """
    return round((celsius * 9/5) + 32, 2)

def fahrenheit_para_celsius(fahrenheit):
    """
    Converte a temperatura de Fahrenheit para Celsius.
    :param fahrenheit: Temperatura em graus Fahrenheit
    :return: Temperatura em graus Celsius
    """
    return round((fahrenheit - 32) * 5/9, 2)

def main(temperatura, tipo_conversao):
    """
    Função principal para converter temperaturas.
    :param temperatura: Temperatura a ser convertida
    :param tipo_conversao: 'C' para Celsius para Fahrenheit, 'F' para Fahrenheit para Celsius
    :return: Temperatura convertida
    """
    if tipo_conversao == "celsius":
        print(celsius_para_fahrenheit(temperatura))
    elif tipo_conversao == "fahrenheit":
        print(fahrenheit_para_celsius(temperatura))
    else:
        return "Tipo de conversão inválido. Use 'celsius' ou 'fahrenheit'."
    
if __name__ == "__main__":
    main(20, "celsius")  # Exemplo de uso: converte 25 graus Celsius para Fahrenheit
    main(20, "fahrenheit")  # Exemplo de uso: converte 77 graus Fahrenheit para Celsius