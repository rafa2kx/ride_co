from repositories.groceries_repository import GroceriesRepository
from services.base_service import BaseService


class GroceriesService(BaseService):
    def __init__(self):
        super().__init__()
        self.groceries_repository = self._get_repository(GroceriesRepository)

    def get_all_groceries(self):
        """Fetch all grocery lists."""
        return self.groceries_repository.get_all_groceries()
    
    def add_grocery_list(self, grocery_list: dict):
        """Add a new grocery list."""
        return self.groceries_repository.add_grocery_list(grocery_list)