import time

#criando o decorator
def medir_tempo_execucao(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f"Tempo de execução: {fim - inicio} segundos")
        return resultado
    return wrapper

#nao pode deicar espaco 
@medir_tempo_execucao
def tarefa_1():
    print("Iniciando tarefa 1...")
    time.sleep(2)
    print("Tarefa 1 concluída.")

tarefa_1()