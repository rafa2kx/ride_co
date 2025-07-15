from repositories.groceries_repository import GroceriesRepository
from services.base_service import BaseService


class GroceriesService(BaseService):
    def __init__(self):
        super().__init__()
        self.groceries_repository = self._get_repository(GroceriesRepository)

    def get_all_groceries(self, family_id: int):
        """Fetch all grocery lists."""
        return self.groceries_repository.get_all_groceries(family_id)
    
    def add_grocery_list(self, grocery_list: dict):
        """Add a new grocery list."""
        return self.groceries_repository.add_grocery_list(grocery_list)
    
    def update_grocery_list(self, id:int, grocery_list: dict):
        """Update grocery list."""
        return self.groceries_repository.update_grocery_list(id, grocery_list)
    
    def update_item(self, item_id: int, grocery_list_item: dict):
        """Update grocery list item status."""
        return self.groceries_repository.update_item(item_id, grocery_list_item)
    
    def delete_grocery_list(self, id: int):
        """Delete grocery list."""
        return self.groceries_repository.delete_grocery_list(id)