class PersonagemDB:
    def __init__(self, nome, poder, nivel, transformacao="Base"):
        """
        inicializa os atributos do personagem
        self garante que esses atributors são únicos para cada instância
        """
        self.nome = nome
        self.poder = poder
        self.nivel = nivel
        self.transformacao = transformacao

    def exibir_informacoes(self): #exibe as inbformações do personagem
        print(f"Nome: {self.nome}")
        print(f"Poder: {self.poder}")
        print(f"Nível: {self.nivel}")
        print(f"Transformação: {self.transformacao}")

    def treinar(self, horas):
        aumento = horas * 10
        self.poder += aumento
        print(f"{self.nome} treinou por {horas} horas e aumentou seu poder em {aumento}.")

    def transformar(self, nova_transformacao):
        """Altera a transformação do personagem."""

        self.transformacao = nova_transformacao
        print(f"{self.nome} se transformou em {self.transformacao}!")

goku = PersonagemDB("Goku", 9000, 100, "Super Saiyajin")
goku.treinar(horas=5)
goku.transformar("Super Saiyajin Blue")

naruto = PersonagemDB("Naruto", 8000, 95, "Sábio dos Seis Caminhos")
naruto.treinar(horas=3)
naruto.transformar("Kurama Modo Biju")  

def exibir_todos_personagens(personagens):
    """Exibe as informações de todos os personagens."""
    for personagem in personagens:
        personagem.exibir_informacoes()
        print("-" * 30)
personagens = [goku, naruto]
exibir_todos_personagens(personagens)