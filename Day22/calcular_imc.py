def calcular_imc():
    print("Bem vindos a calculadora de IMC")
    
    try:
        peso = float(input("Digite o seu peso em quilogramas: "))
        
        altura = float(input("Digite a sua altura em metros: "))
        
        if peso < 0 or altura < 0:
            print("O peso e altura deve ser maior que 0")
            return #encerrar a funcao
        
        imc = round(peso / (altura ** 2), 2)
        
        if imc < 18.5:
            print("Voce esta abaixo do peso ideal")
        elif 18.5 <= imc < 24.9:
            print("Voce esta no peso normal")
        elif 25 <= imc < 29.9:
            print("Voce esta com sobrepeso")
        else:
            print("Voce esta com obesidade")
            
    except ValueError:
        print("Entrada Inválida")
        
if __name__ == "__main__":
    calcular_imc()