import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()


def create_app(key: str):
    # Configure app
    app = Flask(__name__)
    app.config.from_object('instance.config.'+key)

    db.init_app(app)
    migrate.init_app(app, db)

    # Ensure the instance directory exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    with app.app_context():
        from app.blueprints import api
        app.register_blueprint(api)

    return app
