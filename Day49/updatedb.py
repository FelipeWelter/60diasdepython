import sqlite3

conexao = sqlite3.connect("bancopy.db")

cursor = conexao.cursor()
print("conectado ao banco de dados")

### ATUALIZAR DADOS NA TABELA ###
cursor.execute("""
               UPDATE personagens
               SET poder = 9500
               WHERE nome = "NARUTO"
               """)
conexao.commit()
print("Dados atualizados com sucesso.")

cursor.close()
conexao.close()