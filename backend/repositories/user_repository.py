
from models.family import Family
from models.user import User
from repositories.base_repository import BaseRepository

class UserRepository(BaseRepository):
    
    def get_user_by_email(self, email:str):
        user = self.session.query(User) \
            .where(User.email == email) \
            .first()

        return user.as_dict() if user else None
    
    def get_or_add_user_by_email(self, email: str, family_name: str = None, given_name: str = None, family_id: int = None):
        """
        Fetches a user by email or creates a new one if it doesn't exist.
        """
        user = self.get_user_by_email(email)
        if not user:
            if not family_id:
                family = Family(name=family_name, description=f'{family_name}''s Family') if family_name else None
                self.session.add(family)
            else:
                family = self.session.query(Family).filter(Family.id == family_id).first()
                if not family:
                    raise ValueError("Family not found")
            user = User(email=email, family=family, username=email.split('@')[0]) if family else User(email=email, username=f'{given_name}_{email}')
            self.session.add(user)
            self.session.commit()
            return user.as_dict()
        
        return user 
        