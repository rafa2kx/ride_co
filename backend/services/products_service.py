from repositories.products_repository import ProductsRepository
from services.base_service import BaseService


class ProductsService(BaseService):
    def __init__(self):
        super().__init__()
        self.products_repository = self._get_repository(ProductsRepository)

    def get_all_products(self):
        """Fetch all products."""
        return self.products_repository.get_all_products()
    
    def add_product(self, product: dict):
        """Add a new Product."""
        return self.products_repository.add_product(product)