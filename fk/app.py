from flask import Flask
from flask_cors import CORS
import config
from exts import db, redis_client
from models import Admin
from blueprints.users import bp as user_bp
from flask_migrate import Migrate

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)
app.config.from_object(config)
app.register_blueprint(user_bp)
db.init_app(app)
redis_client.init_app(app, decode_responses=True)
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True)
