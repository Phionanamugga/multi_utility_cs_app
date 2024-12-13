'''from flask import Flask
from flask import Blueprint
from app.routes.auth import auth_bp
from app.routes.profile import profile_bp


def create_app():
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(profile_bp, url_prefix='/profile')
    
    return app

'''
from app.routes.auth import auth_bp
from app.routes.profile import profile_bp

# Optionally, you can consolidate the blueprints in a list for easy access
blueprints = [auth_bp, profile_bp]

