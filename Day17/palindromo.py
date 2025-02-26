def palindromo(texto):
    """
    Verifica se numero, texto, ou palavra e um palindromo
    """
    texto = str(texto).replace(" ", "").lower()
    
    if texto == texto[::-1]:
        return f"{texto} e um palindromo"
    return f"{texto} nao e um palindromo"

print(palindromo("felipe"))