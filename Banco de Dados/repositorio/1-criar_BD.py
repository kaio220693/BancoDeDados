import sqlite3

conex = sqlite3.connect("estoque.db") # CRIAR CONEXÃO COM BANCO

cursor = conex.cursor() # ENVIAR COMANDOS PARA O BANCO

# EXECUTAR UM CONJUNTO DE COMANDOS        #INTERGER = inteiro
cursor.execute('''
        CREATE TABLE tabProd(tbCod INTEGER PRIMARY KEY,
        tbNome TEXT,
        tbQtde INTEGER,
        tbEstado TEXT)
''')

cursor.close() # FECHAR CURSOR
conex.close() # FECHAR CONEXÃO COM BANCO
