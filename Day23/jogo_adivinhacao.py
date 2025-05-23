import random

def jogar_adivinhacao():
    """
    um jogo onde o usuario tenta adivinhar um numero aleatorio
    """
    
    print("Bem vindo ao jogo da adivinhação")
    
    #gerar um numero secreto de 0 a 10
    numero_secreto = random.randint(0,10)
    
    tentativas = 0
    
    while True:
        try:
            palpite = int(input("Digite seu palpite: "))
            tentativas += 1
            
            if palpite < numero_secreto:
                print("Muito abaixo do numero secreto")
            elif palpite > numero_secreto:
                print("Muito alto em relação ao numero secreto")
            else:
                print(f"Parabens vc acertou: o numero era {numero_secreto}, suas tentativas {tentativas}")
                break
        
        except ValueError:
            print("Digite um numero valido")
            
if __name__ == "__main__":
    jogar_adivinhacao()