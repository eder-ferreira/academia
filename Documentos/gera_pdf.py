from prettytable import PrettyTable
from reportlab.pdfgen import canvas
import sqlite3
database = 'academia.db'
con = sqlite3.connect(database, timeout=10)
cur = con.cursor()

def alunos_matriculados_mes():
    global tabela
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

def gerar_pdf():
    # Pegando os dados do banco de dados:
    comando_SQl = "SELECT id, matricula, nome,status,dt_cadastro FROM tb_aluno"
    cur.execute(comando_SQl)
    dados_lidos = cur.fetchall()

    tabela = PrettyTable()
    tabela.field_names = [desc[0] for desc in cur.description]
    for row in dados_lidos:
        tabela.add_row(row)
    print(tabela)

    # Pegando os dados na posição 0
    y = 0

    # Defindo o nome do arquivo e tamanho da fonte
    pdf = canvas.Canvas("tabelas_alunos.pdf")
    pdf.setFont("Times-Bold", 15)
    pdf.drawString(150, 805, "Monitoramento dos alunos matriculados:")
    pdf.setFont("Times-Bold", 10)

    pdf.drawString(50, 780, "Matrícula")
    pdf.drawString(110, 780, "Nome")
    pdf.drawString(250, 780, "Status")
    pdf.drawString(330, 780, "Data cadastro")
    # pdf.drawString(400, 780, "Data cadastro")

    # Lendo os dados em PDF
    for i in range(0, len(dados_lidos)):
        y = y + 20
        pdf.drawString(50, 780 - y, str(dados_lidos[i][1]))
        pdf.drawString(110, 780 - y, str(dados_lidos[i][2]))
        pdf.drawString(250, 780 - y, str(dados_lidos[i][3]))
        pdf.drawString(330, 780 - y, str(dados_lidos[i][4]))

        pdf.showPage()
    pdf.save()
    print("PDF gerado com sucesso!")

gerar_pdf()