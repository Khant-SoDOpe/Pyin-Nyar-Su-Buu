from flask import Blueprint, render_template
from routes.auth import require_auth

essential_bp = Blueprint("essential", __name__)

@essential_bp.route("/essential")
def essentialpage():
    return render_template("essential.html")

@essential_bp.route("/essential/earH")
@require_auth
def earH():
    return render_template("earHealth.html")

@essential_bp.route("/essential/literature")
@require_auth
def essentialliterature():
    return render_template("EssentialLiterature.html")

@essential_bp.route("/essential/sexeducation")
@require_auth
def essentialsexeducation():
    return render_template("EssentialSexEducation.html")
