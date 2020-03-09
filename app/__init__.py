from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


from config import Config

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()


def create_app(config_class=Config):
    app = Flask(__name__, static_url_path="")
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    @jwt.token_in_blacklist_loader
    def check_if_token_in_blacklist(decrypted_token):
        from app.auth import models as auth_models  # isort:skip

        jti = decrypted_token["jti"]
        return auth_models.RevokedTokenModel.is_jti_blacklisted(jti)

    from app.auth import bp as auth_bp

    app.register_blueprint(auth_bp, url_prefix="/api/v1")

    return app


from app.auth import models as auth_models  # isort:skip
