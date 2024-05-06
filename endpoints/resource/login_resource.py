from flask import request
from flask_restful import Resource

from marshmallow import ValidationError
from schema.login_schema import LoginRequestSchema
from endpoints.service.login_service import LoginService
from utils.utilitarios import has_empty_or_null_value
from utils.responses.responses import resp_error, resp_ok
from utils.responses.messages import (
MSG_INVALID_DATA,
MSG_ERRO_LOGIN,
MSG_LOGIN_SUCCESS
)

RESOURCE_NAME = "Login"

class LoginResource(Resource):
    def post(self):
        """
        Resource responsavel por gerar token com login
        """
        req_data = request.get_json() or None
        if not req_data or has_empty_or_null_value(req_data):
            return resp_error(RESOURCE_NAME, None, MSG_INVALID_DATA)
        
        try:
            login_request = LoginRequestSchema().load(req_data)
        except ValidationError as err:
            return resp_error(RESOURCE_NAME, err.messages, MSG_ERRO_LOGIN)
            
        retorno, erros = LoginService().login(login_request)
        
        if not retorno:
            return resp_error(RESOURCE_NAME, None, erros)

        return resp_ok(RESOURCE_NAME, MSG_LOGIN_SUCCESS, data=retorno)