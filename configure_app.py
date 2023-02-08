
from flask import Flask
from blueprints import main_bp
from core import db

def init(app: Flask) -> Flask:
    db.init_app(app)
    app.register_blueprint(main_bp)
    return app