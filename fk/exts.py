from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
redis_client = FlaskRedis()
jwt = JWTManager()
