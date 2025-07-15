
from flask import Blueprint, g, request
from flask_jwt_extended import jwt_required
from services.base_service import get_service
from services.products_service import ProductsService
from utils.response_wrapper import make_response

products_bp = Blueprint('products', __name__)

@products_bp.route("/products", methods=['GET'])
@jwt_required()
def get_all_products():
    """
    Returns a list of all products.
    """
    products_service = get_service(ProductsService)
    return make_response(products_service.get_all_products())    

@products_bp.route("/products", methods=['POST'])
@jwt_required()
def add_grocery_list():
    """
    Adds a new Product.
    """
    products_service = get_service(ProductsService)
    product = g.get('snake_case_json', {})
    if not product:
        return make_response(data=None, message="Invalid input", status_code=400)
    
    new_product = products_service.add_product(product)
    return make_response(data=new_product, message="Product added successfully", status_code=201)
