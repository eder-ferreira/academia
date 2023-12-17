
tam = 20
tam2 = 8
opcoes = {
    "1": "Cadastrar",
    "2": "Listar",
    "3": "Pesquisar",
    "4": "Atualizar",
    "5": "Excluir",
    "6": "Relatorio",
    "0": "Sair",
}

while True:
    print(f"+{'-' * tam}+")
    print(f"|{'MENU':{tam}}|")
    print(f"+{'-' * tam}+")
    for k, v in opcoes.items():
        print(f"|{f' {k} - {v}':{tam}}|")
    print(f"+{'-' * tam}+")

    op = input()

    if op not in opcoes:
        print("Opção Inválida!")
        continue

    if op == "0":
        break
    print(f"{opcoes.get(op)}\n")
