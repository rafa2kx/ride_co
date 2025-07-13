from flask import Flask, jsonify, request, g
from flask_migrate import Migrate
from cli import seed
from config import Config
from resources.groceries import groceries_bp
from resources.authentication import auth_bp
from extension import db, jwt
from config import Config
from utils.response_wrapper import to_camel_case, to_snake_case

migrate = Migrate()
def create_app():
    app = Flask(__name__)
    """Initialize the Flask application with configurations and extensions."""
    app.config.from_object(Config)
    db.init_app(app)
    jwt.init_app(app)
    Migrate(app, db)
    app.cli.add_command(seed)
    
    """Register blueprints for the application."""
    app.register_blueprint(groceries_bp)
    app.register_blueprint(auth_bp)
    
    return app

app = create_app()

@app.before_request
def convert_request_json_to_snake_case():
    if request.is_json:
        g.snake_case_json = to_snake_case(request.get_json())

@app.before_request
def start_transaction():
    if request.method in ['POST', 'PUT', 'DELETE']:
        db.session.begin()

@app.after_request
def convert_response_to_camel_case(response):
    if response.is_json:
        original_data = response.get_json()
        camel_case_data = to_camel_case(original_data)
        response.set_data(jsonify(camel_case_data).get_data())
    return response

@app.teardown_request
def end_transaction(exception=None):
    if request.method in ['POST', 'PUT', 'DELETE']:
        if exception:
            db.session.rollback()
            print("Rolled back due to exception:", exception)
        else:
            try:
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                print("Rolled back due to DB error:", e)

# @app.errorhandler(Exception)
# def handle_exception(e):
#     from utils.response_wrapper import make_response
#     return make_response(
#         data=None,
#         message=str(e),
#         success=False,
#         status_code=500
#     )




