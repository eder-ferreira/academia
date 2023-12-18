def validar_campo(campo):
    while not campo:
        print("\033[1;31mCampo vazio! Por favor, preencha o campo!\033[0m")
        campo = input(f"Digite o valor {campo}: ")
    return True


def validar_opcao_login(campo):
    while not campo:
        print("\033[1;31mOpção Inexistente!\033[0m")
        campo = input("\033[0;34mInsira a opção=> \033[0m")
    return True
