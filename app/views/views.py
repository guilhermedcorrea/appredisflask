from flask import Blueprint


view_bp = Blueprint("index", __name__)


@view_bp.route("/")
def home():
    return "index"


