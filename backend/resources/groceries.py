
from flask import Blueprint, g, request
from flask_jwt_extended import jwt_required
from services.base_service import get_service
from services.groceries_service import GroceriesService
from utils.response_wrapper import make_response

groceries_bp = Blueprint('groceries', __name__)

@groceries_bp.route("/groceries", methods=['GET'])
@jwt_required()
def get_groucery_list():
    """
    Returns a list of groceries.
    """
    groceries_service = get_service(GroceriesService)
    return make_response(groceries_service.get_all_groceries())

@groceries_bp.route("/groceries", methods=['POST'])
@jwt_required()
def add_grocery_list():
    """
    Adds a new grocery list.
    """
    groceries_service = get_service(GroceriesService)
    grocery_list = g.get('snake_case_json', {})
    if not grocery_list:
        return make_response(data=None, message="Invalid input", status_code=400)
    
    added_list = groceries_service.add_grocery_list(grocery_list)
    return make_response(data=added_list, message="Grocery list added successfully", status_code=201)