from flask import request
from flask_restful import Resource

from infra.helper import validate_jwt
from endpoints.service.insere_lote_service import InsereLoteService
from utils.responses.responses import resp_error, resp_ok
from utils.responses.messages import (
    MSG_ERRO_TOKEN,
    MSG_SUCCESS,
    MSG_INVALID_TXT_FILE,
)

RESOURCE_NAME = "Inserir Lote"

class InsereLoteResource(Resource):
    def post(self):
        """
        Resource responsavel por inserir um cartao
        """
        file = request.files
        if not file:
            return resp_error(RESOURCE_NAME, None, MSG_INVALID_TXT_FILE)
        
        login_request, erros = validate_jwt(request.headers.get("idSessao"))
        if erros:
            return resp_error(RESOURCE_NAME, None, MSG_ERRO_TOKEN)
        
        retorno, erros = InsereLoteService().insere_lote_request(file, login_request)

        if not retorno:
            return resp_error(RESOURCE_NAME, None, erros)
        
        return resp_ok(RESOURCE_NAME, MSG_SUCCESS, data={})