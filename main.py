import sys

menu = [
    ">>>>>>>> MENU OPÇÕES <<<<<<<<\n"
    "[1] - Cadastrar\n"
    "[2] - Listar\n"
    "[3] - Pesquisar\n"
    "[4] - Atualizar\n"
    "[5] - Excluir\n"
    "[0] - Sair"]


def main():

    while True:
        print("-" * 30)
        print(f"  Olá, seja bem vindo!")
        print("-" * 30)

        for opcao in menu:
            print(opcao)
        opcao = int(input("Insira a opção desejada 0 => "))
        print("-" * 30)

        if opcao == 0:
            print('\033[1;31mFinalizando programa....')
            sys.exit()

    # CADASTRAR
        elif opcao == 1:
            while True:
                submenuCadastrar = int(input(
                    "\n>>>>> MENU CADASTRAR <<<<<\n"
                    "[1] - Aluno\n"
                    "[2] - Usuario \n"
                    "[3] - Funcionario\n"
                    "[4] - Cargos\n"
                    "[5] - Planos\n"
                    "[6] - Endereços\n"
                    "[0] - Voltar ao menu\n"
                    "Insira a opção desejada=> "))

                if submenuCadastrar == 0:
                    print("\033[1;33mSair")
                    break
                elif submenuCadastrar == 1:
                    from CRUD.cadastrar import cadastrar_aluno
                    cadastrar_aluno()

                elif submenuCadastrar == 2:
                    from CRUD.cadastrar import cadastrar_usuario
                    cadastrar_usuario()

                elif submenuCadastrar == 3:
                    from CRUD.cadastrar import cadastrar_funcionario
                    cadastrar_funcionario()

                elif submenuCadastrar == 4:
                    from CRUD.cadastrar import cadastrar_cargo
                    cadastrar_cargo()

                elif submenuCadastrar == 5:
                    from CRUD.cadastrar import cadastrar_plano
                    cadastrar_plano()

                elif submenuCadastrar == 6:
                    from CRUD.cadastrar import cadastrar_endereco
                    cadastrar_endereco()

    # LISTAR
        elif opcao == 2:
            while True:
                submenuListar = int(input(
                    "\n>>>>> MENU LISTAR <<<<<\n"
                    "[7] - Aluno\n"
                    "[8] - Usuario \n"
                    "[9] - Funcionario\n"
                    "[10] - Cargos\n"
                    "[11] - Planos\n"
                    "[12] - Endereços\n"
                    "[0] - Voltar ao menu\n"
                    "Insira a opção desejada=> "))

                if submenuListar == 0:
                    print("\033[1;33mSair")
                    break

                elif submenuListar == 7:
                    from CRUD.listar import listar_aluno
                    listar_aluno()

                elif submenuListar == 8:
                    from CRUD.listar import listar_usuario
                    listar_usuario()

                elif submenuListar == 9:
                    from CRUD.listar import listar_funcionario
                    listar_funcionario()

                elif submenuListar == 10:
                    from CRUD.listar import listar_cargo
                    listar_cargo()

                elif submenuListar == 11:
                    from CRUD.listar import listar_plano
                    listar_plano()

                elif submenuListar == 12:
                    from CRUD.listar import listar_endereco
                    listar_endereco()

    # BUSCAR
        elif opcao == 3:
            while True:
                submenuBuscar = int(input(
                    "\n>>>>> MENU PESQUISAR <<<<<\n"
                    "[13] - Aluno\n"
                    "[14] - Usuario \n"
                    "[15] - Funcionario\n"
                    "[16] - Cargos\n"
                    "[17] - Planos\n"
                    "[18] - Endereços\n"
                    "[0] - Voltar ao menu\n"
                    "Insira a opção desejada=> "))

                if submenuBuscar == 0:
                    print("\033[1;33mSair")
                    break

                elif submenuBuscar == 13:
                    from CRUD.buscar import buscar_aluno
                    buscar_aluno()

                elif submenuBuscar == 14:
                    from CRUD.buscar import buscar_usuario
                    buscar_usuario()

                elif submenuBuscar == 15:
                    from CRUD.buscar import buscar_funcionario
                    buscar_funcionario()

                elif submenuBuscar == 16:
                    from CRUD.buscar import buscar_cargo
                    buscar_cargo()

                elif submenuBuscar == 17:
                    from CRUD.buscar import buscar_plano
                    buscar_plano()

                elif submenuBuscar == 18:
                    from CRUD.buscar import buscar_endereco
                    buscar_endereco()

    # ATUALIZAR
        elif opcao == 4:
            while True:
                submenuAtualiza = int(input(
                    "\n>>>>> MENU ATUALIZAR <<<<<\n"
                    "[19] - Aluno\n"
                    "[20] - Usuario \n"
                    "[21] - Funcionario\n"
                    "[22] - Cargos\n"
                    "[23] - Planos\n"
                    "[24] - Endereços\n"
                    "[0] - Voltar ao menu\n"
                    "Insira a opção desejada=> "))

                if submenuAtualiza == 0:
                    print("\033[1;33m")
                    break

                elif submenuAtualiza == 19:
                    from CRUD.listar import listar_aluno
                    listar_aluno()
                    from CRUD.atualizar import atualiza_aluno
                    atualiza_aluno()
                    from CRUD.listar import listar_aluno
                    listar_aluno()

                elif submenuAtualiza == 20:
                    from CRUD.listar import listar_usuario
                    listar_usuario()
                    from CRUD.atualizar import atualiza_usuario
                    atualiza_usuario()
                    from CRUD.listar import listar_usuario
                    listar_usuario()

                elif submenuAtualiza == 21:
                    from CRUD.listar import listar_funcionario
                    listar_funcionario()
                    from CRUD.atualizar import atualiza_funcionario
                    atualiza_funcionario()
                    from CRUD.listar import listar_funcionario
                    listar_funcionario()

                elif submenuAtualiza == 22:
                    from CRUD.listar import listar_cargo
                    listar_cargo()
                    from CRUD.atualizar import atualiza_cargo
                    atualiza_cargo()
                    from CRUD.listar import listar_cargo
                    listar_cargo()

                elif submenuAtualiza == 23:
                    from CRUD.listar import listar_plano
                    listar_plano()
                    from CRUD.atualizar import atualiza_plano
                    atualiza_plano()
                    from CRUD.listar import listar_plano
                    listar_plano()

                elif submenuAtualiza == 24:
                    from CRUD.listar import listar_endereco
                    listar_endereco()
                    from CRUD.atualizar import atualiza_endereco
                    atualiza_endereco()
                    from CRUD.listar import listar_endereco
                    listar_endereco()





    # EXCLUIR
        elif opcao == 5:
            while True:
                submenuExcluir = int(input(
                    "\n>>>>> MENU EXCLUIR <<<<<\n"
                    "[25] - Aluno\n"
                    "[26] - Usuario \n"
                    "[27] - Funcionario\n"
                    "[28] - Cargos\n"
                    "[29] - Planos\n"
                    "[30] - Endereços\n"
                    "[0] - Voltar ao menu\n"
                    "Insira a opção desejada=> "))

                if submenuExcluir == 0:
                    print("\033[1;33m")
                    break

                elif submenuExcluir == 25:
                    from CRUD.excluir import excluir_aluno
                    from CRUD.listar import listar_aluno
                    excluir_aluno()
                    listar_aluno()

                elif submenuExcluir == 26:
                    from CRUD.excluir import excluir_usuario
                    excluir_usuario()

                elif submenuExcluir == 27:
                    from CRUD.excluir import excluir_funcionario
                    excluir_funcionario()

                elif submenuExcluir == 28:
                    from CRUD.excluir import excluir_cargo
                    excluir_cargo()

                elif submenuExcluir == 29:
                    from CRUD.excluir import excluir_plano
                    excluir_plano()

                elif submenuExcluir == 30:
                    from CRUD.excluir import excluir_endereco
                    excluir_endereco()

        else:
            print("\033[1;33mOpção Inválida!")

main()
