from sqlalchemy import Column, String
from models.base_model import BaseModel
from extension import db

class Category(BaseModel):
    __tablename__ = 'categories'

    name = Column(String(100), nullable=False, unique=True)
    description = Column(String(255), nullable=True)
    products = db.relationship('Product', back_populates='category', cascade='all, delete-orphan')