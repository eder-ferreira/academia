from datetime import date
from numpy import random
from classes import Aluno
from classes import Usuario
from classes import Funcionario
from classes import Cargo
from classes import Plano
from classes import Endereco
from Defs.listar import listar_cargo


import sqlite3
database = './academia.db'
con = sqlite3.connect(database, check_same_thread=False)  # CRIA CONEXÃO
cur = con.cursor()  # CRIA CURSOR


def cadastrar_aluno():
    print("\n<<<<<= CADASTRAR ALUNOS =>>>>>")
    matricula = random.randint(1, 10000000)
    nome_cliente = input("Digite o nome=> ")
    tipo_doc = input("Informe o tpo de documento [CPF-RG-Passaport-Outros]=> ")
    n_documento = input("Digite o numero do documento=> ")
    telefone = input("Digite o telefone=> ")
    genero = input("Digite o sexo [M ou F]=> ")
    status = 'Ativo'
    data_cadastro = date.today()
    data_nascimento = input("Digite sua data de nascimento [aaaa-mm-dd]=> ")
    aluno = Aluno(id='',matricula=matricula, nome=nome_cliente, tipo_documento=tipo_doc, num_documento=n_documento,
                  telefone=telefone, genero=genero, status=status, dt_cadastro=data_cadastro,
                  dt_nascimento=data_nascimento)
    cur.execute("INSERT INTO tb_aluno(id, matricula, nome, tipo_documento, num_documento, telefone, "
                "genero, status, dt_cadastro, dt_nascimento)VALUES(null,?,?,?,?,?,?,?,?,?)",
        (aluno.matricula, aluno.nome, aluno.tipo_documento, aluno.num_documento, aluno.telefone,
         aluno.genero, aluno.status, aluno.dt_cadastro, aluno.dt_nascimento))
    con.commit()

    # INSERE O REGISTRO DO ALUNO NA TABELA USUARIO
    cur.execute(
        "INSERT INTO tb_usuario(matricula, nome, tipo_documento, num_documento, dt_nascimento, dt_cadastro)VALUES(?,?,?,?,?,?)",
        (aluno.matricula, aluno.nome, aluno.tipo_documento, aluno.num_documento,
         aluno.dt_nascimento, aluno.dt_cadastro))
    con.commit()

    # INSERE O REGISTRO DO USUARIO NA TABELA ENDEREÇO
    cur.execute(
        "INSERT INTO tb_endereco(matricula, nome)VALUES(?,?)",
        (aluno.matricula, aluno.nome))
    con.commit()

    print("Registros cadastrados na Tabela Cliente!")


def cadastrar_usuario():
    print("\n<<<<<= CADASTRAR USUARIO =>>>>>")
    matricula = random.randint(1, 10000000)
    usuario = input("Digite o usuario=> ")
    senha = input("Digite a senha=> ")
    nome = input("Digite o nome=> ")
    email = input("Digite o email=> ")
    tipo_doc = input("Informe o tpo de documento [CPF-RG-Passaport-Outros]=> ")
    n_documento = input("Digite o numero do documento=> ")
    status = 'Ativo'
    data_cadastro = date.today()
    data_nascimento = input("Digite sua data de nascimento [aaaa-mm-dd]=> ")

    usuario = Usuario(id='', matricula=matricula, usuario=usuario, senha=senha, nome=nome, email=email,
                      tipo_documento=tipo_doc, num_documento=n_documento, status=status, dt_cadastro=data_cadastro,
                      dt_nascimento=data_nascimento)
    cur.execute("INSERT INTO tb_usuario(id, matricula, usuario, senha, nome, email, tipo_documento, num_documento, "
                "status, dt_cadastro, dt_nascimento)VALUES(null,?,?,?,?,?,?,?,?,?,?)",
        (usuario.matricula, usuario.usuario, usuario.senha, usuario.nome, usuario.email,
         usuario.tipo_documento, usuario.num_documento, usuario.status, usuario.dt_cadastro,
         usuario.dt_nascimento))
    con.commit()

# INSERE O REGISTRO DO USUARIO NA TABELA ALUNO
    cur.execute("INSERT INTO tb_aluno(matricula, nome, tipo_documento, num_documento, dt_nascimento, "
                "dt_cadastro,status)VALUES(?,?,?,?,?,?,?)",
                (usuario.matricula, usuario.nome, usuario.tipo_documento,
                 usuario.num_documento, usuario.dt_nascimento, usuario.dt_cadastro, usuario.status))
    con.commit()

# INSERE O REGISTRO DO USUARIO NA TABELA ENDEREÇO
    cur.execute(
        "INSERT INTO tb_endereco(matricula, nome)VALUES(?,?)",
        (usuario.matricula, usuario.nome))
    con.commit()
    print("Usuário criado com sucesso!!!")
    print("\033[0;34mRegistros cadastrados na Tabela Usuario!\033[0;0m")
    print("\033[0;34mRegistros criado na Tabela Aluno!\033[0;0m")
    print("\033[0;34mRegistros criado na Tabela Endereço!\033[0;0m")

def cadastrar_funcionario():
    print("\n<<<<<= CADASTRAR FUNCIONARIO =>>>>>")
    nome = input("Digite o nome=> ")
    tipo_doc = input("Informe o tpo de documento [CPF-RG-Passaport-Outros]=> ")
    n_documento = input("Digite o numero do documento=> ")
    telefone = input("Digite o telefone=> ")
    email = input("Digite o email=> ")
    data_nascimento = input("Digite sua data de nascimento [aaaa-mm-dd]=> ")
    genero = input("Digite o sexo [M ou F]=> ")
    matricula = random.randint(1, 10000000)
    status = 'Ativo'
    data_contratacao = input("Informe a data de contratação [aaaa-mm-dd]=> ")
    data_desligamento = ''
    cargo_id = input("Informe o codigo do cargo=> ")
    data_cadastro = date.today()

    funcionario = Funcionario(id='', nome=nome, tipo_documento=tipo_doc, num_documento=n_documento,
                              telefone=telefone, email=email, dt_nascimento=data_nascimento, genero=genero,
                              matricula=matricula, status=status, dt_contratacao=data_contratacao,
                              dt_desligamento=data_desligamento, cargo_id=cargo_id, dt_cadastro=data_cadastro)

    cur.execute("INSERT INTO tb_funcionario(id, nome, tipo_documento, num_documento, "
                "telefone, email, dt_nascimento, genero, matricula, status, dt_contratacao, "
                "dt_desligamento, cargo_id, dt_cadastro)VALUES(null,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                (funcionario.nome, funcionario.tipo_documento, funcionario.num_documento,
                 funcionario.telefone, funcionario.email, funcionario.dt_nascimento, funcionario.genero,
                 funcionario.matricula, funcionario.status, funcionario.dt_contratacao, funcionario.dt_desligamento,
                 funcionario.cargo_id, funcionario.dt_cadastro))
    con.commit()
    print("Registros cadastrados na Tabela Funcionario!")


def cadastrar_cargo():
    print("\n<<<<<= CADASTRAR CARGOS E SALARIOS =>>>>>")
    codigo = input("Informe o codigo do cargo=> ")
    nome = input("Digite o nome do cargo=> ")
    setor = input("Digite o setor=> ")
    salario = float(input("Digite o salario base atual=> "))
    data_cadastro = date.today()

    cargo = Cargo(id='', codigo=codigo, nome=nome, setor=setor, salario=salario, dt_cadastro=data_cadastro)
    cur.execute("INSERT INTO tb_cargo(id, codigo, nome, setor, salario_base, dt_cadastro)VALUES(null,?,?,?,?,?)",
        (cargo.codigo, cargo.nome, cargo.setor, cargo.salario, cargo.dt_cadastro))
    con.commit()
    print("Registros cadastrados na Tabela Cargos e Salarios!")


def cadastrar_plano():
    print("\n<<<<<= CADASTRAR PLANOS - MENSAL =>>>>>")
    codigo = input("Digite o codigo do plano=> ")
    descricao = input("Digite o nome do plano=> ")
    nivel = input("Digite o nivel [Basico-Intermediario-Avancado]=> ")
    valor = float(input("Digite o valor da mensalidadel=> "))
    status = 'Ativo'
    data_cadastro = date.today()

    plano = Plano(id=id, codigo=codigo, descricao=descricao, nivel=nivel, valor=valor,status=status, dt_cadastro=data_cadastro)
    cur.execute("INSERT INTO tb_plano(id, codigo, descricao, nivel, valor, status, dt_cadastro)VALUES(null,?,?,?,?,?,?)",
        (plano.codigo, plano.descricao, plano.nivel, plano.valor, plano.status, plano.dt_cadastro))
    con.commit()
    print("Registros cadastrados na Tabela Planos!")

def cadastrar_endereco():
    print("\n<<<<<= CADASTRAR ENDEREÇO =>>>>>")
    matricula = ''
    nome = ''
    rua = input("Informe a [Rua-Av-Travessa]=> ")
    numero = input("Digite o número ou [S/N]=> ")
    complemento = input("Informe o complemento=> ")
    cep = input("Digite o CEP=> ")
    bairro = input("Digite o Bairro=> ")
    cidade = input("Digite a Cidade=> ")
    estado = input("Digite o Estado=> ")

    endereco = Endereco(id='', matricula=matricula, nome=nome, rua=rua, numero=numero, complemento=complemento,cep=cep, bairro=bairro,cidade=cidade, estado=estado)
    cur.execute("INSERT INTO tb_endereco(id, rua, numero, complemento, cep, bairro, cidade, estado)VALUES(null,?,?,?,?,?,?,?,?)",
        (endereco.matricula, endereco.nome, endereco.rua, endereco.numero, endereco.complemento, endereco.cep, endereco.bairro, endereco.cidade, endereco.estado))
    con.commit()
    print("Registros cadastrados na Tabela Endereços!")