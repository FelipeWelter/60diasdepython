def numeros_infinito():
    num = 0
    while True:
        yield num
        num += 1

gerador = numeros_infinito()

for _ in range(10000):
    print(next(gerador))