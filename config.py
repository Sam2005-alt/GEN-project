import os

class Config:
    ENV = os.getenv('ENV', 'development')
    DEBUG = os.getenv('DEBUG', 'True') == 'True'
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///database.db')
    # Add other configuration variables here
