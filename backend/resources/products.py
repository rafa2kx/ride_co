
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
    family_id = request.args.get('familyId', type=int)
    products_service = get_service(ProductsService)
    return make_response(products_service.get_all_products(family_id))    

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

@products_bp.route("/products/<int:id>", methods=['PUT'])
@jwt_required()
def update_product(id:int):
    """
    Update grocery list.
    """
    products_service = get_service(ProductsService)
    product = g.get('snake_case_json', {})
    if not product:
        return make_response(data=None, message="Invalid input", status_code=400)
    
    updated_product = products_service.update_product(id, product)
    return make_response(data=updated_product, message="Product updated successfully", status_code=200)


@products_bp.route("/products/<int:id>", methods=['DELETE'])
@jwt_required()
def delete_product(id:int):
    """
    delete product.
    """
    if not id:
        return make_response(data=None, message="Invalid input", status_code=400)
    products_service = get_service(ProductsService)
    deleted_product = products_service.delete_product(id)
    return make_response(data=deleted_product, message="Product deleted successfully", status_code=200)
