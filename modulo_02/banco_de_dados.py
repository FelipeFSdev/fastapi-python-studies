import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent  # caminho para diretório específico

# criação do banco em diretório específico
conn = sqlite3.connect(ROOT_PATH/"banco_de_dados.sqlite")
cur = conn.cursor()


def criar_tabela(conn, cur):
    sql = 'CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150));'

    cur.execute(sql)
    conn.commit()


def inserir_registro(conn, cur, nome, email):
    sql = "INSERT INTO clientes (nome, email) VALUES (?,?);"
    data = (nome, email)  # tupla com dados a serem inseridos

    cur.execute(sql, data)
    conn.commit()


def atualizar_registro(conn, cur, nome, email, id):
    data = (nome, email, id)
    sql = "UPDATE clientes SET nome=?, email=? WHERE id=?;"

    cur.execute(sql, data)
    conn.commit()


def remover_registro(conn, cur, id):
    data = (id,)
    sql = "DELETE FROM clientes WHERE id = ?;"

    cur.execute(sql, data)
    conn.commit()


def inserir_varios(conn, cur, dados):
    sql = "INSERT INTO  clientes (nome,email) VALUES (?,?);"

    try:
        cur.executemany(sql, dados)
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()


def consultar_registros(cur):
    sql = "SELECT * FROM clientes;"

    cur.execute(sql)
    results = cur.fetchall()

    for client in results:
        print(client)


def consultar_unico_registro(cur, id):
    sql = "SELECT * FROM clientes WHERE id=?;"
    data = (id,)

    cur.execute(sql, data)
    result = cur.fetchone()

    print(result)
