from flask import Flask
from config import Config
from flask_restful import Api


def create_app(config_class=Config):
    app = Flask(__name__, static_url_path="")
    app.config.from_object(Config)

    from app.auth import bp as auth_bp

    app.register_blueprint(auth_bp, url_prefix="/api/v1")

    return app
