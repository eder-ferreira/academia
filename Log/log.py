# import logging
#
# def configurar_logger(nome_arquivo='Log/logfile.log'):
#     # Configurar o logger
#     logging.basicConfig(filename=nome_arquivo,
#                         level=logging.DEBUG,
#                         format='%(asctime)s - %(levelname)s - %(message)s')
#
# def registrar_log(mensagem, nivel=logging.INFO):
#     # Registra uma mensagem no nível especificado
#     logging.log(nivel, mensagem)
#
# # Exemplo de uso
# configurar_logger()  # Configurar o logger com as configurações padrão
#
# # Registra mensagens de log
# registrar_log("Isso é uma mensagem de informação.", logging.INFO)
# registrar_log("Isso é uma mensagem de aviso.", logging.WARNING)
# registrar_log("Isso é uma mensagem de erro.", logging.ERROR)


import logging

# Configurar o logger
logging.basicConfig(
    filename="Log/atividades.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Função para registrar uma atividade
def registrar_atividade(atividade):
    logging.info(atividade)


logging.shutdown()
