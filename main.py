import sys
from datetime import datetime
from datetime import date
from Defs.cadastrar import cadastrar_aluno
from Defs.cadastrar import cadastrar_usuario
from Defs.cadastrar import cadastrar_funcionario
from Defs.cadastrar import cadastrar_cargo
from Defs.cadastrar import cadastrar_plano
from Defs.validar_login import autentica_login

data = date.today()
dia = data.day
mes = data.month
ano = data.year

menu = [
    "\033[0;34m>>>>>>>> MENU OPÇÕES <<<<<<<<\n\033[0;0m"
    "\033[0;34m[1]\033[0;0m - Cadastrar\n"
    "\033[0;34m[2]\033[0;0m - Listar\n"
    "\033[0;34m[3]\033[0;0m - Pesquisar\n"
    "\033[0;34m[4]\033[0;0m - Atualizar\n"
    "\033[0;34m[5]\033[0;0m - Excluir\n"
    "\033[0;34m[6]\033[0;0m - Relatorio\n"    
    "\033[0;34m[0]\033[0;0m - Sair"]


def tela_login():
    print("   [[[====]]]      [[[====]]]"
     f"\n\033[0;32mData: {data} "
      "\n<<<<<<<= TELA DE LOGIN =>>>>>>>>",
      "\n[0] - Sair"
      "\n[1] - Logar"
      "\n[2] - Cadastrar Novo Usuario\033[0m")

def main():
    while True:
        tela_login()
        opcao = input("\033[0;32mInsira a opção=> \033[0m")
        if opcao == '0':
            print("\n\033[0;31mFechando o programa....\n\033[0;0m")
            sys.exit()

        elif opcao == '2':
            cadastrar_usuario()

        elif opcao == '1':
            print("\n<<<<<<<<= \033[0;34mMENU LOGAR \033[0;0m=>>>>>>>>>>")
            login = input("Digite seu login=> ")
            senha = input("Digite sua senha=> ")
            if autentica_login(login, senha):
                print("=" * 36)
                print("\033[0;34mLogin bem-sucedido!\033[0m\n")
                print("-" * 36)
                print(f" Data: {data}")
                print(f" Olá, seja bem vindo(a): {login}!")
                print("-" * 36)

                while True:
                    for opcao in menu:
                        print(opcao)
                    opcao = input("\033[0;34mInsira a opção desejada 0 =>\033[0;0m ")
                    print("-" * 30)

                    if opcao == "0":
                        print('\033[1;31mFinalizando programa....')
                        sys.exit()

                    # CADASTRAR
                    elif opcao == "1":
                        while True:
                            submenuCadastrar = input(
                                "\n>>>>> MENU CADASTRAR <<<<<\n"
                                "[1] - Aluno\n"
                                "[2] - Usuario \n"
                                "[3] - Funcionario\n"
                                "[4] - Cargos\n"
                                "[5] - Planos\n"
                                "[6] - Endereços\n"
                                "[0] - Voltar ao menu\n"
                                "Insira a opção desejada=> ")

                            if submenuCadastrar == "0":
                                print("-" * 30)
                                break

                            elif submenuCadastrar == "1":
                                cadastrar_aluno()

                            elif submenuCadastrar == "2":
                                cadastrar_usuario()

                            elif submenuCadastrar == "3":
                                cadastrar_funcionario()

                            elif submenuCadastrar == "4":
                                cadastrar_cargo()

                            elif submenuCadastrar == "5":
                                cadastrar_plano()

                            elif submenuCadastrar == "6":
                                from Defs.listar import listar_endereco
                                listar_endereco()
                                from Defs.atualizar import atualiza_end_completo
                                atualiza_end_completo()
                            else:
                                print("\033[1;31mOpção Inválida!\nDigite um opção de [0 a 6]\n\033[0;0m")

                    # LISTAR
                    elif opcao == "2":
                        while True:
                            submenuListar = input(
                                "\n>>>>> MENU LISTAR <<<<<\n"
                                "[ 7] - Aluno\n"
                                "[ 8] - Usuario \n"
                                "[ 9] - Funcionario\n"
                                "[10] - Cargos\n"
                                "[11] - Planos\n"
                                "[12] - Endereços\n"
                                "[ 0] - Voltar ao menu\n"
                                "Insira a opção desejada=> ")

                            if submenuListar == "0":
                                print("-" * 30)
                                break

                            elif submenuListar == "7":
                                from Defs.listar import listar_aluno
                                listar_aluno()

                            elif submenuListar == "8":
                                from Defs.listar import listar_usuario
                                listar_usuario()

                            elif submenuListar == "9":
                                from Defs.listar import listar_funcionario
                                listar_funcionario()

                            elif submenuListar == "10":
                                from Defs.listar import listar_cargo
                                listar_cargo()

                            elif submenuListar == "11":
                                from Defs.listar import listar_plano
                                listar_plano()

                            elif submenuListar == "12":
                                from Defs.listar import listar_endereco
                                listar_endereco()
                            else:
                                print("\033[1;31mOpção Inválida!\nDigite um opção de [0 ou 7 a 12]\n\033[0;0m")

                    # BUSCAR
                    elif opcao == "3":
                        while True:
                            submenuBuscar = input(
                                "\n>>>>> MENU PESQUISAR <<<<<\n"
                                "[13] - Aluno\n"
                                "[14] - Usuario \n"
                                "[15] - Funcionario\n"
                                "[16] - Cargos\n"
                                "[17] - Planos\n"
                                "[18] - Endereços\n"
                                "[0] - Voltar ao menu\n"
                                "Insira a opção desejada=> ")

                            if submenuBuscar == "0":
                                print("-" * 30)
                                break

                            elif submenuBuscar == "13":
                                from Defs.buscar import buscar_aluno
                                buscar_aluno()

                            elif submenuBuscar == "14":
                                from Defs.buscar import buscar_usuario
                                buscar_usuario()

                            elif submenuBuscar == "15":
                                from Defs.buscar import buscar_funcionario
                                buscar_funcionario()

                            elif submenuBuscar == "16":
                                from Defs.buscar import buscar_cargo
                                buscar_cargo()

                            elif submenuBuscar == "17":
                                from Defs.buscar import buscar_plano
                                buscar_plano()

                            elif submenuBuscar == "18":
                                from Defs.buscar import buscar_endereco
                                buscar_endereco()
                            else:
                                print("\033[1;31mOpção Inválida!\nDigite um opção de [0 ou 13 a 18]\n\033[0;0m")

                    # ATUALIZAR
                    elif opcao == "4":
                        while True:
                            submenuAtualiza = input(
                                "\n>>>>> MENU ATUALIZAR <<<<<\n"
                                "[19] - Aluno\n"
                                "[20] - Usuario \n"
                                "[21] - Funcionario\n"
                                "[22] - Cargos\n"
                                "[23] - Planos\n"
                                "[24] - Endereços\n"
                                "[ 0] - Voltar ao menu\n"
                                "Insira a opção desejada=> ")

                            if submenuAtualiza == "0":
                                print("-" * 30)
                                break

                            elif submenuAtualiza == "19":
                                from Defs.listar import listar_aluno
                                listar_aluno()
                                from Defs.atualizar import atualiza_aluno
                                atualiza_aluno()
                                from Defs.listar import listar_aluno
                                listar_aluno()

                            elif submenuAtualiza == "20":
                                from Defs.listar import listar_usuario
                                listar_usuario()
                                from Defs.atualizar import atualiza_usuario
                                atualiza_usuario()
                                from Defs.listar import listar_usuario
                                listar_usuario()

                            elif submenuAtualiza == "21":
                                from Defs.listar import listar_funcionario
                                listar_funcionario()
                                from Defs.atualizar import atualiza_funcionario
                                atualiza_funcionario()
                                from Defs.listar import listar_funcionario
                                listar_funcionario()

                            elif submenuAtualiza == "22":
                                from Defs.listar import listar_cargo
                                listar_cargo()
                                from Defs.atualizar import atualiza_cargo
                                atualiza_cargo()
                                from Defs.listar import listar_cargo
                                listar_cargo()

                            elif submenuAtualiza == "23":
                                from Defs.listar import listar_plano
                                listar_plano()
                                from Defs.atualizar import atualiza_plano
                                atualiza_plano()
                                from Defs.listar import listar_plano
                                listar_plano()

                            elif submenuAtualiza == "24":
                                from Defs.listar import listar_endereco
                                listar_endereco()
                                from Defs.atualizar import atualiza_end_completo
                                atualiza_end_completo()
                                from Defs.listar import listar_endereco
                                listar_endereco()
                            else:
                                print("\033[1;31mOpção Inválida!\nDigite um opção de [0 ou 19 a 24]\n\033[0;0m")

                    # EXCLUIR
                    elif opcao == "5":
                        while True:
                            submenuExcluir = input(
                                "\n>>>>> MENU EXCLUIR <<<<<\n"
                                "[25] - Aluno\n"
                                "[26] - Usuario \n"
                                "[27] - Funcionario\n"
                                "[28] - Cargos\n"
                                "[29] - Planos\n"
                                "[30] - Endereços\n"
                                "[ 0] - Voltar ao menu\n"
                                "Insira a opção desejada=> ")

                            if submenuExcluir == "0":
                                print("-" * 30)
                                break

                            elif submenuExcluir == "25":
                                from Defs.excluir import excluir_aluno
                                from Defs.listar import listar_aluno
                                listar_aluno()
                                excluir_aluno()
                                listar_aluno()

                            elif submenuExcluir == "26":
                                from Defs.excluir import excluir_usuario
                                from Defs.listar import listar_usuario
                                listar_usuario()
                                excluir_usuario()
                                listar_usuario()

                            elif submenuExcluir == "27":
                                from Defs.excluir import excluir_funcionario
                                from Defs.listar import listar_funcionario
                                listar_funcionario()
                                excluir_funcionario()
                                listar_funcionario()

                            elif submenuExcluir == "28":
                                from Defs.excluir import excluir_cargo
                                from Defs.listar import listar_cargo
                                listar_cargo()
                                excluir_cargo()
                                listar_cargo()


                            elif submenuExcluir == "29":
                                from Defs.excluir import excluir_plano
                                from Defs.listar import listar_plano
                                listar_plano()
                                excluir_plano()
                                listar_plano()


                            elif submenuExcluir == "30":
                                from Defs.excluir import excluir_endereco
                                from Defs.listar import listar_endereco
                                listar_endereco()
                                excluir_endereco()
                                listar_endereco()

                            else:
                                print("\033[1;31mOpção Inválida!\nDigite um opção de [0 ou 25 a 30]\n\033[0m")

                    # RELATORIO
                    elif opcao == "6":
                        while True:
                            submenuRelatorio = input(
                                "\n>>>>> MENU RELATORIOS <<<<<\n"
                                "[31] - Funcionario vs Cargo\n"
                                "[32] - Maiores Salarios \n"
                                "[33] - Aniversariantes do mês \n"
                                "[ 0] - Voltar ao menu\n"
                                "Insira a opção desejada=> ")

                            if submenuRelatorio == "0":
                                print("-" * 30)
                                break

                            elif submenuRelatorio == "31":
                                from Defs.join import join_funcionario_cargo
                                join_funcionario_cargo()

                            elif submenuRelatorio == "32":
                                from Defs.join import salarios
                                salarios()
                                from Defs.join import gera_grafico_salario
                                gera_grafico_salario()

                            elif submenuRelatorio == "33":
                                from Defs.join import aniversario
                                aniversario()

                            else:
                                print("\033[1;31mOpção Inválida!\nDigite um opção de [0 ou 25 a 30]\n\033[0m")

                    else:
                        print("\033[1;31mOpção Inválida!\nDigite um opção de [0 a 5]\n\033[0m")

            else:
                print("\033[1;31mLogin ou senha incorretos!\033[0m")

main()
