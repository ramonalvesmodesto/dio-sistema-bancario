import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent
PATH_DATABASE = ROOT_PATH/"database"

con = sqlite3.connect(PATH_DATABASE/"banco.db")
cur = con.cursor()
cur.row_factory = sqlite3.Row

def criar_tabela(con, cur):
    try:
        cur.execute("CREATE TABLE banco (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150) UNIQUE)")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


def inserir_registro(cur, con, dados: tuple):
    try:
        cur.execute("INSERT INTO banco (nome, email) VALUES (?, ?)", dados)
        con.commit()
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        con.rollback()

def inserir_lista_registros(cur, con, dados):
    try:
        cur.executemany("INSERT INTO banco (nome, email) VALUES (?, ?)", dados)
        con.commit()
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        con.rollback()

def atualizar_registro(cur, con, id: str, dados: tuple):
    try:
        cur.execute("UPDATE banco SET nome=?, email=? WHERE id=?", (*dados, id))
        con.commit()
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        con.rollback()

def deletar_registro(cur, con, id: str):
    try:
        cur.execute("DELETE FROM banco WHERE id=?", (id,))
        con.commit()
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        con.rollback()

def recuperar_registro(cur, id: str):
    try:
        cur.execute("SELECT * FROM banco WHERE id=?", (id,))
        return cur.fetchone()
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    
def recuperar_lista_registros(cur):
    try:
        cur.execute("SELECT * FROM banco")
        return cur.fetchall()
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


dados = ("Ramon", "teste@teste")

#criar_tabela(con, cur)
#inserir_registro(cur, con, dados)
#deletar_registro(cur, con, '1')
#atualizar_registro(cur, con,'2' , dados)

# print(dict(recuperar_registro(cur, '3')))

# for dado in recuperar_lista_registros(cur):
#     print(dict(dado))

