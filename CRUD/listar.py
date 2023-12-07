from prettytable import PrettyTable
import sqlite3

database = 'academia.db'
con = sqlite3.connect(database, check_same_thread=False)  # CRIA CONEXÃO
cur = con.cursor()  # CRIA CURSOR


def listar_aluno():

    print("\n<<<<<= LISTAR ALUNOS =>>>>>")
    cur.execute("""SELECT * FROM tb_aluno;
    """)
    resultados = cur.fetchall()
    tabela = PrettyTable()
    tabela.field_names = [desc[0] for desc in cur.description]
    for row in resultados:
        tabela.add_row(row)
    print(tabela)


def listar_usuario():
    print("\n<<<<<= LISTAR USUARIO =>>>>>")
    cur.execute("""SELECT * FROM tb_usuario;
    """)
    resultados = cur.fetchall()
    tabela = PrettyTable()
    tabela.field_names = [desc[0] for desc in cur.description]
    for row in resultados:
        tabela.add_row(row)
    print(tabela)


def listar_funcionario():
    print("\n<<<<<= LISTAR FUNCIONARIO =>>>>>")
    cur.execute("""SELECT * FROM tb_funcionario;
    """)
    resultados = cur.fetchall()

    tabela = PrettyTable()
    tabela.field_names = [desc[0] for desc in cur.description]
    for row in resultados:
        tabela.add_row(row)
    print(tabela)


def listar_cargo():
    print("\n<<<<<= LISTAR CARGOS E SALARIOS =>>>>>")
    cur.execute("""SELECT * FROM tb_cargo;
    """)
    resultados = cur.fetchall()
    tabela = PrettyTable()
    tabela.field_names = [desc[0] for desc in cur.description]
    for row in resultados:
        tabela.add_row(row)
    print(tabela)


def listar_plano():
    print("\n<<<<<= LISTAR PLANOS - MENSAL =>>>>>")
    cur.execute("""SELECT * FROM tb_plano;
    """)
    resultados = cur.fetchall()
    tabela = PrettyTable()
    tabela.field_names = [desc[0] for desc in cur.description]
    for row in resultados:
        tabela.add_row(row)
    print(tabela)


def listar_endereco():
    print("\n<<<<<= LISTAR ENDEREÇO =>>>>>")
    cur.execute("""SELECT * FROM tb_endereco;
    """)
    resultados = cur.fetchall()
    tabela = PrettyTable()
    tabela.field_names = [desc[0] for desc in cur.description]
    for row in resultados:
        tabela.add_row(row)
    print(tabela)