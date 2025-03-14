def conversor_moeda(valor, taxa_cambio, tipo_conversao):
    """
    Args:
    valor: (float):
    taxa_cambio: 
    tipo_conversao: dolar para real, real para dolar
    """
    
    if tipo_conversao == 'dolar_real':
        return round(valor * taxa_cambio, 2)
    elif tipo_conversao == 'real_dolar':
        return round(valor / taxa_cambio, 2)
    else:
        return ValueError("Tipo de conversao invalida")
print(conversor_moeda(12, 6.10, 'real_dolar'))