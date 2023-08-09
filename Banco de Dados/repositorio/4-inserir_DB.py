import sqlite3 as s

db = "estoque.db" #Variavel para guardar o nome do bando

conex = s.connect(db)
cursor = conex.cursor()

resp = 'S' # Variavel de conteole do While
inserir = "n"

while(resp.upper() == 'S'):
    try:
        w_cod = int(input("Código do Produto: "))
        w_nome = input("Nome do Produto: ")
        w_qtde = int(input("Quantidade: "))
        w_estado = input("Estado: ")

        cursor.execute('''INSERT INTO tabProd(tbCod, tbNome, tbQtde, tbEstado) 
                VALUES(?,?,?,?)''', (w_cod, w_nome, w_qtde, w_estado))
        
        inserir = "s"
        
    except s.IntegrityError:
        print("============================")
        print("|==> Chave existente", w_cod)
        print("============================")
    resp = input("Deseja continuar? (S/N)")

    if inserir == 's':
        conex.commit()
    cursor.close()
    conex.close()