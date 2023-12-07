from datetime import date
from classes import Usuario
import sqlite3

import sqlite3
database = 'academia.db'
con = sqlite3.connect(database, check_same_thread=False)  # CRIA CONEXÃO
cur = con.cursor()  # CRIA CURSOR

def verificar_login(login, senha):
    dados = cur.execute('SELECT * FROM tb_usuario WHERE usuario=? AND senha=?', (login, senha))
    return cur.fetchone() is not None



