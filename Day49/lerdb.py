import sqlite3

conexao = sqlite3.connect("bancopy.db")

cursor = conexao.cursor()
print("conectado ao banco de dados")

### LER DADOS DA TABELA ###
cursor.execute("""
               SELECT * FROM personagens
               """)
personagens = cursor.fetchall()
print("Dados lidos com sucesso.")

print("Personagens:")
for personagem in personagens:
    print(f"ID: {personagem[0]}, Nome: {personagem[1]}, Poder: {personagem[2]}, Universo: {personagem[3]}")

cursor.close()
conexao.close()