import threading
import time

def tarefa(nome, tempo_execucao):
    print(f"Tarefa {nome} iniciada.")
    time.sleep(tempo_execucao)
    print(f"Tarefa {nome} finalizada.")

threading1 = threading.Thread(target=tarefa, args=("Download tarefa 1", 3))
threading2 = threading.Thread(target=tarefa, args=("Download Tarefa 2", 4))

# Inicia as threads
threading1.start()
threading2.start()

#aguardando as tarefas finalizar
threading1.join()
threading2.join()

print("Todas as tarefas foram concluídas.")

