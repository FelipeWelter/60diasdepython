#pip install plotext --break-system-packages
import plotext as plt

power_levels = {
    "felipe": 10000,
    "sophia": 5000,
    "carlos": 1000,
    "ana": 12,
    "alicia": 89,
}

personagens = list(power_levels.keys())
poderes = list(power_levels.values())

plt.title("Níveis de Poder dos Personagens")
plt.xlabel("Personagens")
plt.ylabel("Nível de Poder")
plt.bar(personagens, poderes, label="Nivel de poder")
plt.show()