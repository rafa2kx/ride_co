
from sqlalchemy import and_, select
from interfaces import IService
from models.grocery_list_item import GroceryListItem
from models.product import Product
from repositories.base_repository import BaseRepository
from models.grocery_list import GroceryList

class GroceriesRepository(BaseRepository):
    
    def get_all_groceries(self):
        """Fetch all grocery lists."""
        lists = self.session.query(GroceryList) \
            .join(GroceryList.items) \
            .outerjoin(GroceryListItem.product) \
            .all()

        result = []
        for grocery_list in lists:
            list_data = self._convert_grocery_list_model_to_dict(grocery_list)
            result.append(list_data)
        return result
    
    def add_grocery_list(self, grocery_list: dict):
        """Add a new grocery list."""
        items = grocery_list.pop('items', [])
        new_list = GroceryList(**grocery_list)
        for item in items:
            new_item = GroceryListItem(**item, grocery_list=new_list)
            self.session.add(new_item)
        self.session.add(new_list)
        self.session.commit()
        return new_list.as_dict()
    
    def update_grocery_list(self, list_id: int, grocery_list: dict):
        """Update an existing grocery list."""
        existing_list = self.session.query(GroceryList).filter(GroceryList.id == list_id).first()
        if not existing_list:
            return None
        list_items = grocery_list.pop('items', [])
        for key, value in grocery_list.items():
            setattr(existing_list, key, value)

        # Update or add items
        existing_items = {item.id: item for item in existing_list.items}
        items_dict = {}
        for item in list_items:
            item_id = item.get('id')
            if item_id:
                items_dict[item_id] = item
                existing_item = existing_items.get(item_id)
                for key, value in item.items():
                    setattr(existing_item, key, value)
            else:
                new_item = GroceryListItem(**item, grocery_list=existing_list)
                self.session.add(new_item)
        
        # Remove items that are no longer in the list
        for item_id in list(existing_items.keys()):
            if item_id not in items_dict:
                self.session.delete(existing_items[item_id])
        

        self.session.commit()
        return existing_list.as_dict()
    
    def get_grocery_list_by_id(self, list_id: int):
        """Fetch a grocery list by its ID."""
        grocery_list = self.session.query(GroceryList) \
            .join(GroceryList.items) \
            .outerjoin(GroceryListItem.product) \
            .filter(GroceryList.id == list_id).first()
        
        if not grocery_list:
            return None
        
        list_data = self._convert_grocery_list_model_to_dict(grocery_list)
        return list_data
    
    def _convert_grocery_list_model_to_dict(self, model: GroceryList) -> dict:
        """Convert a SQLAlchemy model to a dictionary."""
        list_data = model.as_dict()
        items = []
        for item in model.items:
            item_data = item.as_dict()
            if item.product:
                item_data['product'] = item.product.as_dict()
            items.append(item_data)
        list_data["items"] = items
        return list_data
        
        