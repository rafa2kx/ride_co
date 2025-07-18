from repositories.products_repository import ProductsRepository
from services.base_service import BaseService


class ProductsService(BaseService):
    def __init__(self):
        super().__init__()
        self.products_repository = self._get_repository(ProductsRepository)

    def get_all_products(self, family_id:int):
        """Fetch all products."""
        return self.products_repository.get_all_products(family_id)
    
    def add_product(self, product: dict):
        """Add a new Product."""
        return self.products_repository.add_product(product)
    
    def update_product(self, product_id:int, product: dict):
        """Update Product."""
        return self.products_repository.update_product(product_id, product)
    
    def delete_product(self, id: int):
        """Delete Product."""
        return self.products_repository.delete_product(id)