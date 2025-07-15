
from sqlalchemy import and_, select
from interfaces import IService
from models.grocery_list_item import GroceryListItem
from models.product import Product
from repositories.base_repository import BaseRepository
from models.grocery_list import GroceryList

class ProductsRepository(BaseRepository):
    
    def get_all_products(self):
        products = self.session.query(Product).all()
        return [product.as_dict() for product in products]
    
    def add_product(self, product: dict):
        """Add a new Product."""
        new_product = Product(**product)
        self.session.add(new_product)
        self.session.flush()
        return new_product.as_dict()
    
        
        