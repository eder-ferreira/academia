import sqlite3
database = './academia.db'
con = sqlite3.connect(database, check_same_thread=False)  # CRIA CONEXÃO
cur = con.cursor()


def excluir_aluno():
    print("\n<<<<<= EXCLUIR ALUNO =>>>>>")
    exclui = input("Informe o id ser excluido => ")
    con.execute(f"DELETE FROM tb_aluno WHERE id == {exclui}")
    con.commit()
    print(f"Registro id: {exclui} excluido com sucesso!!!")


def excluir_usuario():
    print("\n<<<<<= EXCLUIR USUARIO =>>>>>")
    exclui = input("Informe o id ser excluido => ")
    con.execute(f"DELETE FROM tb_usuario WHERE id == '{exclui}' ")
    con.commit()
    print(f"Registro id: {exclui} excluido com sucesso!!!")


def excluir_funcionario():
    print("\n<<<<<= EXCLUIR FUNCIONARIO =>>>>>")
    exclui = input("Informe o id ser excluido => ")
    con.execute(f"DELETE FROM tb_funcionario WHERE id=='{exclui}'")
    con.commit()
    print(f"Registro id: {exclui} excluido com sucesso!!!")


def excluir_cargo():
    print("\n<<<<<= EXCLUIR CARGOS E SALARIOS =>>>>>")
    exclui = input("Informe o id ser excluido => ")
    con.execute(f"DELETE FROM tb_cargo WHERE id =='{exclui}'")
    con.commit()
    print(f"Registro id: {exclui} excluido com sucesso!!!")


def excluir_plano():
    print("\n<<<<<= EXCLUIR PLANOS - MENSAL =>>>>>")
    exclui = input("Informe o id ou codigo ser excluido => ")
    con.execute(f"DELETE FROM tb_plano WHERE id =='{exclui}' or codigo == '{exclui}'")
    con.commit()
    print(f"Registro id: {exclui} excluido com sucesso!!!")


def excluir_endereco():
    print("\n<<<<<= EXCLUIR ENDEREÇO =>>>>>")
    exclui = input("Informe o id ou rua ser excluido => ")
    con.execute(f"DELETE FROM tb_endereco WHERE id =='{exclui}' or rua == '{exclui}'")
    con.commit()
    print(f"Registro id: {exclui} excluido com sucesso!!!")