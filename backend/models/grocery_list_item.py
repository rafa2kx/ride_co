from sqlalchemy import Column
from sqlalchemy import Integer, String, Boolean
from models.base_model import BaseModel
from extension import db

class GroceryListItem(BaseModel):
    __tablename__ = 'grocery_list_items'

    grocery_list_id = Column(Integer, db.ForeignKey('grocery_lists.id'), nullable=False)
    grocery_list = db.relationship('GroceryList', back_populates='items',)
    
    product_id = Column(Integer, db.ForeignKey('products.id'), nullable=True)
    product = db.relationship('Product')
    
    custom_name = Column(String(255), nullable=True)
    quantity = Column(Integer, nullable=False, default=1)
    notes = Column(String(255), nullable=True)
    purchased = Column(Boolean, nullable=False, default=False)