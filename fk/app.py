from flask import Flask
from flask_cors import CORS
import config
from exts import db
from blueprints.users import bp as auth_bp

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config.from_object(config)
app.register_blueprint(auth_bp)
#db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
