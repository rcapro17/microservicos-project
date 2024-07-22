from flask import Flask
from routes import task_bp
from config import Config
import redis

app = Flask(__name__)
app.config.from_object(Config)

redis_client = redis.StrictRedis.from_url(Config.REDIS_URL)
app.register_blueprint(task_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port="5027")
