from sqlalchemy import Column, Integer, String
from models.base_model import BaseModel
from extension import db

class Family(BaseModel):
    __tablename__ = 'families'

    name = Column(String(100), nullable=False, unique=True)
    description = Column(String(255), nullable=True)
    users = db.relationship('User', back_populates='family', cascade='all, delete-orphan')
    lists = db.relationship('GroceryList', back_populates='family', cascade='all, delete-orphan')
    def __repr__(self):
        return f"<User {self.name}>"