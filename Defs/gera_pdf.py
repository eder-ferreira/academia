from prettytable import PrettyTable
from reportlab.pdfgen import canvas
import sqlite3

database = "Defs/academia.db"
con = sqlite3.connect(database, timeout=10)
cur = con.cursor()


def gerar_pdf():
    # Pegando os dados do banco de dados:
    comando_SQl = (
        "SELECT id, matricula, nome,status,dt_cadastro, dt_nascimento FROM tb_aluno"
    )
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
    pdf = canvas.Canvas("PDF_tb_alunos.pdf")
    pdf.setFont("Times-Bold", 15)
    pdf.drawString(150, 805, "Relatório de alunos matriculados:")
    pdf.setFont("Times-Bold", 10)

    pdf.drawString(40, 780, "Id")
    pdf.drawString(60, 780, "Matrícula")
    pdf.drawString(110, 780, "Nome")
    pdf.drawString(250, 780, "Status")
    pdf.drawString(330, 780, "Data cadastro")
    pdf.drawString(410, 780, "Data aniversario")

    # Lendo os dados em PDF
    for i in range(0, len(dados_lidos)):
        y = y + 20
        pdf.drawString(40, 780 - y, str(dados_lidos[i][0]))
        pdf.drawString(60, 780 - y, str(dados_lidos[i][1]))
        pdf.drawString(110, 780 - y, str(dados_lidos[i][2]))
        pdf.drawString(250, 780 - y, str(dados_lidos[i][3]))
        pdf.drawString(340, 780 - y, str(dados_lidos[i][4]))
        pdf.drawString(420, 780 - y, str(dados_lidos[i][5]))

    pdf.showPage()
    pdf.save()
    print("PDF gerado com sucesso!")


# -------------------------------------------------------------

# # Definindo a posição inicial das linhas horizontais
# y_start = 780
# y_end = 780 - (len(dados_lidos) + 1) * 20
#
# # Desenhando linhas horizontais
# for y in range(y_start, y_end, -20):
#     pdf.line(col_widths[0], y, col_widths[-1], y)
#
# # Desenhando linhas verticais
# for x in col_widths:
#     pdf.line(x, y_start, x, y_end)
