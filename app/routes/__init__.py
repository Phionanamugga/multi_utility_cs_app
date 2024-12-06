from flask import Blueprint
from app.routes.auth import auth_bp
from app.routes.profile import profile_bp


def register_routes(app):
    app.register_blueprint(auth_bp, url_prefix='/auth')

def register_routes(app):
    app.register_blueprint(profile_bp, url_prefix='/profile')

