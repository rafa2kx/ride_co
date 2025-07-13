from sqlalchemy import Column, Integer, String
from models.base_model import BaseModel
from extension import db

class User(BaseModel):
    __tablename__ = 'users'

    username = Column(String(100), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    family_id = Column(Integer, db.ForeignKey('families.id'), nullable=True)
    family = db.relationship('Family', back_populates='users')
    def __repr__(self):
        return f"<User {self.name}>"