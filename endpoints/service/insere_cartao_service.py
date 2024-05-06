import logging
import requests

from models.model import CartaoModel
from config.logger import log
from utils.responses.messages import MSG_NO_DATA_FOUND

class InsereCartaoService:
    def insere_cartao_request(self, novo_cartao_request, login_request):
        """
        service responsavel por inserer um cartao
        """
        log(f"user {login_request.get("user_name")} : iniciando requisição de insere de cartao")
        
        try:
            retorno, erros = CartaoModel(novo_cartao_request.get("nr_cartao"), novo_cartao_request.get("nm_nome_cartao")).save_to_db()
            log(f"user {login_request.get("user_name")} : inserção de cartao realizada com sucesso")

            return retorno, erros

        except requests.exceptions.RequestException as e:
            log(f"user {login_request.get("user_name")} : erro ao insere de cartao")

            return None, str(e)
