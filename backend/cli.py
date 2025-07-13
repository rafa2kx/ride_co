import click
from flask.cli import with_appcontext
from models import GroceryList
from extension import db
from models.category import Category
from models.family import Family
from models.grocery_list_item import GroceryListItem
from models.product import Product
from models.user import User

@click.command(name="seed")
@with_appcontext
def seed():
    family = Family(name="Smith Family", description="Weekly groceries for the Smith family")
    db.session.add(family)  
    user = User(username="johnsmith", email='johnsmith@mail.com', family=family)
    db.session.add(user)
    fruits = Category(name="Fruits")
    db.session.add(fruits)
    vegetables = Category(name="Vegetables")
    db.session.add(vegetables)
    products = [Product(name="Apples", price=0.5, category=fruits), 
                Product(name="Bananas", price=0.3, category=fruits),
                Product(name="Carrots", price=0.2, category=vegetables),
                Product(name="Broccoli", price=0.4, category=vegetables)]
    db.session.add_all(products)
    weekly = GroceryList(name="Weekly Shopping", family=family, description="Weekly grocery list for the Smith family")
    db.session.add(weekly)
    items = [GroceryListItem(quantity=5, grocery_list=weekly, product=products[0]), 
             GroceryListItem(quantity=3, grocery_list=weekly, product=products[1]),
             GroceryListItem(custom_name='Protein Shakes', quantity=2, grocery_list=weekly, product=products[2])]
    db.session.add_all(items)

    
    db.session.commit()
    print("Dummy data inserted.")