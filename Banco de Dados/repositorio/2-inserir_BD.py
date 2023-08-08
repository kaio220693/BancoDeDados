import sqlite3 as s

conex = s.connect("estoque.db")
cursor = conex.cursor()

cursor.execute('''
    INSERT INTO tabProd(tbCod, tbNome, tbQtde, tbEstado) 
                VALUES(1, "teclado", 15, "SP")
''')

conex.commit() #Transferindo a informação de memoria para o banco
cursor.close()
conex.close()