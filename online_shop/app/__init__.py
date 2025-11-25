from flask import Flask
import json
import os
def create_app():
    base_dir=os.path.abspath(os.path.dirname(__file__)+ '/..')
    app = Flask(__name__, template_folder=os.path.join(base_dir, 'templates'),
                static_folder=os.path.join(base_dir, 'static'))
        # Load config from JSON file
    config_path = os.path.join(base_dir, 'config.json')
    with open(config_path) as f:
        config = json.load(f)
    app.config.update(config)
    # Set up SQLAlchemy with absolute DB path
    db_path = os.path.abspath(os.path.join(base_dir, config['DB_PATH']))
    # Ensure the DB directory exists so SQLite can create the file
    db_dir = os.path.dirname(db_path)
    if not os.path.exists(db_dir):
        os.makedirs(db_dir, exist_ok=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    from .models import db
    db.init_app(app)

    
    from .routes import bp as routes_bp
    app.register_blueprint(routes_bp)
    return app