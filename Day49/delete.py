import sqlite3

conexao = sqlite3.connect("bancopy.db")

cursor = conexao.cursor()
print("conectado ao banco de dados")

### DELETAR DADOS NA TABELA ###
cursor.execute("""
               DELETE FROM personagens
               WHERE nome = "NARUTO"
               """)
conexao.commit()
print("Dados deletados com sucesso.")

cursor.close()
conexao.close()