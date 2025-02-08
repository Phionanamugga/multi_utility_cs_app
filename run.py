from flask_migrate import Migrate
from flask import Flask, jsonify, request, render_template
#from app.models.user import User
#from app.routes import auth, profile, utility, email_service, phone_service
#from app.utils import hashers, response, validators
#from app.config import Config
#from app.database import db

# Initialize Flask app
app = Flask(__name__, template_folder='app/templates')

# Load configuration
#app.config.from_object(Config)

# Initialize database
#db.init_app(app)

# Register Blueprints (modularize your routes)
#app.register_blueprint(auth.bp, url_prefix="/auth")
#app.register_blueprint(profile.bp, url_prefix="/profile")
#app.register_blueprint(utility.bp, url_prefix="/utility")
#app.register_blueprint(email_service.bp, url_prefix="/email")
#app.register_blueprint(phone_service.bp, url_prefix="/phone")

@app.route('/')
def home():
    return render_template('index.html')
    #return "Hello, Flask!"

# Health check route
#@app.route("/health", methods=["GET"])
#def health_check():
    #return jsonify({"status": "ok", "message": "Service is running"}), 200

# Error handling (optional)
#@app.errorhandler(404)
#def not_found(error):
    #return jsonify({"error": "Resource not found"}), 404

#@app.errorhandler(500)
#def server_error(error):
    #return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    # Run the app on localhost, port 8000
    app.run(host="0.0.0.0", port=8000, debug=True)









