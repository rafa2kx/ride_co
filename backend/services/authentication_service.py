from flask_jwt_extended import create_access_token
from repositories.user_repository import UserRepository
from services.base_service import BaseService

class AuthenticationService(BaseService):
    def __init__(self):
        super().__init__()
        self.user_repository = self._get_repository(UserRepository)

    def get_token(self, google_decoded_token: dict):
        email = google_decoded_token.get('email', '')
        family_name = google_decoded_token.get('family_name', '')
        given_name = google_decoded_token.get('given_name', '')
        user = self.user_repository.get_or_add_user_by_email(email, family_name, given_name)
        if not user:
            return None
        return create_access_token(identity=user)