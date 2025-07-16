
from sqlalchemy import and_, select,or_
from interfaces import IService
from models.grocery_list_item import GroceryListItem
from models.product import Product
from repositories.base_repository import BaseRepository
from models.grocery_list import GroceryList

class ProductsRepository(BaseRepository):
    
    def get_all_products(self, family_id:int):
        products = self.session.query(Product).filter(or_(Product.family_id == family_id, Product.family_id == None) ).all()
        return [product.as_dict() for product in products]
    
    def add_product(self, product: dict):
        """Add a new Product."""
        new_product = Product(**product)
        self.session.add(new_product)
        self.session.flush()
        return new_product.as_dict()
    
    def update_product(self, product_id:int, product: dict):
        """Update a Product."""
        record = self.session.query(Product).filter(Product.id == product_id).first()
        if not record:
            return None
        
        for key, value in product.items():
            setattr(record, key, value)
        
        self.session.flush()
        return record.as_dict()
    
    def delete_product(self, product_id: int):
        """Delete a Product."""
        product = self.session.query(Product).filter(Product.id == product_id).first()
        if not product:
            return None
        
        self.session.delete(product)
        self.session.flush()
        return product.as_dict()
    
        
        