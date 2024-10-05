from flask import Blueprint, render_template, request, redirect, url_for, session
from functools import wraps
import redis
import os
from dotenv import load_dotenv

auth_bp = Blueprint('auth', __name__)
load_dotenv()


# Redis configuration
# r = redis.Redis(
#     host= os.getenv("REDIS_HOST"),
#     port= os.getenv("REDIS_PORT"),
#     password= os.getenv("REDIS_PASSWORD")
# )

r = redis.from_url(os.environ['REDIS_URL'])

# Decorator for requiring authentication
def require_auth(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if 'authenticated' in session:
            return view(*args, **kwargs)
        return redirect(url_for('auth.loginpage'))
    return wrapped_view

# Login route
@auth_bp.route("/login", methods=["POST"])
def login():
    # User login logic
    email = request.form.get("Email")
    password = request.form.get("Password")

    # Retrieve user data from Redis
    user_data = r.hgetall(email)

    if user_data:
        if user_data[b'Password'].decode('utf-8') == password:
            # Set the user as authenticated in the session
            session['authenticated'] = True
            condition = True
            letter = 'Successfully Login!'
            return render_template('index.html', contact=letter, condition=condition)
        else:
            condition = "error"
            letter = 'Please Check Your Password!'
            return render_template('login.html', contact=letter, condition=condition)
    else:
        condition = "error"
        letter = 'No Account Found!'
        return render_template('login.html', contact=letter, condition=condition)

# Signup route
@auth_bp.route("/signup", methods=["POST"])
def signup():
    # User signup logic
    name = request.form.get("Name")
    email = request.form.get("Email")
    password = request.form.get("Password")
    password2 = request.form.get("Password2")

    if password == password2:
        # Check if the user already exists
        if r.exists(email):
            condition = True
            letter = "Already Have an Account!"
            return render_template('signup.html', contact=letter, condition=condition)

        # Store user data in Redis
        user_data = {
            'Name': name,
            'Email': email,
            'Password': password,
            'withgoogle': 0  # Convert boolean to integer
        }
        r.hmset(email, user_data)
        condition = "success"
        letter = "Account Successfully Created!"
        return render_template('login.html', contact=letter, condition=condition)
    else:
        condition = True
        letter = "Please Check Your Confirm Password!"
        return render_template('signup.html', contact=letter, condition=condition)


# Logout route
@auth_bp.route("/logout")
@require_auth
def logout():
    # Logout logic 
    session.pop('authenticated', None)
    return redirect(url_for('auth.loginpage'))

# Login page route
@auth_bp.route("/loginpage")
def loginpage():
    return render_template("login.html")

# Signup page route
@auth_bp.route("/signuppage")
def signuppage():
    return render_template("signup.html")
