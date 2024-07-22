import os

class Config:
    RABBITMQ_URL = os.getenv('RABBITMQ_URL', 'amqp://guest:guest@rabbitmq:5672/')
    REDIS_URL = os.getenv('REDIS_URL', 'redis://redis:6379/0')
    USER_SERVICE_URL = os.getenv('USER_SERVICE_URL', 'http://user-service:5027')
