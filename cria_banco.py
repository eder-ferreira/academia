# ----------------------  CRIA BANCO ---------------------------------------
import sqlite3
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
     FOREIGN KEY("matricula") REFERENCES "tb_usuario"("id"))
    ''')

    cur.execute('''CREATE TABLE IF NOT EXISTS 'tb_usuario'(
    'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'matricula'	INTEGER NOT NULL UNIQUE,
    'usuario' VARCHAR(15),
    'senha' VARCHAR(10),
    'nome' VARCHAR(15),
    'email' VARCHAR(15),
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
    'dt_cadastro' DATE,
    FOREIGN KEY("cargo_id") REFERENCES "tb_cargo"("codigo"),
    FOREIGN KEY("matricula") REFERENCES "tb_usuario"("matricula")
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
    FOREIGN KEY("codigo") REFERENCES "tb_aluno"("matricula"))
    ''')

    cur.execute('''CREATE TABLE IF NOT EXISTS 'tb_endereco'(
    'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'matricula'	INTEGER,
    'nome' TEXT,
    'rua' TEXT,
    'numero' VARCHAR(10),
    'complemento' TEXT,
    'cep' VARCHAR(8),
    'bairro' TEXT,
    'cidade' TEXT,
    'estado' TEXT,
    FOREIGN KEY("matricula") REFERENCES "tb_aluno"("matricula"),
    FOREIGN KEY("matricula") REFERENCES "tb_funcionario"("matricula")
    )''')

    con.commit()
print('Tabelas Aluno - Usuario - Funcionario - Cargo - Plano - Endereço criadas!!!')

# ----------------------  FECHA BANCO E CONEXÃO ------------------------------
cur.close()  # FECHA O OBJETO
con.close()  # FECHA A CONEXÃO
