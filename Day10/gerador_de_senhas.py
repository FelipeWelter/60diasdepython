import random
import string

#random - fornece numeros aleatorios
#string - letras, simbolos e numeros

def gerador_de_senhas(tamanho):
    comprimento = tamanho
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''
    
    while len(senha) < comprimento:
        senha += random.choice(caracteres)
        
    print(f"Sua Senha é: {senha}")
    
gerador_de_senhas(8)