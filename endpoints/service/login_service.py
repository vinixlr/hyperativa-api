import logging
import requests

from models.model import UserModel
from config.logger import log
from infra.helper import auth

class LoginService:
    def login(self, login_request):
        """
        service responsavel por gerar chave de autenticação login
        """
        log(f"user {login_request.get("user_name")} : iniciando requisição de login")

        try:
            retorno = auth(UserModel(login_request.get("user_name"), login_request.get("password")))
            log(f"user {login_request.get("user_name")} : login realizado com sucesso")
            return retorno, None

        except requests.exceptions.RequestException as e:
            log(f"user {login_request.get("user_name")} : erro ao realizar login")          
            return None, str(e)
        
