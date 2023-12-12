from prettytable import PrettyTable
import sqlite3

database = './academia.db'
con = sqlite3.connect(database, check_same_thread=False)  # CRIA CONEXÃO
cur = con.cursor()  # CRIA CURSOR


def buscar_aluno():
    print("\n<<<<<= BUSCAR ALUNO =>>>>>")
    busca = input("Digite um nome ou id para pesquisar=> ")
    resultados = cur.execute(f"SELECT * FROM tb_aluno WHERE lower(nome) LIKE ? OR id = ?", (f"%{busca.lower()}%", busca))

    resultados = cur.fetchall()
    tabela = PrettyTable()
    tabela.field_names = [desc[0] for desc in cur.description]
    for row in resultados:
        tabela.add_row(row)
    print(tabela)


def buscar_usuario():
    print("\n<<<<<= BUSCAR USUARIO =>>>>>")
    busca = input("Digite um id ou nome para pesquisar=> ")
    resultados = cur.execute(f"SELECT * FROM tb_usuario WHERE lower(nome) LIKE ? OR id = ?", (f"%{busca.lower()}%", busca))

    resultados = cur.fetchall()
    tabela = PrettyTable()
    tabela.field_names = [desc[0] for desc in cur.description]
    for row in resultados:
        tabela.add_row(row)
    print(tabela)


def buscar_funcionario():
    print("\n<<<<<= BUSCAR FUNCIONARIO =>>>>>")
    busca = input("Digite um nome ou id para pesquisar=> ")
    resultados = cur.execute(f"SELECT * FROM tb_funcionario WHERE lower(nome) LIKE ? OR id = ?", (f"%{busca.lower()}%", busca))

    resultados = cur.fetchall()
    tabela = PrettyTable()
    tabela.field_names = [desc[0] for desc in cur.description]
    for row in resultados:
        tabela.add_row(row)
    print(tabela)


def buscar_cargo():
    print("\n<<<<<= BUSCAR CARGOS E SALARIOS =>>>>>")
    busca = input("Digite o codigo, nome ou setor para pesquisar=> ")
    resultados = cur.execute(
        f"SELECT *FROM tb_cargo WHERE codigo = ? OR lower(nome) LIKE ? OR setor = ?", (busca,f"%{busca.lower()}%", busca))

    resultados = cur.fetchall()
    tabela = PrettyTable()
    tabela.field_names = [desc[0] for desc in cur.description]
    for row in resultados:
        tabela.add_row(row)
    print(tabela)


def buscar_plano():
    print("\n<<<<<= BUSCAR PLANOS - MENSAL =>>>>>")
    busca = input("Digite o codigo, descrição ou nivel para pesquisar=> ")
    resultados = cur.execute(
        f"SELECT *FROM tb_plano WHERE codigo = ? or lower(descricao) LIKE ?  or lower(nivel) LIKE ?",(busca, f"%{busca.lower()}%", f"%{busca.lower()}%"))

    resultados = cur.fetchall()
    tabela = PrettyTable()
    tabela.field_names = [desc[0] for desc in cur.description]
    for row in resultados:
        tabela.add_row(row)
    print(tabela)


def buscar_endereco():
    print("\n<<<<<= BUSCAR ENDEREÇO =>>>>>")
    busca = input("Digite o Nome da Rua ou cidade ou Bairro ou cep para pesquisar=> ")
    resultados = cur.execute(
        f"SELECT *FROM tb_endereco WHERE rua = '{busca}' or cep = '{busca}' or bairro = '{busca}' or cidade = '{busca}'")
    resultados = cur.fetchall()
    tabela = PrettyTable()
    tabela.field_names = [desc[0] for desc in cur.description]
    for row in resultados:
        tabela.add_row(row)
    print(tabela)