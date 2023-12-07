# ----------------------  CRIA BANCO ---------------------------------------
import sqlite3
from random import random

con = sqlite3.connect('academia.db', check_same_thread=False)
cur = con.cursor()
print('Banco de dados academia.db criado!!!')
# ----------------------  CRIA TABELAS ---------------------------------------

with con:
    cur.execute('''CREATE TABLE IF NOT EXISTS 'tb_aluno'(
    'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'matricula' INTEGER NOT NULL,
    'nome' TEXT,
    'tipo_documento' TEXT,
    'num_documento' VARCHAR(10),
    'telefone' VARCHAR(12),
    'genero' VARCHAR(1),
    'status' TEXT,
    'dt_cadastro' DATE,
    'usuario_id' INTEGER,
     FOREIGN KEY("usuario_id") REFERENCES "tb_usuario"("id"))
    ''')

    cur.execute('''CREATE TABLE IF NOT EXISTS 'tb_usuario'(
    'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'usuario' VARCHAR(15) NOT NULL,
    'senha' VARCHAR(10) NOT NULL,
    'nome' VARCHAR(15) NOT NULL,
    'email' VARCHAR(15) NOT NULL,
    'status' TEXT,
    'dt_cadastro' DATE)
    ''')

    cur.execute('''CREATE TABLE IF NOT EXISTS 'tb_funcionario'(
    'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'nome' TEXT,
    'tipo_documento' TEXT,
    'num_documento' VARCHAR(10),
    'telefone' VARCHAR(12),
    'genero' VARCHAR(1),
    'matricula' INTEGER NOT NULL,
    'status' TEXT,
    'dt_contratacao' DATE,
    'dt_desligamento' DATE,
    'cargo_id' INTEGER,
    'usuario_id' INTEGER,
    'dt_cadastro' DATE,
    FOREIGN KEY("cargo_id") REFERENCES "tb_cargo"("codigo"),
    FOREIGN KEY("usuario_id") REFERENCES "tb_usuario"("id")
    )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS 'tb_cargo'(
    'id' INTEGER NOT NULL PRIMARY KEY,
    'codigo' INTEGER,
    'nome' TEXT,
    'setor' TEXT,
    'salario_base' FLOAT,
    'dt_cadastro' DATE)
    ''')

    cur.execute('''CREATE TABLE IF NOT EXISTS 'tb_plano'(
    'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'codigo' INTEGER,
    'descricao' TEXT NOT NULL,
    'nivel' TEXT NOT NULL,
    'valor' FLOAT,
    'status' TEXT,
    'dt_cadastro' DATE,
    'aluno_matricula' INTEGER,
    FOREIGN KEY("aluno_matricula") REFERENCES "tb_aluno"("matricula"))
    ''')

    cur.execute('''CREATE TABLE IF NOT EXISTS 'tb_endereco'(
    'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'rua' TEXT NOT NULL,
    'numero' VARCHAR(10) NOT NULL,
    'complemento' TEXT,
    'cep' VARCHAR(8),
    'bairro' TEXT,
    'cidade' TEXT,
    'estado' TEXT,
    'aluno_matricula' INTEGER,
    'funcionario_matricula' INTEGER,
    FOREIGN KEY("aluno_matricula") REFERENCES "tb_aluno"("matricula"),
    FOREIGN KEY("funcionario_matricula") REFERENCES "tb_funcionario"("matricula")
    )''')

    con.commit()
print('Tabelas Aluno - Usuario - Funcionario - Cargo - Plano - Endereço criadas!!!')


# ----------------------  POPULA TABELA USUARIO ------------------------------
with con:
    cur.execute('''INSERT INTO tb_usuario(usuario, senha, nome, email, status, dt_cadastro)VALUES('admrural','adm123','Eder Ferreira','admrural@gmail.com','Ativo','2023-11-01')''')
    cur.execute('''INSERT INTO tb_usuario(usuario, senha, nome, email, status, dt_cadastro)VALUES('loren','loren','Loren Pires','loren@loren.com','Inativo','2022-11-01')''')
    cur.execute('''INSERT INTO tb_usuario(usuario, senha, nome, email, status, dt_cadastro)VALUES('jleonel','admin','João Leonel Ferreira','jleonel@gmail.com','Ativo','2023-10-01')''')
    cur.execute('''INSERT INTO tb_usuario(usuario, senha, nome, email, status, dt_cadastro)VALUES('luisinha','anapires','Ana Luisa Pires','ana.luisa@ana.com','Ativo','2023-09-01')''')
    cur.execute('''INSERT INTO tb_usuario(usuario, senha, nome, email, status, dt_cadastro)VALUES('luvpof','12345','Luciana Ferreira','lu@gmail.com','Ativo','2023-07-01')''')
    cur.execute('''INSERT INTO tb_usuario(usuario, senha, nome, email, status, dt_cadastro)VALUES('aurora','au3355','Maria Aurora da Silva','aurora@aurora.com','Ativo','2023-03-01')''')
    cur.execute('''INSERT INTO tb_usuario(usuario, senha, nome, email, status, dt_cadastro)VALUES('alice2005','al2023','Alice Ortega','ortega@alice.com','Ativo','2023-01-01')''')
    cur.execute('''INSERT INTO tb_usuario(usuario, senha, nome, email, status, dt_cadastro)VALUES('toniamachado','272ton','Antonia Machado','tonia@gmail.com','Inativo','2023-02-01')''')
    cur.execute('''INSERT INTO tb_usuario(usuario, senha, nome, email, status, dt_cadastro)VALUES('caco79','carlos1979','Carlos Augusto Moraes','caco@caco.com','Ativo','2023-05-01')''')
    cur.execute('''INSERT INTO tb_usuario(usuario, senha, nome, email, status, dt_cadastro)VALUES('arimateia','ari68','José de Arimateia','arimateia@gmail.com','Ativo','2023-08-01')''')
    con.commit()
print("Tabela de Usuarios populada com sucesso!")


# ----------------------  POPULA TABELA FUNCIONARIO ------------------------------
with con:
    cur.execute('''INSERT INTO tb_funcionario(nome, tipo_documento, num_documento, telefone, genero, matricula, status, dt_contratacao,dt_desligamento,cargo_id, usuario_id, dt_cadastro)VALUES('João Santos','CPF',11134577700,'6799996-1792','M','0258433','Ativo','2023-05-01','','','','2023-12-05')''')
    cur.execute('''INSERT INTO tb_funcionario(nome, tipo_documento, num_documento, telefone, genero, matricula, status, dt_contratacao,dt_desligamento,cargo_id, usuario_id, dt_cadastro)VALUES('Arnaldo Fleuri','CPF',09832227700,'6599996-0003','M','0258444','Ativo','2023-05-01','','','','2023-12-05')''')
    cur.execute('''INSERT INTO tb_funcionario(nome, tipo_documento, num_documento, telefone, genero, matricula, status, dt_contratacao,dt_desligamento,cargo_id, usuario_id, dt_cadastro)VALUES('Carlos da Costa','CPF',09555577700,'6999996-0292','M','0258455','Ativo','2023-05-01','','','','2023-12-05')''')
    cur.execute('''INSERT INTO tb_funcionario(nome, tipo_documento, num_documento, telefone, genero, matricula, status, dt_contratacao,dt_desligamento,cargo_id, usuario_id, dt_cadastro)VALUES('João Leonel Ferreira','CPF',09834587600,'3199996-1802','M','0258466','Ativo','2023-05-01','','','','2023-12-05')''')
    cur.execute('''INSERT INTO tb_funcionario(nome, tipo_documento, num_documento, telefone, genero, matricula, status, dt_contratacao,dt_desligamento,cargo_id, usuario_id, dt_cadastro)VALUES('Bruno Guimarães','CPF',09834577321,'6699996-1796','M','0258477','Desligado','2015-05-01','2023-09-01','','','2023-12-05')''')
    cur.execute('''INSERT INTO tb_funcionario(nome, tipo_documento, num_documento, telefone, genero, matricula, status, dt_contratacao,dt_desligamento,cargo_id, usuario_id, dt_cadastro)VALUES('Loren Pires','CPF',00034577700,'2199996-1792','F','0258488','Ativo','2023-05-01','','','','2023-12-05')''')
    cur.execute('''INSERT INTO tb_funcionario(nome, tipo_documento, num_documento, telefone, genero, matricula, status, dt_contratacao,dt_desligamento,cargo_id, usuario_id, dt_cadastro)VALUES('Ana Luisa Oliveira','CPF',09123577700,'6799996-4492','F','0258499','Ativo','2023-05-01','','','','2023-12-05')''')
    cur.execute('''INSERT INTO tb_funcionario(nome, tipo_documento, num_documento, telefone, genero, matricula, status, dt_contratacao,dt_desligamento,cargo_id, usuario_id, dt_cadastro)VALUES('Luciana Ferreira','CPF',09456577700,'1199996-1234','F','0258422','Ativo','2023-05-01','','','','2023-12-05')''')
    cur.execute('''INSERT INTO tb_funcionario(nome, tipo_documento, num_documento, telefone, genero, matricula, status, dt_contratacao,dt_desligamento,cargo_id, usuario_id, dt_cadastro)VALUES('Herminia Assunção','CPF',09830327700,'1699996-4321','F','0258411','Ativo','2023-05-01','','','','2023-12-05')''')
    cur.execute('''INSERT INTO tb_funcionario(nome, tipo_documento, num_documento, telefone, genero, matricula, status, dt_contratacao,dt_desligamento,cargo_id, usuario_id, dt_cadastro)VALUES('Marina de Paula Fonseca','CPF',09834567980,'6799996-1717','F','0258400','Aposentada','1999-05-01','2023-08-01','','','2023-12-05')''')
    con.commit()
print("Tabela de Funcionario populada com sucesso!")

# ----------------------  POPULA TABELA ALUNOS ------------------------------
with con:
    cur.execute('''INSERT INTO tb_aluno(matricula, nome, tipo_documento, num_documento, telefone, genero, status, dt_cadastro, usuario_id)VALUES(0269570,'João da Silva','CPF',09834577700,'6799996-1792','M','Ativo','2019-05-01','')''')
    cur.execute('''INSERT INTO tb_aluno(matricula, nome, tipo_documento, num_documento, telefone, genero, status, dt_cadastro, usuario_id)VALUES(0269571,'José Francisco do Carmo','CPF',09834577722,'6899996-1722','M','Ativo','2023-12-01','')''')
    cur.execute('''INSERT INTO tb_aluno(matricula, nome, tipo_documento, num_documento, telefone, genero, status, dt_cadastro, usuario_id)VALUES(0269572,'Maria José Costa','CPF',09834574400,'6999996-1800','F','Ativo','2023-03-01','')''')
    cur.execute('''INSERT INTO tb_aluno(matricula, nome, tipo_documento, num_documento, telefone, genero, status, dt_cadastro, usuario_id)VALUES(0269573,'Artemio Machado','CPF',09204577700,'1199996-1733','M','Ativo','2023-05-01','')''')
    cur.execute('''INSERT INTO tb_aluno(matricula, nome, tipo_documento, num_documento, telefone, genero, status, dt_cadastro, usuario_id)VALUES(0269574,'Leonel de Paula','CPF',09834577711,'6699996-1392','M','Ativo','2022-02-01','')''')
    cur.execute('''INSERT INTO tb_aluno(matricula, nome, tipo_documento, num_documento, telefone, genero, status, dt_cadastro, usuario_id)VALUES(0269575,'Luiza de Souza','CPF',09834579900,'6599996-1295','F','Ativo','2020-06-01','')''')
    cur.execute('''INSERT INTO tb_aluno(matricula, nome, tipo_documento, num_documento, telefone, genero, status, dt_cadastro, usuario_id)VALUES(0269576,'Loren Pires','CPF',09835577700,'2199996-1891','M','Ativo','2023-05-01','')''')
    cur.execute('''INSERT INTO tb_aluno(matricula, nome, tipo_documento, num_documento, telefone, genero, status, dt_cadastro, usuario_id)VALUES(0269577,'Ana Maria Ferreira','CPF',09832177700,'4499996-1202','F','Ativo','2082-05-01','')''')
    cur.execute('''INSERT INTO tb_aluno(matricula, nome, tipo_documento, num_documento, telefone, genero, status, dt_cadastro, usuario_id)VALUES(0269578,'Amora Oliveira','CPF',09834566600,'6299996-1112','F','Ativo','2023-05-01','')''')
    cur.execute('''INSERT INTO tb_aluno(matricula, nome, tipo_documento, num_documento, telefone, genero, status, dt_cadastro, usuario_id)VALUES(0269579,'Francisca Matos Freitas','CPF',09094577700,'6799996-0093','F','Ativo','1999-07-01','')''')
    con.commit()
print("Tabela de Alunos populada com sucesso!")

# ----------------------  POPULA TABELA CARGOS ------------------------------
with con:
    cur.execute('''INSERT INTO tb_cargo(codigo,nome,setor,salario_base,dt_cadastro) VALUES(111,'Serviços Gerais','Limpeza',1800,'2023-05-01')''')
    cur.execute('''INSERT INTO tb_cargo(codigo,nome,setor,salario_base,dt_cadastro) VALUES(222,'Analista', 'Patrimonio',2800,'2023-05-01')''')
    cur.execute('''INSERT INTO tb_cargo(codigo,nome,setor,salario_base,dt_cadastro) VALUES(333,'Advogado', 'Juridico',3700,'2023-05-01')''')
    cur.execute('''INSERT INTO tb_cargo(codigo,nome,setor,salario_base,dt_cadastro) VALUES(444,'Coordenador', 'Financeiro',4200,'2023-05-01')''')
    cur.execute('''INSERT INTO tb_cargo(codigo,nome,setor,salario_base,dt_cadastro) VALUES(555,'Analista', 'Recursos Humanos',4800,'2023-05-01')''')
    cur.execute('''INSERT INTO tb_cargo(codigo,nome,setor,salario_base,dt_cadastro) VALUES(666,'Gerente', 'Comercial',8000,'2023-05-01')''')
    cur.execute('''INSERT INTO tb_cargo(codigo,nome,setor,salario_base,dt_cadastro) VALUES(777,'Coordenador', 'Planejamento',6800,'2023-05-01')''')
    cur.execute('''INSERT INTO tb_cargo(codigo,nome,setor,salario_base,dt_cadastro) VALUES(888,'Gerente', 'Auditoria', 7000,'2023-05-01')''')
    cur.execute('''INSERT INTO tb_cargo(codigo,nome,setor,salario_base,dt_cadastro) VALUES(999,'Especialista', 'TI', 5000,'2023-05-01')''')
    cur.execute('''INSERT INTO tb_cargo(codigo,nome,setor,salario_base,dt_cadastro) VALUES(101,'Diretor Geral', 'Presidencia',50000,'2023-05-01')''')
    con.commit()
print("Tabela de Cargo e salarios populada com sucesso!")

# ----------------------  POPULA TABELA PLANOS ------------------------------
with con:
    cur.execute('''INSERT INTO tb_plano(codigo,descricao,nivel,valor,status,dt_cadastro,aluno_matricula) VALUES(1001,'Musculação','Basico', 185, 'Ativo','2023-05-01','')''')
    cur.execute('''INSERT INTO tb_plano(codigo,descricao,nivel,valor,status,dt_cadastro,aluno_matricula) VALUES(1002,'Musculação','Intermediario', 250, 'Ativo','2023-05-01','')''')
    cur.execute('''INSERT INTO tb_plano(codigo,descricao,nivel,valor,status,dt_cadastro,aluno_matricula) VALUES(1003,'Musculação','Avançado', 300, 'Ativo','2023-05-01','')''')
    cur.execute('''INSERT INTO tb_plano(codigo,descricao,nivel,valor,status,dt_cadastro,aluno_matricula) VALUES(1004,'Aerobico','Basico', 185, 'Ativo','2023-05-01','')''')
    cur.execute('''INSERT INTO tb_plano(codigo,descricao,nivel,valor,status,dt_cadastro,aluno_matricula) VALUES(1005,'Aerobico','Intermediario', 285, 'Ativo','2023-05-01','')''')
    cur.execute('''INSERT INTO tb_plano(codigo,descricao,nivel,valor,status,dt_cadastro,aluno_matricula) VALUES(1006,'Aerobico','Avançado', 350, 'Ativo','2023-05-01','')''')
    cur.execute('''INSERT INTO tb_plano(codigo,descricao,nivel,valor,status,dt_cadastro,aluno_matricula) VALUES(1007,'Dança','Basico', 200, 'Ativo','2023-05-01','')''')
    cur.execute('''INSERT INTO tb_plano(codigo,descricao,nivel,valor,status,dt_cadastro,aluno_matricula) VALUES(1008,'Dança','Intermediario', 300, 'Ativo','2023-05-01','')''')
    cur.execute('''INSERT INTO tb_plano(codigo,descricao,nivel,valor,status,dt_cadastro,aluno_matricula) VALUES(1009,'Dança','Avançado', 400, 'Ativo','2023-05-01','')''')
    cur.execute('''INSERT INTO tb_plano(codigo,descricao,nivel,valor,status,dt_cadastro,aluno_matricula) VALUES(1010,'Cross Fit','Basico', 500, 'Ativo','2023-05-01','')''')
    con.commit()
print("Tabela de Planos populada com sucesso!")

# ----------------------  POPULA TABELA ENDEREÇOS ------------------------------
with con:
    cur.execute('''INSERT INTO tb_endereco(rua, numero, complemento, cep, bairro, cidade, estado,aluno_matricula,funcionario_matricula) VALUES('Rua das Couves',33,'Qd 04','78042-804','São José','Cuiabá','MT','','')''')
    cur.execute('''INSERT INTO tb_endereco(rua, numero, complemento, cep, bairro, cidade, estado,aluno_matricula,funcionario_matricula) VALUES('Rua das Abobrinhas',43,'Qd 33','78045-804','Verdão','Cuiabá','MT','','')''')
    cur.execute('''INSERT INTO tb_endereco(rua, numero, complemento, cep, bairro, cidade, estado,aluno_matricula,funcionario_matricula) VALUES('Rua das Margaridas',63,'Qd 28','78047-804','Dom Aquino','Cuiabá','MT','','')''')
    cur.execute('''INSERT INTO tb_endereco(rua, numero, complemento, cep, bairro, cidade, estado,aluno_matricula,funcionario_matricula) VALUES('Rua da Roseira',38,'Qd 84','78042-806','São José','Cuiabá','MT','','')''')
    cur.execute('''INSERT INTO tb_endereco(rua, numero, complemento, cep, bairro, cidade, estado,aluno_matricula,funcionario_matricula) VALUES('Rua dos Ipês',30,'Qd 03','78042-809','Santa Rosa','Cuiabá','MT','','')''')
    cur.execute('''INSERT INTO tb_endereco(rua, numero, complemento, cep, bairro, cidade, estado,aluno_matricula,funcionario_matricula) VALUES('Rua Aroeira',333,'Qd 06','78041-804','Lixeira','Cuiabá','MT','','')''')
    cur.execute('''INSERT INTO tb_endereco(rua, numero, complemento, cep, bairro, cidade, estado,aluno_matricula,funcionario_matricula) VALUES('Rua Flamboiam',42,'Qd 01','78045-904','São José','Cuiabá','MT','','')''')
    cur.execute('''INSERT INTO tb_endereco(rua, numero, complemento, cep, bairro, cidade, estado,aluno_matricula,funcionario_matricula) VALUES('Avenida Miguel Sutil ',1334,'','78048-808','Goiabeiras','Cuiabá','MT','','')''')
    cur.execute('''INSERT INTO tb_endereco(rua, numero, complemento, cep, bairro, cidade, estado,aluno_matricula,funcionario_matricula) VALUES('Avenida do CPA',2033,' ','78040-800','Centro Sul','Cuiabá','MT','','')''')
    cur.execute('''INSERT INTO tb_endereco(rua, numero, complemento, cep, bairro, cidade, estado,aluno_matricula,funcionario_matricula) VALUES('Avenida Getulio Vargas',5001,' ','78042-804','Centro Norte','Cuiabá','MT','','')''')
    con.commit()
print("Tabela de Endereços populada com sucesso!")

# ----------------------  FECHA BANCO E CONEXÃO ------------------------------
cur.close()  # FECHA O OBJETO
con.close()  # FECHA A CONEXÃO
