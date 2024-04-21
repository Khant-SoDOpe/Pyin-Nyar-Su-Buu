from main import app  # Assuming your Flask application instance is named 'app' in main.py

if __name__ == "__main__":
    app.secret_key = "handsomeKhant"
    app.run(host='0.0.0.0', port=3000)