from app.extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(15), unique=True, nullable=True)
    preferences = db.Column(db.JSON, default={})  # For service preferences (e.g., power, water, ferry)

    def __repr__(self):
        return f'<User {self.name}>'
