from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    from app.routes import main_routes, lead_routes, tree_routes, vendor_routes, admin_routes
    app.register_blueprint(main_routes)
    app.register_blueprint(lead_routes)
    app.register_blueprint(tree_routes)
    app.register_blueprint(vendor_routes)
    app.register_blueprint(admin_routes)

    return app
