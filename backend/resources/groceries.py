
from flask import Blueprint, g, request
from flask_jwt_extended import jwt_required
from services.base_service import get_service
from services.groceries_service import GroceriesService
from utils.response_wrapper import make_response

groceries_bp = Blueprint('groceries', __name__)
#TODO: Nice to have: Web Socket for real-time updates

@groceries_bp.route("/groceries", methods=['GET'])
@jwt_required()
def get_grocery_list():
    #TODO: Add pagination and filtering
    """
    Returns a list of groceries.
    """
    groceries_service = get_service(GroceriesService)
    family_id = request.args.get('familyId', type=int)
    if family_id is None:
        return make_response(data=None, message="Family ID is required", status_code=400)   
    
    return make_response(groceries_service.get_all_groceries(family_id))

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

@groceries_bp.route("/groceries/<int:id>", methods=['PUT'])
@jwt_required()
def update_grocery_list(id:int):
    """
    Update grocery list.
    """
    groceries_service = get_service(GroceriesService)
    grocery_list = g.get('snake_case_json', {})
    if not grocery_list:
        return make_response(data=None, message="Invalid input", status_code=400)
    
    added_list = groceries_service.update_grocery_list(id, grocery_list)
    return make_response(data=added_list, message="Grocery list updated successfully", status_code=201)


@groceries_bp.route("/groceries/items/<int:item_id>", methods=['PATCH'])
@jwt_required()
def update_items_status(item_id:int):
    """
    Update grocery list.
    """
    groceries_service = get_service(GroceriesService)
    grocery_list_item = g.get('snake_case_json', {})
    if not grocery_list_item:
        return make_response(data=None, message="Invalid input", status_code=400)
    
    added_list = groceries_service.update_item(item_id, grocery_list_item)
    return make_response(data=added_list, message="Grocery list updated successfully", status_code=201)

@groceries_bp.route("/groceries/<int:id>", methods=['DELETE'])
@jwt_required()
def delete_grocery_list(id:int):
    """
    delete grocery list.
    """
    groceries_service = get_service(GroceriesService)
    if not id:
        return make_response(data=None, message="Invalid input", status_code=400)
    
    added_list = groceries_service.delete_grocery_list(id)
    return make_response(data=added_list, message="Grocery list added successfully", status_code=201)