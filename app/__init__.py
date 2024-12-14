from flask import Flask
#from flask import Blueprint
#from app.routes.auth import auth_bp
#from app.routes.profile import profile_bp
from flask_sqlalchemy import SQLAlchemy # type: ignore
from flask_migrate import Migrate

# Initialize the database object
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # App configuration (e.g., secret key, database URI)
    app.config['SECRET_KEY'] = 'your_secret_key'
    # Configure the app (add your configuration settings here)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'  # Example URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize db with the app
    db.init_app(app)

    # Register Blueprints
    from app.routes.auth import auth_bp
    from app.routes.profile import profile_bp
    from app.routes.user import user_bp
    

    app.register_blueprint(auth_bp, url_prefix='/auth')
    print("auth_bp registered")  # Debug print
    app.register_blueprint(profile_bp, url_prefix='/profile')
    print("profile_bp registered")  # Debug print
    app.register_blueprint(user_bp)
    print("profile_bp registered")  # Debug print
    print("App creation complete.")  # Debug print 
    return app








