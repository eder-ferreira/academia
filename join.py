from prettytable import PrettyTable
import sqlite3
def filtra():
    con = sqlite3.connect('academia.db')
    cur = con.cursor()

    # Executar a consulta
    cur.execute("""
        SELECT tb_funcionario.id, tb_funcionario.num_documento, tb_funcionario.nome, tb_funcionario.matricula, tb_cargo.nome, tb_cargo.setor, tb_cargo.salario_base
        FROM tb_funcionario
        INNER JOIN tb_cargo ON tb_funcionario.cargo_id = tb_cargo.codigo
    """)

    # Obter os resultados
    resultados = cur.fetchall()

    # Imprimi resultado
    for resultado in resultados:
        print(resultado)

    tabela = PrettyTable()
    tabela.field_names =["Id","Doc_Identificação","Funcionario", "Matricula", "Cargo", "Setor", "Salario"]
    for row in resultados:
        tabela.add_row(row)
    print(tabela)

    con.close()
filtra()


