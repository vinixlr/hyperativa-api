from flask import request
from flask_restful import Resource

from marshmallow import ValidationError
from schema.inseri_cartao_schema import InseriCartaoRequestSchema
from infra.helper import validate_jwt
from utils.utilitarios import has_empty_or_null_value
from endpoints.service.insere_cartao_service import InsereCartaoService
from utils.responses.responses import resp_error, resp_ok
from utils.responses.messages import (
    MSG_ERRO_TOKEN,
    MSG_SUCCESS,
    MSG_INVALID_DATA,
    MSG_ERRO_CARD_INSERT
)

RESOURCE_NAME = "Inserir Cartao"

class InsereCartaoResource(Resource):
    def post(self):
        """
        Resource responsavel por inserir um cartao
        """
        req_data = request.get_json() or None
        if not req_data or has_empty_or_null_value(req_data):
            return resp_error(RESOURCE_NAME, None, MSG_INVALID_DATA)
        
        try:
            inserir_cartao_request = InseriCartaoRequestSchema().load(req_data)
        except ValidationError as err:
            return resp_error(RESOURCE_NAME, err.messages, MSG_ERRO_CARD_INSERT)
        
        login_request, erros = validate_jwt(request.headers.get("idSessao"))
        if erros:
            return resp_error(RESOURCE_NAME, None, MSG_ERRO_TOKEN)
        
        retorno, erros = InsereCartaoService().insere_cartao_request(inserir_cartao_request, login_request)

        if not retorno:
            return resp_error(RESOURCE_NAME, None, erros)
        
        return resp_ok(RESOURCE_NAME, MSG_SUCCESS, data={})