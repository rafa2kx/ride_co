from flask import Blueprint, g
import jwt
# from extension import jwt
from services.authentication_service import AuthenticationService
from services.base_service import get_service
from utils.response_wrapper import make_response

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/auth", methods=['POST'])
def login():
    data:dict = g.get('snake_case_json', {})
    google_token = data.get('token')
    decoded_data:dict = jwt.decode(google_token,  options={"verify_signature": False})
    if not decoded_data:
        return make_response(message="Invalid token", success=False, status_code= 401)

    auth_service = get_service(AuthenticationService)
    token = auth_service.get_token(decoded_data)

    if not token :
        return make_response(message="Invalid credentials", success=False, status_code= 401)

    return make_response({"token": token }, 200)
