class Pessoa:
    def __init__(self, id, nome, tipo_documento, num_documento, telefone, genero, dt_nascimento):
        self.id = id
        self.nome = nome
        self.tipo_documento = tipo_documento  #'RG', 'CPF', 'CNH', 'PASSAPORTE', 'OUTRO'
        self.num_documento = num_documento
        self.telefone = telefone
        self.genero = genero                  # M / F
        self.dt_nascimento = dt_nascimento


class Usuario:
    def __init__(self, id, matricula, usuario, senha, nome, email, tipo_documento, num_documento,status, dt_cadastro, dt_nascimento):
        self.id = id
        self.matricula = matricula
        self.usuario = usuario
        self.senha = senha
        self.nome = nome
        self.email = email
        self.tipo_documento = tipo_documento  #'RG', 'CPF', 'CNH', 'PASSAPORTE', 'OUTRO'
        self.num_documento = num_documento
        self.status = status                # ATIVO / INATIVO
        self.dt_cadastro = dt_cadastro
        self.dt_nascimento = dt_nascimento


class Aluno(Pessoa):
    def __init__(self, id, matricula, status, dt_cadastro, nome, tipo_documento, num_documento, telefone, genero,dt_nascimento):
        super().__init__(id, nome, tipo_documento, num_documento, telefone, genero, dt_nascimento)
        self.id = id
        self.matricula = matricula
        self.status = status                # ATIVO / INATIVO
        self.dt_cadastro = dt_cadastro


class Funcionario(Pessoa):
    def __init__(self, id, nome, tipo_documento, num_documento, telefone,dt_nascimento, genero, matricula, status, dt_contratacao,dt_desligamento,cargo_id,dt_cadastro, email):
        super().__init__(id, nome, tipo_documento, num_documento, telefone, genero, dt_nascimento)
        self.id = id
        self.matricula = matricula
        self.status = status                # ATIVO / INATIVO
        self.dt_contratacao = dt_contratacao
        self.dt_desligamento = dt_desligamento
        self.cargo_id = cargo_id
        self.dt_cadastro = dt_cadastro
        self.email = email


class Cargo:
    def __init__(self, id, codigo, nome, setor, salario, dt_cadastro):
        self.id = id
        self.codigo = codigo
        self.nome = nome
        self.setor = setor
        self.salario = salario
        self.dt_cadastro = dt_cadastro


class Plano:
    def __init__(self, id, codigo, descricao, nivel, valor, status, dt_cadastro):
        self.id = id
        self.codigo = codigo
        self.descricao = descricao
        self.nivel = nivel                  # INICIANTE, INTERMEDIARIO, AVANÇADO
        self.valor = valor
        self.status = status                # ATIVO / INATIVO
        self.dt_cadastro = dt_cadastro


class Endereco:
    def __init__(self, id, matricula, nome, rua, numero, complemento, cep, bairro, cidade, estado):
        self.id = id
        self.matricula = matricula
        self.nome = nome
        self.rua = rua
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado