entrada = input("Coloque o numero: ")

try: #tente rodar
    numero = int(entrada)
    if numero % 2 == 0:
        print("numero par")
    else:
        print("numero impar")
except ValueError:
    print("Voce nao passou um numero inteiro")