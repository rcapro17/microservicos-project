import os

class Config:
    # Ensure the DATABASE_URL environment variable includes the correct port number
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:testpass@localhost:5433/user_service')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REDIS_URL = os.getenv('REDIS_URL', 'redis://redis:6379/0')
