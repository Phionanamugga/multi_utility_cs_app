class Config:
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 587
    SMTP_USERNAME = 'your_email@gmail.com'
    SMTP_PASSWORD = 'your_email_password'
    SMTP_FROM_EMAIL = 'no-reply@multiutility.com'

class Config:
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SMS_API_URL = 'https://api.smsprovider.com/send'
    SMS_API_KEY = 'your_sms_api_key'
    SMS_SENDER_ID = 'MULTIUTIL'

