import sys
from datetime import date
from Defs.cadastrar import cadastrar_aluno
from Defs.cadastrar import cadastrar_usuario
from Defs.cadastrar import cadastrar_funcionario
from Defs.cadastrar import cadastrar_cargo
from Defs.cadastrar import cadastrar_plano
from Defs.validar_login import autentica_login
from Defs.validaCampoVazio import validar_opcao_login
from Log.log import registrar_atividade
from Defs.gera_pdf import gerar_pdf

data = date.today()
dia = data.day
mes = data.month
ano = data.year

menu = [
    "\033[0;34m>>>>>>>> MENU OPÇÕES <<<<<<<<\n\033[0;0m"
    "[\033[0;34m 1 \033[0;0m] - Cadastrar\n"
    "[\033[0;34m 2 \033[0;0m] - Listar\n"
    "[\033[0;34m 3 \033[0;0m] - Pesquisar\n"
    "[\033[0;34m 4 \033[0;0m] - Atualizar\n"
    "[\033[0;34m 5 \033[0;0m] - Excluir\n"
    "[\033[0;34m 6 \033[0;0m] - Relatorio\n"
    "[\033[0;34m 0 \033[0;0m] - Sair"
]
registrar_atividade("usuario acessou o sistema")


def tela_login():
    print(
        " "
        f"\n\033[0;34m>>>>>>>>= Data: {data} =<<<<<\033[0;0m"
        "\n\033[0;34m>>>>>>>>= TELA DE LOGIN =<<<<<<<<\033[0;0m",
        "\n[\033[0;34m 0 \033[0;0m] - Sair"
        "\n[\033[0;34m 1 \033[0;0m] - Logar"
        "\n[\033[0;34m 2 \033[0;0m] - Cadastrar Novo Usuario",
    )


registrar_atividade("usuario acessou tela de login")


def main():
    while True:
        tela_login()
        opcao = input("\033[0;34mInsira a opção=> \033[0m")
        validar_opcao_login(opcao)
        if opcao == "0":
            print("-" * 30)
            print("\033[0;31m      Sistema Encerrado!\033[0;0m")
            print("-" * 30)
            sys.exit()

        elif opcao == "2":
            cadastrar_usuario()

        elif opcao == "1":
            registrar_atividade("usuario acessou o login!")
            print("\n\033[0;34m>>>>>>>> MENU LOGAR <<<<<<<<\033[0;0m")
            login = input("Digite seu login=> ")
            senha = input("Digite sua senha=> ")
            if autentica_login(login, senha):
                print("=" * 36)
                print("\033[0;34mLogin bem-sucedido!\033[0m")
                print("-" * 36)
                print(f" Data: {data}")
                print(f" Olá, seja bem vindo(a): {login}!")
                print("-" * 36)
                registrar_atividade("usuario efetuou login")
                while True:
                    for opcao in menu:
                        print(opcao)
                    opcao = input("\033[0;34mInsira a opção desejada =>\033[0;0m ")
                    print("=" * 30)

                    if opcao == "0":
                        registrar_atividade("usuario saiu do sistema!")
                        print("\033[0;31mFinalizando programa....\033[0;0m")
                        print("-" * 30)
                        break

                    # CADASTRAR
                    elif opcao == "1":
                        while True:
                            submenuCadastrar = input(
                                "\033[0;34m>>>>>>>> MENU CADASTRAR <<<<<<<<\n\033[0;0m"
                                "[\033[0;34m 1 \033[0;0m] - Aluno\n"
                                "[\033[0;34m 2 \033[0;0m] - Usuario\n"
                                "[\033[0;34m 3 \033[0;0m] - Funcionario\n"
                                "[\033[0;34m 4 \033[0;0m] - Cargos\n"
                                "[\033[0;34m 5 \033[0;0m] - Planos\n"
                                "[\033[0;34m 6 \033[0;0m] - Endereços\n"
                                "[\033[0;34m 0 \033[0;0m] - Voltar ao menu\n"
                                "\033[0;34mInsira a opção desejada =>\033[0;0m "
                            )
                            registrar_atividade("usuario acessou menu de cadastro!")
                            if submenuCadastrar == "0":
                                print("-" * 30)
                                break

                            elif submenuCadastrar == "1":
                                registrar_atividade(
                                    "usuario acessou menu de cadastrar aluno!"
                                )
                                cadastrar_aluno()

                            elif submenuCadastrar == "2":
                                registrar_atividade(
                                    "usuario acessou menu de cadastrar usuario!"
                                )
                                cadastrar_usuario()

                            elif submenuCadastrar == "3":
                                registrar_atividade(
                                    "usuario acessou menu de cadastrar funcionario!"
                                )
                                cadastrar_funcionario()

                            elif submenuCadastrar == "4":
                                registrar_atividade(
                                    "usuario acessou menu de cadastrar cargo!"
                                )
                                cadastrar_cargo()

                            elif submenuCadastrar == "5":
                                registrar_atividade(
                                    "usuario acessou menu de cadastrar plano!"
                                )
                                cadastrar_plano()

                            elif submenuCadastrar == "6":
                                registrar_atividade(
                                    "usuario acessou menu de cadastrar endereço!"
                                )
                                from Defs.listar import listar_endereco

                                listar_endereco()
                                from Defs.atualizar import atualiza_end_completo

                                atualiza_end_completo()
                            else:
                                print(
                                    "\033[1;31mOpção Inválida!\nDigite um opção de [0 a 6]\n\033[0;0m"
                                )
                                registrar_atividade(
                                    "usuario digitou Opção Inválida! Digite um opção de [0 a 6]!"
                                )

                    # LISTAR
                    elif opcao == "2":
                        while True:
                            submenuListar = input(
                                "\033[0;34m>>>>>>>> MENU LISTAR <<<<<<<<\n\033[0;0m"
                                "[\033[0;34m  7 \033[0;0m] - Aluno\n"
                                "[\033[0;34m  8 \033[0;0m] - Usuario\n"
                                "[\033[0;34m  9 \033[0;0m] - Funcionario\n"
                                "[\033[0;34m 10 \033[0;0m] - Cargos\n"
                                "[\033[0;34m 11 \033[0;0m] - Planos\n"
                                "[\033[0;34m 12 \033[0;0m] - Endereços\n"
                                "[\033[0;34m  0 \033[0;0m] - Voltar ao menu\n"
                                "\033[0;34mInsira a opção desejada =>\033[0;0m "
                            )
                            registrar_atividade("usuario acessou menu de listar")

                            if submenuListar == "0":
                                print("-" * 30)
                                break

                            elif submenuListar == "7":
                                registrar_atividade(
                                    "usuario acessou menu de listar aluno"
                                )
                                from Defs.listar import listar_aluno

                                listar_aluno()

                            elif submenuListar == "8":
                                registrar_atividade(
                                    "usuario acessou menu de listar usuario"
                                )
                                from Defs.listar import listar_usuario

                                listar_usuario()

                            elif submenuListar == "9":
                                registrar_atividade(
                                    "usuario acessou menu de listar funcionario"
                                )
                                from Defs.listar import listar_funcionario

                                listar_funcionario()

                            elif submenuListar == "10":
                                registrar_atividade(
                                    "usuario acessou menu de listar cargo"
                                )
                                from Defs.listar import listar_cargo

                                listar_cargo()

                            elif submenuListar == "11":
                                registrar_atividade(
                                    "usuario acessou menu de listar plano"
                                )
                                from Defs.listar import listar_plano

                                listar_plano()

                            elif submenuListar == "12":
                                registrar_atividade(
                                    "usuario acessou menu de listar endereço"
                                )
                                from Defs.listar import listar_endereco

                                listar_endereco()
                            else:
                                print(
                                    "\033[1;31mOpção Inválida!\nDigite um opção de [0 ou 7 a 12]\n\033[0;0m"
                                )
                                registrar_atividade(
                                    "usuario digitou opção inválida no menu de atualizar!"
                                )

                    # BUSCAR
                    elif opcao == "3":
                        while True:
                            submenuBuscar = input(
                                "\033[0;34m>>>>>>>> MENU PESQUISAR <<<<<<<<\n\033[0;0m"
                                "[\033[0;34m 13 \033[0;0m] - Aluno\n"
                                "[\033[0;34m 14 \033[0;0m] - Usuario\n"
                                "[\033[0;34m 15 \033[0;0m] - Funcionario\n"
                                "[\033[0;34m 16 \033[0;0m] - Cargos\n"
                                "[\033[0;34m 17 \033[0;0m] - Planos\n"
                                "[\033[0;34m 18 \033[0;0m] - Endereços\n"
                                "[\033[0;34m  0 \033[0;0m] - Voltar ao menu\n"
                                "\033[0;34mInsira a opção desejada =>\033[0;0m "
                            )
                            registrar_atividade("usuario acessou menu de pesquisar")

                            if submenuBuscar == "0":
                                print("-" * 30)
                                break

                            elif submenuBuscar == "13":
                                registrar_atividade(
                                    "usuario acessou menu de pesquisar aluno"
                                )
                                from Defs.buscar import buscar_aluno

                                buscar_aluno()

                            elif submenuBuscar == "14":
                                registrar_atividade(
                                    "usuario acessou menu de pesquisar usuario"
                                )
                                from Defs.buscar import buscar_usuario

                                buscar_usuario()

                            elif submenuBuscar == "15":
                                registrar_atividade(
                                    "usuario acessou menu de pesquisar funcionario"
                                )
                                from Defs.buscar import buscar_funcionario

                                buscar_funcionario()

                            elif submenuBuscar == "16":
                                registrar_atividade(
                                    "usuario acessou menu de pesquisar cargo"
                                )
                                from Defs.buscar import buscar_cargo

                                buscar_cargo()

                            elif submenuBuscar == "17":
                                registrar_atividade(
                                    "usuario acessou menu de pesquisar plano"
                                )
                                from Defs.buscar import buscar_plano

                                buscar_plano()

                            elif submenuBuscar == "18":
                                registrar_atividade(
                                    "usuario acessou menu de pesquisar endereço"
                                )
                                from Defs.buscar import buscar_endereco

                                buscar_endereco()
                            else:
                                print(
                                    "\033[1;31mOpção Inválida!\nDigite um opção de [0 ou 13 a 18]\n\033[0;0m"
                                )
                                registrar_atividade(
                                    "usuario digitou opção inválida no menu de pesquisar!"
                                )

                    # ATUALIZAR
                    elif opcao == "4":
                        while True:
                            submenuAtualiza = input(
                                "\033[0;34m>>>>>>>> MENU ATUALIZAR <<<<<<<<\n\033[0;0m"
                                "[\033[0;34m 19 \033[0;0m] - Aluno\n"
                                "[\033[0;34m 20 \033[0;0m] - Usuario\n"
                                "[\033[0;34m 21 \033[0;0m] - Funcionario\n"
                                "[\033[0;34m 22 \033[0;0m] - Cargos\n"
                                "[\033[0;34m 23 \033[0;0m] - Planos\n"
                                "[\033[0;34m 24 \033[0;0m] - Endereços\n"
                                "[\033[0;34m  0 \033[0;0m] - Voltar ao menu\n"
                                "\033[0;34mInsira a opção desejada =>\033[0;0m "
                            )
                            registrar_atividade("usuario acessou menu de atualizar")
                            if submenuAtualiza == "0":
                                print("-" * 30)
                                break

                            elif submenuAtualiza == "19":
                                registrar_atividade(
                                    "usuario acessou menu de atualizar aluno"
                                )
                                from Defs.listar import listar_aluno

                                listar_aluno()
                                from Defs.atualizar import atualiza_aluno

                                atualiza_aluno()
                                from Defs.listar import listar_aluno

                                listar_aluno()

                            elif submenuAtualiza == "20":
                                registrar_atividade(
                                    "usuario acessou menu de atualiza usuario"
                                )
                                from Defs.listar import listar_usuario

                                listar_usuario()
                                from Defs.atualizar import atualiza_usuario

                                atualiza_usuario()
                                from Defs.listar import listar_usuario

                                listar_usuario()

                            elif submenuAtualiza == "21":
                                registrar_atividade(
                                    "usuario acessou menu de atualizar funcionario"
                                )
                                from Defs.listar import listar_funcionario

                                listar_funcionario()
                                from Defs.atualizar import atualiza_funcionario

                                atualiza_funcionario()
                                from Defs.listar import listar_funcionario

                                listar_funcionario()

                            elif submenuAtualiza == "22":
                                registrar_atividade("usuario acessou menu de cargo")
                                from Defs.listar import listar_cargo

                                listar_cargo()
                                from Defs.atualizar import atualiza_cargo

                                atualiza_cargo()
                                from Defs.listar import listar_cargo

                                listar_cargo()

                            elif submenuAtualiza == "23":
                                registrar_atividade("usuario acessou menu de plano")
                                from Defs.listar import listar_plano

                                listar_plano()
                                from Defs.atualizar import atualiza_plano

                                atualiza_plano()
                                from Defs.listar import listar_plano

                                listar_plano()

                            elif submenuAtualiza == "24":
                                registrar_atividade("usuario acessou menu de endereço")
                                from Defs.listar import listar_endereco

                                listar_endereco()
                                from Defs.atualizar import atualiza_end_completo

                                atualiza_end_completo()
                                from Defs.listar import listar_endereco

                                listar_endereco()
                            else:
                                print(
                                    "\033[1;31mOpção Inválida!\nDigite um opção de [0 ou 19 a 24]\n\033[0;0m"
                                )

                    # EXCLUIR
                    elif opcao == "5":
                        while True:
                            submenuExcluir = input(
                                "\033[1;31m>>>>>>>> MENU EXCLUIR <<<<<<<<\n\033[0;0m"
                                "[\033[1;31m 25 \033[0;0m] - Aluno\n"
                                "[\033[1;31m 26 \033[0;0m] - Usuario\n"
                                "[\033[1;31m 27 \033[0;0m] - Funcionario\n"
                                "[\033[1;31m 28 \033[0;0m] - Cargos\n"
                                "[\033[1;31m 29 \033[0;0m] - Planos\n"
                                "[\033[1;31m 30 \033[0;0m] - Endereços\n"
                                "[\033[1;31m  0 \033[0;0m] - Voltar ao menu\n"
                                "\033[1;31mInsira a opção desejada =>\033[0;0m "
                            )
                            registrar_atividade("usuario acessou menu de excluir")
                            if submenuExcluir == "0":
                                print("-" * 30)
                                break

                            elif submenuExcluir == "25":
                                registrar_atividade(
                                    "usuario acessou menu de exclusão de aluno"
                                )
                                from Defs.excluir import excluir_aluno
                                from Defs.listar import listar_aluno

                                listar_aluno()
                                excluir_aluno()
                                listar_aluno()

                            elif submenuExcluir == "26":
                                registrar_atividade(
                                    "usuario acessou menu de exclusão de usuario"
                                )
                                from Defs.excluir import excluir_usuario
                                from Defs.listar import listar_usuario

                                listar_usuario()
                                excluir_usuario()
                                listar_usuario()

                            elif submenuExcluir == "27":
                                registrar_atividade(
                                    "usuario acessou menu de exclusão de funcionario"
                                )
                                from Defs.excluir import excluir_funcionario
                                from Defs.listar import listar_funcionario

                                listar_funcionario()
                                excluir_funcionario()
                                listar_funcionario()

                            elif submenuExcluir == "28":
                                registrar_atividade(
                                    "usuario acessou menu de exclusão de cargo"
                                )
                                from Defs.excluir import excluir_cargo
                                from Defs.listar import listar_cargo

                                listar_cargo()
                                excluir_cargo()
                                listar_cargo()

                            elif submenuExcluir == "29":
                                registrar_atividade(
                                    "usuario acessou menu de exclusão de plano"
                                )
                                from Defs.excluir import excluir_plano
                                from Defs.listar import listar_plano

                                listar_plano()
                                excluir_plano()
                                listar_plano()

                            elif submenuExcluir == "30":
                                registrar_atividade(
                                    "usuario acessou menu de exclusão de endereço"
                                )
                                from Defs.excluir import excluir_endereco
                                from Defs.listar import listar_endereco

                                listar_endereco()
                                excluir_endereco()
                                listar_endereco()

                            else:
                                print(
                                    "Opção Inválida!\n\033[1;31mDigite um opção de [0 ou 25 a 30]\n\033[0m"
                                )

                    # RELATORIO
                    elif opcao == "6":
                        while True:
                            submenuRelatorio = input(
                                "\033[0;33m>>>>>>>> MENU RELATORIOS <<<<<<<<\n\033[0;0m"
                                "[\033[0;33m 31 \033[0;0m] - Funcionario vs Cargo\n"
                                "[\033[0;33m 32 \033[0;0m] - Maiores Salarios por Setor\n"
                                "[\033[0;33m 33 \033[0;0m] - Aniversariantes do mês\n"
                                "[\033[0;33m 34 \033[0;0m] - Alunos Matriculados mês\n"
                                "[\033[0;33m 35 \033[0;0m] - Exporta PDF Relatorio de Alunos\n"
                                "[\033[0;33m  0 \033[0;0m] - Voltar ao menu\n"
                                "\033[0;33mInsira a opção desejada =>\033[0;0m "
                            )
                            registrar_atividade("usuario acessou menu de relatorio")
                            if submenuRelatorio == "0":
                                print("-" * 30)
                                break

                            elif submenuRelatorio == "31":
                                from Defs.join import join_funcionario_cargo

                                join_funcionario_cargo()
                                registrar_atividade(
                                    "usuario acessou menu de relatorio Funcionario vs Cargo"
                                )

                            elif submenuRelatorio == "32":
                                from Defs.join import salarios

                                salarios()
                                from Defs.join import gera_grafico_salario

                                gera_grafico_salario()
                                registrar_atividade(
                                    "usuario acessou menu de relatorio Maiores Salarios por Setor"
                                )

                            elif submenuRelatorio == "33":
                                from Defs.join import aniversario

                                aniversario()
                                registrar_atividade(
                                    "usuario acessou menu de relatorio Aniversariantes do mês"
                                )

                            elif submenuRelatorio == "34":
                                from Defs.join import alunos_matriculados_mes

                                alunos_matriculados_mes()
                                registrar_atividade(
                                    "usuario acessou menu de relatorio Alunos matriculados mês"
                                )

                            elif submenuRelatorio == "35":
                                gerar_pdf()
                                registrar_atividade(
                                    "usuario acessou menu de relatorio Exporta PDF alunos"
                                )

                            else:
                                print(
                                    "Opção Inválida!\n\033[0;33mDigite um opção de [0 ou 31 a 35]\n\033[0m"
                                )
                                registrar_atividade(
                                    "usuario digitou no menu relatorios opção inválida [0 ou 31 a 35]!"
                                )

                    else:
                        print(
                            "Opção Inválida!\n\033[1;31mDigite um opção de [0 a 6]\n\033[0m"
                        )
                        registrar_atividade(
                            "usuario digitou opção inválida. Opção diferente de [0 a 6] no menu de login!"
                        )
        else:
            print("\033[1;31mLogin ou senha incorretos!\033[0m")
            registrar_atividade("usuario digitou Login ou senha incorretos!")


main()
