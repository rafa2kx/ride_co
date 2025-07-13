
from models.family import Family
from models.user import User
from repositories.base_repository import BaseRepository

class UserRepository(BaseRepository):
    
    def get_user_by_email(self, email:str):
        user = self.session.query(User) \
            .where(User.email == email) \
            .first()

        return user.as_dict() if user else None
    
    def get_or_add_user_by_email(self, email: str, family_name: str = None, given_name: str = None):
        """
        Fetches a user by email or creates a new one if it doesn't exist.
        """
        user = self.get_user_by_email(email)
        if not user:
            family = Family(name=family_name, description=f'{family_name}''s Family') if family_name else None
            user = User(email=email, family=family, user_name=f'{email.split('@')[0]}') if family else User(email=email, user_name=f'{given_name}_{email}')
            self.session.add_all(user, family)
            self.session.commit()
            return user.as_dict()
        
        return user 
        