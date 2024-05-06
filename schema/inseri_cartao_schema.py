from marshmallow import Schema
from marshmallow.fields import Str

from utils.responses.messages import MSG_FIELD_REQUIRED

class InseriCartaoRequestSchema(Schema):
    nr_cartao = Str(required=True, error_messages={'required': MSG_FIELD_REQUIRED})
    nm_nome_cartao = Str(required=True, error_messages={'required': MSG_FIELD_REQUIRED})