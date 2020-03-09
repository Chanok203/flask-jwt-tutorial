from app.api import bp
from flask import jsonify


@bp.route("/", methods=["GET", "POST"])
@bp.route("/index", methods=["GET", "POST"])
def index():
    return "API is running normally."

