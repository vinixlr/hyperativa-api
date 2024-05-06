import logging

def configurar_logger(nome_arquivo='log.log'):
    logging.basicConfig(filename=nome_arquivo, level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

def log(mensagem):
    logging.info(mensagem)