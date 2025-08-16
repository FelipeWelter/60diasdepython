class Ninja:
    def __init__(self, nome, chakara):
        self.nome = nome
        self.chakara = chakara

    def usar_jutsu(self, custo_chakara):
        try:
            if custo_chakara > self.chakara:
                raise ValueError("Chakara insuficiente para usar o jutsu.")
            self.chakara -= custo_chakara
            print(f"{self.nome} usou um jutsu e agora tem {self.chakara} de chakara restante.")
        except ValueError as Error:
            print(f"Erro: {Error} Foi detectado. o {self.nome} não pode usar o jutsu.")

if __name__ == "__main__":
    kakashi = Ninja("Kakashi", 100)
    kakashi.usar_jutsu(30)  # Exemplo de uso com sucesso
    kakashi.usar_jutsu(20)   # Tentativa de usar jutsu com chakara insuficiente
