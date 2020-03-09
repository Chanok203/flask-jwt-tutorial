from flask import Flask
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__, static_url_path="")
    app.config.from_object(Config)

    from app.api import bp as api_bp

    app.register_blueprint(api_bp, url_prefix="/")

    return app
