def calcular_media_notas(notas):
    """
    Calcula media a partir de uma lista
    
    Arg:
    notas (lista)
    
    return:
    float da media das notas
    """
    
    media = sum(notas) / len(notas)
    #arredonda as medias para duas casas decimais
    return round(media, 2)

print(calcular_media_notas([10,8,5,6,3]))