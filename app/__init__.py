import os
from flask import Flask
from .db import close_db, init_db

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get("STAFFTRACK_SECRET", "change-this-for-production"),
        DATABASE=os.path.join(app.instance_path, "stafftrack.sqlite"),
    )
    os.makedirs(app.instance_path, exist_ok=True)
    from . import db
    app.teardown_appcontext(close_db)
    with app.app_context():
        init_db()
    from .routes import bp
    app.register_blueprint(bp)
    return app
