import os
from flask import Flask
from flask import Blueprint
from app.routes.auth import auth_bp
from app.routes.profile import profile_bp
from app.models import User
from flask_sqlalchemy import SQLAlchemy # type: ignore
from flask_migrate import Migrate
from app.extensions import db


# Initialize the database object
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name=None):
    app = Flask(__name__, instance_relative_config=True)

    # App configuration (e.g., secret key, database URI)
    app.config['SECRET_KEY'] = 'your_secret_key'
    # Configure the app (add your configuration settings here)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'  # Example URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Load configuration from the instance folder
    app.config.from_object('config.default_config')  # Default config
    app.config.from_pyfile('config.py', silent=True)  # Override with instance config

# Optional: Select config by name (e.g., from environment variables)
    if config_name:
        app.config.from_object(f'instance.config.{config_name}')

    # Initialize db with the app
    db.init_app(app)
    migrate.init_app(app, db)


    app.register_blueprint(auth_bp, url_prefix='/auth')
    print("auth_bp registered")  # Debug print
    app.register_blueprint(profile_bp, url_prefix='/profile')
    print("profile_bp registered")  # Debug print
    app.register_blueprint(user_bp)
    print("profile_bp registered")  # Debug print
    print("App creation complete.")  # Debug print 
    return app








