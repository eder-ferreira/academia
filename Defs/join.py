from prettytable import PrettyTable
from datetime import datetime
from datetime import date

import sqlite3
database = './academia.db'
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

def join_usuario_aluno_endereco():
    print(f"\nRELATORIO GERADO DAS TABELAS (tb_aluno - tb_usuario - tb_endereco) !")
    cur.execute("""SELECT tb_usuario.matricula, tb_usuario.nome, 
    tb_aluno.telefone, tb_usuario.email, tb_aluno.dt_nascimento, strftime('%Y', 'now') - strftime('%Y', tb_aluno.dt_nascimento) 
    AS idade, tb_endereco.rua, tb_endereco.numero, tb_endereco.cep, tb_endereco.bairro, 
    tb_endereco.cidade, tb_endereco.estado
    FROM tb_usuario 
    INNER JOIN tb_aluno ON tb_usuario.matricula = tb_aluno.matricula
    INNER JOIN tb_endereco ON tb_aluno.matricula = tb_endereco.matricula""")

    resultados = cur.fetchall()
    tabela = PrettyTable()
    tabela.field_names =["Matricula", "Nome", "Telefone", "E-mail", "Data Nascimento","Idade","Rua","Numero","CEP","Bairro","Cidade","Estado"]
    for row in resultados:
        tabela.add_row(row)
    print(tabela)

def salarios():
    global escolha
    escolha = input("""Digite a quantidade de linhas Ex.:Top 5 =>  """)
    cur.execute(f""" SELECT nome, setor, salario_base FROM tb_cargo ORDER BY salario_base DESC LIMIT {escolha} """)


    resultados = cur.fetchall()
    tabela = PrettyTable()
    tabela.field_names = [desc[0] for desc in cur.description]
    for row in resultados:
        tabela.add_row(row)
    print(tabela)

def aniversario():

    # cur.execute("""SELECT strftime('%d-%m-%Y', 'now')""")
    # cur.execute("""SELECT * FROM tb_funcionario WHERE dt_nascimento BETWEEN '1900-01-01' AND '2000-01-01'""")
    # cur.execute(f"""SELECT nome, dt_nascimento FROM tb_funcionario WHERE strftime('%m', dt_nascimento) = '{mes}'""")

    mes = input("Insira o mês dos aniversariantes => ")
    cur.execute(f"""SELECT nome, dt_nascimento, strftime('%Y', 'now') - strftime('%Y', dt_nascimento) AS idade FROM 
    tb_funcionario WHERE strftime('%m', dt_nascimento) = '{mes}'""")
    print(f"\nPARABÉNS AOS ANIVERSARIANTES NO MÊS {mes}!")
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

def idade():
    cur.execute("""
    SELECT nome, dt_nascimento, strftime('%Y', 'now') - strftime('%Y', dt_nascimento) 
    AS idade
    FROM tb_funcionario
    """)

    resultados = cur.fetchall()
    tabela = PrettyTable()
    tabela.field_names = [desc[0] for desc in cur.description]
    for row in resultados:
        tabela.add_row(row)
    print(tabela)

def gera_grafico_salario():
    cur.execute(f""" SELECT setor, salario_base FROM tb_cargo ORDER BY salario_base DESC LIMIT {escolha} """)
    resultados = cur.fetchall()
    nome, setor = zip(*resultados)

    # Criar o gráfico
    import matplotlib.pyplot as plt
    plt.style.use("Solarize_Light2")
    nome, setor = zip(*resultados)
    plt.bar(nome, setor, label='Setor',color="b")

    plt.xlabel('Setor')
    plt.ylabel('Salário')
    plt.title('Salário por Setor')
    plt.legend()
    plt.xticks(rotation=45)
    plt.show()

def alunos_matriculados_mes():
    ano = input("Insira o ano da pesquisa => ")
    cur.execute(f"""
    SELECT strftime('%m', dt_cadastro) AS mes, 
    COUNT(*) AS qtde_matriculas 
    FROM tb_aluno
    WHERE (strftime('%Y', dt_cadastro) = '{ano}')
    GROUP BY mes 
    ORDER BY mes""")

    print(f"\nALUNOS MATRICULADO NO ANO {ano} POR MES!")
    resultados = cur.fetchall()
    tabela = PrettyTable()
    tabela.field_names = [desc[0] for desc in cur.description]
    for row in resultados:
        tabela.add_row(row)
    print(tabela)


    # Criar o gráfico
    import matplotlib.pyplot as plt
    plt.style.use("Solarize_Light2")
    mes, qtde_matriculas = zip(*resultados)
    plt.bar(mes, qtde_matriculas, label='Qtde',color="g")

    plt.xlabel('Mês')
    plt.ylabel('Quantidade')
    plt.title(f'Alunos matriculados no ano {ano} por mês')
    plt.legend()
    plt.xticks(rotation=45)
    plt.show()