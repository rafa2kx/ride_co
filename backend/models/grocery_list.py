from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String
from extension import db

class GroceryList(BaseModel):
    __tablename__ = 'grocery_lists'

    name = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)
    family_id = Column(Integer, db.ForeignKey('families.id'))
    items = db.relationship('GroceryListItem', back_populates='grocery_list', cascade='all, delete-orphan')
    family = db.relationship('Family', back_populates='lists')
