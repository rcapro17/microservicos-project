import redis
from flask import Flask
from config import Config
from models import db
from routes import user_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
app.register_blueprint(user_bp)

redis_client = redis.StrictRedis.from_url(Config.REDIS_URL)

# Create a variable to keep track of whether the tables have been created
tables_created = False

@app.before_request
def create_tables():
    global tables_created
    if not tables_created:
        db.create_all()
        tables_created = True
