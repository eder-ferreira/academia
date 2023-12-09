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
    'matricula'	INTEGER NOT NULL UNIQUE,
    'nome' TEXT,
    'tipo_documento' TEXT,
    'num_documento' VARCHAR(10) NOT NULL UNIQUE,
    'telefone' VARCHAR(12),
    'genero' VARCHAR(1),
    'status' TEXT,
    'dt_cadastro' DATE,
    'dt_nascimento' DATE,
    'usuario_id' INTEGER,
     FOREIGN KEY("usuario_id") REFERENCES "tb_usuario"("id"))
    ''')

    cur.execute('''CREATE TABLE IF NOT EXISTS 'tb_usuario'(
    'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'usuario' VARCHAR(15) NOT NULL,
    'senha' VARCHAR(10) NOT NULL,
    'nome' VARCHAR(15) NOT NULL,
    'email' VARCHAR(15) NOT NULL,
    'tipo_documento' TEXT,
    'num_documento' VARCHAR(10) UNIQUE,
    'status' TEXT,
    'dt_nascimento' DATE,
    'dt_cadastro' DATE)
    ''')

    cur.execute('''CREATE TABLE IF NOT EXISTS 'tb_funcionario'(
    'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'nome' TEXT,
    'tipo_documento' TEXT,
    'num_documento' VARCHAR(10) UNIQUE,
    'telefone' VARCHAR(12),
    'email' VARCHAR(15),
    'dt_nascimento' DATE,
    'genero' VARCHAR(1),
    'matricula'	INTEGER,
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
    'codigo' INTEGER NOT NULL UNIQUE,
    'nome' TEXT,
    'setor' TEXT,
    'salario_base' FLOAT,
    'dt_cadastro' DATE)
    ''')

    cur.execute('''CREATE TABLE IF NOT EXISTS 'tb_plano'(
    'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'codigo' INTEGER NOT NULL UNIQUE,
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
    cur.execute('''INSERT INTO tb_usuario(usuario, senha, nome, email, tipo_documento, num_documento, status, dt_nascimento, dt_cadastro)VALUES('admrural','adm123','Eder Ferreira','admrural@gmail.com','RG',001036771,'Ativo','1979-09-25','2023-11-01')''')
    cur.execute('''INSERT INTO tb_usuario(usuario, senha, nome, email, tipo_documento, num_documento, status, dt_nascimento,  dt_cadastro)VALUES('loren','loren','Loren Pires','loren@loren.com','Inativo','CPF',00134123456,'2007-01-24','2022-11-01')''')
    cur.execute('''INSERT INTO tb_usuario(usuario, senha, nome, email, tipo_documento, num_documento, status, dt_nascimento,  dt_cadastro)VALUES('jleonel','admin','João Leonel Ferreira','jleonel@gmail.com','CPF',00134123457,'Ativo','1980-04-02','2023-10-01')''')
    cur.execute('''INSERT INTO tb_usuario(usuario, senha, nome, email, tipo_documento, num_documento, status, dt_nascimento,  dt_cadastro)VALUES('luisinha','anapires','Ana Luisa Pires','ana.luisa@ana.com','RG',001036556,'Ativo','1987-04-04','2023-09-01')''')
    cur.execute('''INSERT INTO tb_usuario(usuario, senha, nome, email, tipo_documento, num_documento, status, dt_nascimento,  dt_cadastro)VALUES('luvpof','lu123','Luciana Ferreira','lu@gmail.com','CPF',00103655632,'1979-09-25','Ativo','2000-02-01')''')
    cur.execute('''INSERT INTO tb_usuario(usuario, senha, nome, email, tipo_documento, num_documento, status, dt_nascimento,  dt_cadastro)VALUES('aurora','au3355','Maria Aurora da Silva','aurora@aurora.com','CPF',00134123459,'Ativo','2002-03-17','2023-03-01')''')
    cur.execute('''INSERT INTO tb_usuario(usuario, senha, nome, email, tipo_documento, num_documento, status, dt_nascimento,  dt_cadastro)VALUES('alice2005','al2023','Alice Ortega','ortega@alice.com','Ativo','RG',001022987,'1988-01-20','2023-01-01')''')
    cur.execute('''INSERT INTO tb_usuario(usuario, senha, nome, email, tipo_documento, num_documento, status, dt_nascimento,  dt_cadastro)VALUES('toniamachado','272ton','Antonia Machado','tonia@gmail.com','CPF',00134123460,'Inativo','2001-12-05','2023-02-01')''')
    cur.execute('''INSERT INTO tb_usuario(usuario, senha, nome, email, tipo_documento, num_documento, status, dt_nascimento,  dt_cadastro)VALUES('caco79','carlos1979','Carlos Augusto Moraes','caco@caco.com','CPF',00134123561,'Ativo','2003-06-06','2023-05-01')''')
    cur.execute('''INSERT INTO tb_usuario(usuario, senha, nome, email, tipo_documento, num_documento, status, dt_nascimento,  dt_cadastro)VALUES('arimateia','ari68','José de Arimateia','arimateia@gmail.com','Passaport',33097512,'Ativo','1978-12-25','2023-08-01')''')
    con.commit()
print("Tabela de Usuarios populada com sucesso!")



# ----------------------  POPULA TABELA FUNCIONARIO ------------------------------
with con:
    cur.execute('''INSERT INTO tb_funcionario(nome, tipo_documento, num_documento, telefone, email, dt_nascimento, genero, matricula, status, dt_contratacao,dt_desligamento,cargo_id, usuario_id, dt_cadastro)VALUES('João Santos','CPF',00134577700,'6799996-1792','jsantos@email.com','2000-12-01','M','0158433','Ativo','2023-05-01','',111,'','2023-12-05')''')
    cur.execute('''INSERT INTO tb_funcionario(nome, tipo_documento, num_documento, telefone, email, dt_nascimento, genero, matricula, status, dt_contratacao,dt_desligamento,cargo_id, usuario_id, dt_cadastro)VALUES('Arnaldo Fleuri','CPF',01832227700,'6599996-0003','afleuri@email.com','2001-05-13','M','0338444','Ativo','2023-05-01','',222,'','2023-12-05')''')
    cur.execute('''INSERT INTO tb_funcionario(nome, tipo_documento, num_documento, telefone, email, dt_nascimento, genero, matricula, status, dt_contratacao,dt_desligamento,cargo_id, usuario_id, dt_cadastro)VALUES('Carlos da Costa','CPF',02554576700,'6999996-0292','ccarlos@email.com','1987-12-01','M','0258925','Ativo','2023-05-01','',333,'','2023-12-05')''')
    cur.execute('''INSERT INTO tb_funcionario(nome, tipo_documento, num_documento, telefone, email, dt_nascimento, genero, matricula, status, dt_contratacao,dt_desligamento,cargo_id, usuario_id, dt_cadastro)VALUES('João Leonel Ferreira','CPF',09234587601,'3199996-1802','jleonel@email.com','2005-08-10','M','0254466','Ativo','2023-05-01','',444,'','2023-12-05')''')
    cur.execute('''INSERT INTO tb_funcionario(nome, tipo_documento, num_documento, telefone, email, dt_nascimento, genero, matricula, status, dt_contratacao,dt_desligamento,cargo_id, usuario_id, dt_cadastro)VALUES('Bruno Guimarães','CPF',03834533321,'6699996-1796','bguima@email.com','1991-05-10','M','0238477','Desligado','2015-05-01','2023-09-01',555,'','2023-12-05')''')
    cur.execute('''INSERT INTO tb_funcionario(nome, tipo_documento, num_documento, telefone, email, dt_nascimento, genero, matricula, status, dt_contratacao,dt_desligamento,cargo_id, usuario_id, dt_cadastro)VALUES('Loren Pires','CPF',00134177700,'2199996-1792','lpires@email.com','2004-06-23','F','0248488','Ativo','2023-05-01','',666,'','2023-12-05')''')
    cur.execute('''INSERT INTO tb_funcionario(nome, tipo_documento, num_documento, telefone, email, dt_nascimento, genero, matricula, status, dt_contratacao,dt_desligamento,cargo_id, usuario_id, dt_cadastro)VALUES('Ana Luisa Oliveira','CPF',09123347700,'6799996-4492','aluisa@email.com','2001-11-18','F','0256499','Ativo','2023-05-01','',777,'','2023-12-05')''')
    cur.execute('''INSERT INTO tb_funcionario(nome, tipo_documento, num_documento, telefone, email, dt_nascimento, genero, matricula, status, dt_contratacao,dt_desligamento,cargo_id, usuario_id, dt_cadastro)VALUES('Luciana Ferreira','CPF',09456575500,'1199996-1234','lferreira@email.com','2002-05-01','F','0338422','Ativo','2023-05-01','',111,'','2023-12-05')''')
    cur.execute('''INSERT INTO tb_funcionario(nome, tipo_documento, num_documento, telefone, email, dt_nascimento, genero, matricula, status, dt_contratacao,dt_desligamento,cargo_id, usuario_id, dt_cadastro)VALUES('Herminia Assunção','CPF',09830322200,'1699996-4321','hassuncao@email.com','1995-12-01','F','0282411','Ativo','2023-05-01','',999,'','2023-12-05')''')
    cur.execute('''INSERT INTO tb_funcionario(nome, tipo_documento, num_documento, telefone, email, dt_nascimento, genero, matricula, status, dt_contratacao,dt_desligamento,cargo_id, usuario_id, dt_cadastro)VALUES('Marina de Paula Fonseca','CPF',04834597910,'6799996-1717','mpaula@email.com','1980-11-22','F','0118400','Aposentada','1999-05-01','2023-08-01',999,'','2023-12-05')''')
    cur.execute('''INSERT INTO tb_funcionario(nome, tipo_documento, num_documento, telefone, email, dt_nascimento, genero, matricula, status, dt_contratacao,dt_desligamento,cargo_id, usuario_id, dt_cadastro)VALUES('João Pereira da Silva','CPF',00134522201,'6799996-1792','jpereira@email.com','1978-12-25','M','0122201','Ativo','2023-05-01','',111,'','2023-12-05')''')
    cur.execute('''INSERT INTO tb_funcionario(nome, tipo_documento, num_documento, telefone, email, dt_nascimento, genero, matricula, status, dt_contratacao,dt_desligamento,cargo_id, usuario_id, dt_cadastro)VALUES('Arthur Fidelis','CPF',01832115507,'6899996-0004','afidelis@email.com','1994-12-17','M','0158403','Ativo','2023-05-01','',222,'','2023-12-05')''')
    cur.execute('''INSERT INTO tb_funcionario(nome, tipo_documento, num_documento, telefone, email, dt_nascimento, genero, matricula, status, dt_contratacao,dt_desligamento,cargo_id, usuario_id, dt_cadastro)VALUES('Roberto Carlos Guimarães','CPF',09527533400,'6999996-0295','rcarlos@email.com','2023-05-01','M','0158163','Ativo','2023-05-01','',333,'','2023-12-05')''')
    cur.execute('''INSERT INTO tb_funcionario(nome, tipo_documento, num_documento, telefone, email, dt_nascimento, genero, matricula, status, dt_contratacao,dt_desligamento,cargo_id, usuario_id, dt_cadastro)VALUES('João Leonardo Paim','CPF',00834587605,'7088996-1502','jleonardo@email.com','1989-12-09','M','0218304','Ativo','2023-05-01','',444,'','2023-12-05')''')
    cur.execute('''INSERT INTO tb_funcionario(nome, tipo_documento, num_documento, telefone, email, dt_nascimento, genero, matricula, status, dt_contratacao,dt_desligamento,cargo_id, usuario_id, dt_cadastro)VALUES('Marcos Silva Guimarães','CPF',22834522005,'7199997-1699','msilva@email.com','2000-12-12','M','0234405','Desligado','2015-05-01','2023-09-01',555,'','2023-12-05')''')
    cur.execute('''INSERT INTO tb_funcionario(nome, tipo_documento, num_documento, telefone, email, dt_nascimento, genero, matricula, status, dt_contratacao,dt_desligamento,cargo_id, usuario_id, dt_cadastro)VALUES('Lorena Calabria de Jesus','CPF',00134501752,'2177996-3393','loca@email.com','2003-07-07','F','0348406','Ativo','2023-05-01','',666,'','2023-12-05')''')
    cur.execute('''INSERT INTO tb_funcionario(nome, tipo_documento, num_documento, telefone, email, dt_nascimento, genero, matricula, status, dt_contratacao,dt_desligamento,cargo_id, usuario_id, dt_cadastro)VALUES('Analu Maldini','CPF',10123532700,'6299396-2299','anamaldini@email.com','1996-03-28','F','0155207','Ativo','2023-05-01','',777,'','2023-12-05')''')
    cur.execute('''INSERT INTO tb_funcionario(nome, tipo_documento, num_documento, telefone, email, dt_nascimento, genero, matricula, status, dt_contratacao,dt_desligamento,cargo_id, usuario_id, dt_cadastro)VALUES('Lucia Veronica Salazar','CPF',03456572330,'1188996-4321','lver@email.com','2004-09-25','F','0290208','Ativo','2023-05-01','',111,'','2023-12-05')''')
    cur.execute('''INSERT INTO tb_funcionario(nome, tipo_documento, num_documento, telefone, email, dt_nascimento, genero, matricula, status, dt_contratacao,dt_desligamento,cargo_id, usuario_id, dt_cadastro)VALUES('Herminia Esteves','CPF',06530327200,'1699666-1234','hesteves@email.com','2000-04-20','F','0250909','Ativo','2023-05-01','',999,'','2023-12-05')''')
    cur.execute('''INSERT INTO tb_funcionario(nome, tipo_documento, num_documento, telefone, email, dt_nascimento, genero, matricula, status, dt_contratacao,dt_desligamento,cargo_id, usuario_id, dt_cadastro)VALUES('Marta Maria da Conceição','CPF',00004564930,'6795996-2030','mmaria@email.com','1997-12-23','F','0148510','Aposentada','1999-05-01','2023-08-01',999,'','2023-12-05')''')
    con.commit()
print("Tabela de Funcionario populada com sucesso!")

# ----------------------  POPULA TABELA ALUNOS ------------------------------
with con:
    cur.execute('''INSERT INTO tb_aluno(matricula, nome, tipo_documento, num_documento, telefone, genero, status, dt_cadastro, dt_nascimento, usuario_id)VALUES(0269533,'João da Silva','CPF',09834555700,'6799996-1792','M','Ativo','2019-05-01','1980-05-23','')''')
    cur.execute('''INSERT INTO tb_aluno(matricula, nome, tipo_documento, num_documento, telefone, genero, status, dt_cadastro, dt_nascimento, usuario_id)VALUES(0269544,'José Francisco do Carmo','CPF',09834577722,'6899996-1722','M','Ativo','2023-12-01','1985-12-14','')''')
    cur.execute('''INSERT INTO tb_aluno(matricula, nome, tipo_documento, num_documento, telefone, genero, status, dt_cadastro, dt_nascimento, usuario_id)VALUES(0269555,'Maria José Costa','CPF',09834574400,'6999996-1800','F','Ativo','2023-03-01','1990-05-13','')''')
    cur.execute('''INSERT INTO tb_aluno(matricula, nome, tipo_documento, num_documento, telefone, genero, status, dt_cadastro, dt_nascimento, usuario_id)VALUES(0269566,'Artemio Machado','CPF',09204577700,'1199996-1733','M','Ativo','2023-05-01','1988-12-11','')''')
    cur.execute('''INSERT INTO tb_aluno(matricula, nome, tipo_documento, num_documento, telefone, genero, status, dt_cadastro, dt_nascimento, usuario_id)VALUES(0269577,'Leonel de Paula','CPF',09834577711,'6699996-1392','M','Ativo','2022-02-01','1997-01-23','')''')
    cur.execute('''INSERT INTO tb_aluno(matricula, nome, tipo_documento, num_documento, telefone, genero, status, dt_cadastro, dt_nascimento, usuario_id)VALUES(0269588,'Luiza de Souza','CPF',09834579900,'6599996-1295','F','Ativo','2020-06-01','2001-05-03','')''')
    cur.execute('''INSERT INTO tb_aluno(matricula, nome, tipo_documento, num_documento, telefone, genero, status, dt_cadastro, dt_nascimento, usuario_id)VALUES(0269599,'Loren Pires','CPF',09835577700,'2199996-1891','M','Ativo','2023-05-01','2005-08-23','')''')
    cur.execute('''INSERT INTO tb_aluno(matricula, nome, tipo_documento, num_documento, telefone, genero, status, dt_cadastro, dt_nascimento, usuario_id)VALUES(0269500,'Ana Maria Ferreira','CPF',09832177700,'4499996-1202','F','Ativo','2082-05-01','2000-07-18','')''')
    cur.execute('''INSERT INTO tb_aluno(matricula, nome, tipo_documento, num_documento, telefone, genero, status, dt_cadastro, dt_nascimento, usuario_id)VALUES(0269511,'Amora Oliveira','CPF',09834566600,'6299996-1112','F','Ativo','2023-05-01','1986-12-23','')''')
    cur.execute('''INSERT INTO tb_aluno(matricula, nome, tipo_documento, num_documento, telefone, genero, status, dt_cadastro, dt_nascimento, usuario_id)VALUES(0269522,'Francisca Matos Freitas','CPF',09094577700,'6799996-0093','F','Ativo','1999-07-01','1999-07-07','')''')
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
    cur.execute('''INSERT INTO tb_cargo(codigo,nome,setor,salario_base,dt_cadastro) VALUES(102,'Professor', 'Operacional',6000,'2023-05-01')''')
    cur.execute('''INSERT INTO tb_cargo(codigo,nome,setor,salario_base,dt_cadastro) VALUES(103,'Secretaria', 'Administrativo',2000,'2023-05-01')''')
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
