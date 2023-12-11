from prettytable import PrettyTable
from datetime import datetime
from datetime import date

import sqlite3
database = 'academia.db'
con = sqlite3.connect(database, check_same_thread=False)
cur = con.cursor()


def join_funcionario_cargo():
    # Executar a consulta INNER JOIN
    cur.execute("""
        SELECT tb_funcionario.id, tb_funcionario.nome, tb_funcionario.matricula, 
        tb_cargo.nome, tb_cargo.setor, tb_cargo.salario_base
        FROM tb_funcionario
        INNER JOIN tb_cargo ON tb_funcionario.cargo_id = tb_cargo.codigo
    """)

    # Obter os resultados
    resultados = cur.fetchall()

    # Imprimi resultado
    # for resultado in resultados:
    #     print(resultado)

    tabela = PrettyTable()
    tabela.field_names =["Id","Funcionario", "Matricula", "Cargo", "Setor", "Salario"]
    for row in resultados:
        tabela.add_row(row)
    print(tabela)


def salarios():

    escolha = input("""Digite a quantidade de linhas Ex.:Top 5 =>  """)

    cur.execute(f""" SELECT nome, setor, salario_base FROM tb_cargo ORDER BY salario_base DESC LIMIT {escolha} """)
    # Obter os resultados
    resultados = cur.fetchall()

    # Imprimi resultado
    # for resultado in resultados:
    #     print(resultado)

    tabela = PrettyTable()
    tabela.field_names = [desc[0] for desc in cur.description]
    for row in resultados:
        tabela.add_row(row)
    print(tabela)


def aniversario():

    # cur.execute("""SELECT strftime('%d-%m-%Y', 'now')""")
    # cur.execute("""SELECT * FROM tb_funcionario WHERE dt_nascimento BETWEEN '1900-01-01' AND '2000-01-01'""")
    mes = input("Insira o mês dos aniversariantes => ")
    cur.execute(f"""SELECT nome, dt_nascimento FROM tb_funcionario WHERE strftime('%m', dt_nascimento) = '{mes}'""")

    resultados = cur.fetchall()
    tabela = PrettyTable()
    tabela.field_names = [desc[0] for desc in cur.description]
    for row in resultados:
        tabela.add_row(row)
    print(tabela)



def calculaIdade():
    nome = input('Digite o nome: ')
    sobrenome = input('Digite o sobrenome: ')
    nascimento = input('Digite a data de nascimento: ')
    idade = date.today().year - datetime.strptime(nascimento, '%d/%m/%Y').year
    print(f'Olá! O nome completo é {nome} {sobrenome} e hoje você tem {idade} anos')

calculaIdade()