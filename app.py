from flask import Flask, render_template, request, redirect, url_for, session, send_file, abort
from functools import wraps
from dotenv import load_dotenv
import os

from routes.essential import essential_bp
from routes.steam import steam_bp
from routes.formalEducation import formalEducation_bp

from routes.auth import require_auth, auth_bp
from routes.google import google_bp

# Initialize Flask app
app = Flask(__name__)
load_dotenv()
app.secret_key = os.getenv("SECRET_KEY")

# Routes

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/HIC")
@require_auth
def hic():
    return render_template("hear.html")

@app.route("/VIC")
@require_auth
def vic():
    return render_template("visual.html")

@app.route("/aboutus")
def aboutus():
    return render_template("about.html")

# Essential pages
app.register_blueprint(essential_bp)

# STEAM pages
app.register_blueprint(steam_bp)

app.register_blueprint(auth_bp)

app.register_blueprint(google_bp)

app.register_blueprint(formalEducation_bp)

# Run the app
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=3000)
