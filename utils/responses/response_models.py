from typing import Any

from pydantic import BaseModel

from utils.responses.response_model_abstract import ResponseModelAbstract

class ResponseError400Model(BaseModel, ResponseModelAbstract):
    status: int
    resource: str
    message : str
    errors : Any = None

    def set_response(self, response):
        self.errors = response

class ResponseSuccessModel(BaseModel, ResponseModelAbstract):
    status: int
    message: str
    resource: str
    dados: Any = None

    def set_response(self, response):
        self.dados = response