from flask import Blueprint, render_template
from routes.auth import require_auth

steam_bp = Blueprint("steam", __name__)

@steam_bp.route("/steam")
def steam():
    return render_template("steam.html")

@steam_bp.route("/steam/Sci")
def steamSci():
    return render_template("steamScience.html")

@steam_bp.route("/steam/Sci/PHOSIS")
@require_auth
def PHOSIS():
    return render_template("photosynthesis.html")