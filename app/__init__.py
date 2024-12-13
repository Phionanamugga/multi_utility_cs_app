
from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import and register blueprints
    from app.routes.auth import auth_bp
    from app.routes.profile import profile_bp
    
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(profile_bp, url_prefix="/profile")

    return app

from flask import Flask
from flask import Blueprint
from app.routes.auth import auth_bp
from app.routes.profile import profile_bp

def create_app():
    app = Flask(__name__)

    # App configuration (e.g., secret key, database URI)
    app.config['SECRET_KEY'] = 'your_secret_key'

    # Register Blueprints
    from app.routes.auth import auth_bp
    from app.routes.profile import profile_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(profile_bp, url_prefix='/profile')

    return app
