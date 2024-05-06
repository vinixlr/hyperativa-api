from marshmallow import Schema
from marshmallow.fields import Str

from utils.responses.messages import MSG_FIELD_REQUIRED

class LoginRequestSchema(Schema):
    user_name = Str(required=True, error_messages={'required': MSG_FIELD_REQUIRED})
    password = Str(required=True, error_messages={'required': MSG_FIELD_REQUIRED})