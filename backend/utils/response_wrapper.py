from flask import jsonify
import inflection

def make_response(data=None, message="", success=True, status_code=200):
    response = {
        "success": success,
        "message": message,
        "data": data
    }
    return jsonify(response), status_code

def to_camel_case(data):
    if isinstance(data, dict):
        return {inflection.camelize(k, False): to_camel_case(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [to_camel_case(item) for item in data]
    return data

def to_snake_case(data):
    if isinstance(data, dict):
        return {inflection.underscore(k): to_snake_case(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [to_snake_case(item) for item in data]
    return data