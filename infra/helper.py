import jwt
from datetime import datetime, timedelta
from requests.exceptions import RequestException
from utils.enum.token_enum import EstadoToken
from config.chave_screta import CHAVE_SECRETA

from models.model import UserModel

def auth(auth_request: UserModel):
    user_query = auth_request.find_by_name()
    if user_query.nome == auth_request.nome and user_query.password == auth_request.password:
        token_payload = {
            'user_name': auth_request.nome,
            'exp': datetime.utcnow() + timedelta(minutes=12)
        }
        token = jwt.encode(token_payload, CHAVE_SECRETA, algorithm='HS256')
        return token_padronizado(token), None
    
    raise RequestException(EstadoToken.NAO_AUTENTICADO.name)

def validate_jwt(token):
    try:
        payload = jwt.decode(token, CHAVE_SECRETA, algorithms=["HS256"])
        return payload, None
    except jwt.ExpiredSignatureError:
        return None, EstadoToken.EXPIRADO
    except jwt.InvalidTokenError:
        return None, EstadoToken.INVALIDO

def token_padronizado(token):
    return {"idSessao": token, 
            "dataExp": datetime.now() + timedelta(minutes=12)
    }