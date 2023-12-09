import sqlite3
database = 'academia.db'
con = sqlite3.connect(database, check_same_thread=False)  # CRIA CONEXÃO
cur = con.cursor()  # CRIA CURSOR


def atualiza_aluno():
    print("\n<<<<<= ATUALIZAR ALUNO =>>>>>")
    id = input("Informe o Id a ser atualizado => ")
    campo = input("Informe o Campo a ser atualizado => ")
    valor = input("Informe o novo valor => ")
    cur.execute(f'''UPDATE tb_aluno SET '{campo}' == '{valor}' WHERE id == '{id}' ''')
    con.commit()
    print(f"O Id: {id} no campo: {campo} foi atualizado para: {valor}")

    cur.execute(f'''UPDATE tb_usuario SET '{campo}' == '{valor}' WHERE id == '{id}' ''')
    con.commit()

def atualiza_usuario():
    print("\n<<<<<= ATUALIZAR USUARIO =>>>>>")
    id = input("Informe o Id a ser atualizado => ")
    campo = input("Informe o Campo a ser atualizado => ")
    valor = input("Informe o novo valor => ")
    cur.execute(f'''UPDATE tb_usuario SET '{campo}' == '{valor}' WHERE id == '{id}' ''')
    con.commit()
    print(f"O Id: {id} no campo: {campo} foi atualizado para: {valor}")

    cur.execute(f'''UPDATE tb_aluno SET '{campo}' == '{valor}' WHERE id == '{id}' ''')
    con.commit()

def atualiza_funcionario():
    print("\n<<<<<= ATUALIZAR FUNCIONARIO =>>>>>")
    id = input("Informe o Id a ser atualizado => ")
    campo = input("Informe o Campo a ser atualizado => ")
    valor = input("Informe o novo valor => ")
    cur.execute(f'''UPDATE tb_funcionario SET '{campo}' == '{valor}' WHERE id == '{id}' ''')
    con.commit()
    print(f"O Id: {id} no campo: {campo} foi atualizado para: {valor}")

def atualiza_cargo():
    print("\n<<<<<= ATUALIZAR CARGO =>>>>>")
    id = input("Informe o Id a ser atualizado => ")
    campo = input("Informe o Campo a ser atualizado => ")
    valor = input("Informe o novo valor => ")
    cur.execute(f'''UPDATE tb_cargo SET '{campo}' == '{valor}' WHERE id == '{id}' ''')
    con.commit()
    print(f"O Id: {id} no campo: {campo} foi atualizado para: {valor}")

def atualiza_plano():
    print("\n<<<<<= ATUALIZAR PLANO =>>>>>")
    id = input("Informe o Id a ser atualizado => ")
    campo = input("Informe o Campo a ser atualizado => ")
    valor = input("Informe o novo valor => ")
    cur.execute(f'''UPDATE tb_plano SET '{campo}' == '{valor}' WHERE id == '{id}' ''')
    con.commit()
    print(f"O Id: {id} no campo: {campo} foi atualizado para: {valor}")

def atualiza_endereco():
    print("\n<<<<<= ATUALIZAR ENDEREÇO =>>>>>")
    id = input("Informe o Id a ser atualizado => ")
    campo = input("Informe o Campo a ser atualizado => ")
    valor = input("Informe o novo valor => ")
    cur.execute(f'''UPDATE tb_endereco SET '{campo}' == '{valor}' WHERE id == '{id}' ''')
    con.commit()
    print(f"O Id: {id} no campo: {campo} foi atualizado para: {valor}")