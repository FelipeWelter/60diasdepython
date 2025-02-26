def anagrama(palavra1, palavra2):
    """
    Verifica se duas palavras sao um anagrama ou nao
    :param palavra1: Primeira palavra
    :param palavra2: segunda
    :return: true se as palavras forem um anagrama
    """
    
    
    palavra1 = palavra1.replace(" ", "").lower()
    palavra2 = palavra2.replace(" ", "").lower()
    
    if sorted(palavra1) == sorted(palavra2):
        return f"Essas palavrao sao anagramas"
    return f"Essas palavras nao sao anagramas"
    
print(anagrama("roma", "amor"))