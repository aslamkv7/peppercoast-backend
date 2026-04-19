from flask import Blueprint
from utils.response import success_response

health_bp = Blueprint("health", __name__)


@health_bp.route("/health", methods=["GET"])
def health_check():
    return success_response(
        message="PepperCoast API healthy",
        data={"status": "ok"}
    )