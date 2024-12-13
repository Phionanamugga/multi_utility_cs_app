
from flask import Flask
from flask import Blueprint
from app.routes.auth import auth_bp
from app.routes.profile import profile_bp
from app.routes.user import user_bp

def create_app():
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(profile_bp, url_prefix='/profile')
    app.register_blueprint(user_bp, url_prefix='/user')

    return app

