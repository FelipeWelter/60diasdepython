import matplotlib.pyplot as plt

# Dados de exemplo
categorias = ['A', 'B', 'C', 'D']
valores = [10, 20, 15, 25]

# Criando o gráfico de barras
plt.bar(categorias, valores)

# Adicionando título e rótulos
plt.title('Gráfico de Barras Exemplo')
plt.xlabel('Categorias')
plt.ylabel('Valores')

# Exibindo o gráfico
plt.show()
