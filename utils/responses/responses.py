from flask import jsonify

from utils.responses.response_models import ResponseError400Model, ResponseSuccessModel
from utils.responses.messages import MSG_SUCCESS, MSG_INVALID_DATA, MSG_ERRO_STRING_MISSING

def resp_ok(resource: str, message: str, data=None, **extras):
    """
    Responses 200
    """
    if not resource:
        resource = ""

    if not message:
        message = MSG_SUCCESS

    response_model = ResponseSuccessModel(
        status=200,
        message=message,
        resource=resource,
        dados=data,
    )

    response = response_model.model_dump()

    response.update(extras)
    resp = jsonify(response)
    resp.status_code = 200

    return resp

def resp_error(resource: str, errors: object, msg: str = MSG_INVALID_DATA):
    """
    Responses 400
    """
    if not isinstance(resource, str):
        raise ValueError(MSG_ERRO_STRING_MISSING)

    response_model = ResponseError400Model(
        status=400,
        message=msg,
        resource=resource,
        errors=errors,
    )

    resp = jsonify(response_model.model_dump())
    resp.status_code = 400

    return resp