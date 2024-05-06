import logging
import requests

from models.model import CartaoModel
from config.logger import log
from utils.responses.messages import MSG_NO_DATA_FOUND

class ConsultaCartaoService:
    def consulta_cartao_request(self, cartao, login_request):
        """
        service responsavel por consultar um cartao
        """
        log(f"user {login_request.get("user_name")} : iniciando requisição de consulta de cartao")
        
        try:
            retorno = CartaoModel.find_by_numero_cartao(cartao)
            if not retorno:
                log(f"user {login_request.get("user_name")} : erro ao consulta de cartao")
                return None, MSG_NO_DATA_FOUND      

            log("consulta de cartao realizada com sucesso")
            return retorno, None

        except requests.exceptions.RequestException as e:
            log(f"user {login_request.get("user_name")} : erro ao consulta de cartao")

            return None, str(e)
