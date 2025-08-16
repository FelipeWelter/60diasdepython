class Veiculo:
    def __init__(self, marca, modelo, velocidade_maxima):
        self.marca = marca
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima

    def ligar_motor(self):
        print(f"O motor do {self.marca} {self.modelo} está ligado.")
    
    def acelerar(self, velocidade):
        if velocidade <= self.velocidade_maxima:
            print(f"{self.marca} {self.modelo} acelerou para {velocidade} km/h.")
        else:
            print(f"Velocidade máxima de {self.marca} {self.modelo} é {self.velocidade_maxima} km/h.")
                  
    def ligar_luzes(self):
        print(f"As luzes do {self.marca} {self.modelo} estão ligadas.")

class Carro(Veiculo):
    def __init__(self, marca, modelo, velocidade_maxima, portas):
        super().__init__(marca, modelo, velocidade_maxima)
        self.portas = portas

    def abrir_porta(self):
        print(f"A porta do {self.marca} {self.modelo} está aberta.")

meu_carro = Carro("Toyota", "Corolla", 180, 4)
meu_carro.ligar_motor()
meu_carro.acelerar(150)
meu_carro.ligar_luzes()
meu_carro.abrir_porta()
meu_carro.acelerar(200)  # Testando velocidade acima do máximo