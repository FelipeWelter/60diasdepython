def fatorial(n):
        """
        Calcula o fatorial de um numero usando recursão
        :param n: Número inteiro nao negativo.
        :return: Fatorial de n.
        """
        if n < 0:
            raise ValueError("O numero deve ser positivo")
        #retorna 1 caso o numero serja 0 ou 1
        if n == 0 or n == 1:
            return 1
        #recursividade
        return n * fatorial(n -1)

try:
    print(f"Fatorial igual a {fatorial(10)}")
except ValueError as e:
    print(e)