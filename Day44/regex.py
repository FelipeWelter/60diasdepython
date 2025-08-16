import re

def validar_email(email):
    
    """
    funcao recebe email e valida se o email é válido
    """


    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(regex, email):
        print(f"{email} é um email válido.")
    else:
        print(f"{email} não é um email válido.")


# ^ - Início da string
# [a-zA-Z0-9._%+-]+ - Um ou mais caracteres alfanuméricos, pontos, sublinhados, porcentagens, sinais de mais ou menos
# @ - O símbolo arroba
# $ - Fim da string


validar_email("feliwelter@gmail.com")
validar_email("teste.com")