from flask import Flask, render_template, request, redirect, url_for, session, send_file, abort, Response
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

@app.route('/sitemap.xml', methods=['GET'])
def sitemap():
    # List of static and dynamic URLs
    urls = [
        {'loc': url_for('index', _external=True), 'lastmod': '2025-01-01'},  # Updated from 'home' to 'index'
        {'loc': url_for('aboutus', _external=True), 'lastmod': '2025-01-01'},
        {'loc': 'https://pyinnyarsubuu.khantzay.com/FormalEducation', 'lastmod': '2025-01-01'},
        {'loc': 'https://pyinnyarsubuu.khantzay.com/essential', 'lastmod': '2025-01-01'},
        {'loc': 'https://pyinnyarsubuu.khantzay.com/steam', 'lastmod': '2025-01-01'},
        {'loc': 'https://pyinnyarsubuu.khantzay.com/loginpage', 'lastmod': '2025-01-01'},
        {'loc': 'https://pyinnyarsubuu.khantzay.com/signuppage', 'lastmod': '2025-01-01'},
    ]
    
    # Create sitemap XML
    sitemap_xml = ['<?xml version="1.0" encoding="UTF-8"?>']
    sitemap_xml.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    for url in urls:
        sitemap_xml.append(f"<url><loc>{url['loc']}</loc><lastmod>{url['lastmod']}</lastmod></url>")
    sitemap_xml.append('</urlset>')
    
    # Return XML response
    response = Response("\n".join(sitemap_xml), mimetype='application/xml')
    return response

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
    app.run(host='0.0.0.0', port=3000, debug=True)
