from flask import Blueprint
from app.blueprints.users import users

api = Blueprint('api', __name__, url_prefix='/api/v1')
api.register_blueprint(users)
