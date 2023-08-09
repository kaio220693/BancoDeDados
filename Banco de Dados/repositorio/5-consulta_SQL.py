import sqlite3 as s

db = "estoque.db"

conex = s.connect(db)
cursor = conex.cursor()

cursor.execute("SELECT tbCod, tbNome, tbQtde From tabProd")

linha = cursor.fetchone()

for elemento in linha:
    print(elemento)

cursor.close()
conex.close()