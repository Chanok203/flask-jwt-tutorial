from flask import Blueprint
from flask_restful import Api
from app.auth.routes import initialize_routes

bp = Blueprint("auth", __name__)
api = Api(bp)
initialize_routes(api)

from app.auth import routes  # isort:skip
