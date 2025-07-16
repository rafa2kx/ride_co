from sqlalchemy import Column, Float, Integer, String
from extension import db
from models.base_model import BaseModel

class Product(BaseModel):
    __tablename__ = 'products'

    name = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)
    price = Column(Float, nullable=False)
    category_id = Column(Integer, db.ForeignKey('categories.id'), nullable=True)
    family_id = Column(Integer, db.ForeignKey('families.id'), nullable=True)
    category = db.relationship('Category', back_populates='products')
