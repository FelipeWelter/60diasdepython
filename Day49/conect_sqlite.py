import sqlite3

conexao = sqlite3.connect("bancopy.db")

cursor = conexao.cursor()
print("conectado ao banco de dados")

### CRIACAO DA TABELA ###
#comentado por ja esta criada a tabela...

#cursor.execute("""
#               CREATE TABLE IF NOT EXISTS personagens
#               (
#                id INTEGER PRIMARY KEY AUTOINCREMENT,
#                nome TEXT NOT NULL,
#                poder INTEGER NOT NULL,
#                universo TEXT NOT NULL)
#               """)

#print("Tabela 'personagens' criada com sucesso.")

### INSERIR DADOS NA TABELA ###
cursor.execute("""
               INSERT INTO personagens (nome, poder, universo)
               VALUES ("NARUTO", 9000, "NARUTO")
               """)
conexao.commit()
print("Dados inseridos com sucesso.")


conexao.close()