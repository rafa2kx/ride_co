from sqlalchemy import Column, Integer, String
from models.base_model import BaseModel
from extension import db

class Store(BaseModel):
    __tablename__ = 'stores'

    name = Column(String(100), nullable=False, unique=True)
    address = Column(String(255), nullable=False)
    phone_number = Column(String(20), nullable=True)
    email = Column(String(100), nullable=True)

    def __repr__(self):
        return f"<Store {self.name}>"