from flask import request
from flask_restful import Resource
from infra.helper import validate_jwt
from endpoints.service.consulta_cartao_service import ConsultaCartaoService
from utils.responses.responses import resp_error, resp_ok
from utils.responses.messages import MSG_ERRO_TOKEN, MSG_SUCCESS


RESOURCE_NAME = "Consulta Cartao"

class ConsultaCartaoResource(Resource):
    def get(self, cartao):
        """
        Resource responsavel por buscar cartao
        """
        login_request, erros = validate_jwt(request.headers.get("idSessao"))
        if erros:
            return resp_error(RESOURCE_NAME, None, MSG_ERRO_TOKEN)
        
        retorno, erros = ConsultaCartaoService().consulta_cartao_request(cartao, login_request)

        if erros:
            return resp_error(RESOURCE_NAME, None, erros)
        
        return resp_ok(RESOURCE_NAME, MSG_SUCCESS, data={"id": retorno.id,
                                                         "nrCartao": retorno.nr_cartao,
                                                         "nmCartaoNome": retorno.nm_cartao_nome,
                                                         "dtInclusao": retorno.dt_inclusao,
                                                         "loteId": retorno.lote_id})