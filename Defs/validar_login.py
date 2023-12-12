import sqlite3
database = 'Defs/academia.db'
con = sqlite3.connect(database, check_same_thread=False)  # CRIA CONEXÃO
cur = con.cursor()  # CRIA CURSOR

from Defs.cadastrar import cadastrar_usuario
def autentica_login(login, senha):
    dados = cur.execute('SELECT * FROM tb_usuario WHERE usuario=? AND senha=?', (login, senha))
    return cur.fetchone() is not None


def cad_user():
    return cadastrar_usuario()




