from flask import Blueprint, render_template
from routes.auth import require_auth

formalEducation_bp = Blueprint("formalEducation", __name__)

# Formal education pages
@formalEducation_bp.route("/FormalEducation")
def formaleducation():
    return render_template("formalEducationGrade.html")

@formalEducation_bp.route("/FormalEducation/Subjects")
def FormalEducationSubjects():
    return render_template("FormalEducation.html")

@formalEducation_bp.route("/FormalEducation/Subjects/myanmar")
def myanmar():
    return render_template("myan.html")

@formalEducation_bp.route("/FormalEducation/Subjects/myanmar/yaythalpyazat")
@require_auth
def yaythalpyazat():
    return render_template("yaythalpyazat.html")

@formalEducation_bp.route("/FormalEducation/Subjects/myanmar/mahawthahtar")
@require_auth
def mahawthahtar():
    return render_template("mahawthadar.html")

@formalEducation_bp.route("/FormalEducation/Subjects/science")
@require_auth
def science():
    return render_template("science.html")