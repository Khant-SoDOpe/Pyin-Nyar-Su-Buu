from flask import Blueprint, redirect, session , render_template , abort, request
from google_auth_oauthlib.flow import Flow
import os
import pathlib
import requests
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
from google.oauth2 import id_token
import google.auth.transport.requests
from dotenv import load_dotenv

google_bp = Blueprint('google', __name__)

load_dotenv()

# Google OAuth configuration
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "../client_secret.json")
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="pyinnyarsubuu.onrneder.com/callback"
)

@google_bp.route("/googleLogin")
def googleLogin():
    # Initiates Google OAuth login flow
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    return redirect(authorization_url)

@google_bp.route("/callback")
def callback():
    # OAuth callback logic
    flow.fetch_token(authorization_response=request.url)

    if not session["state"] == request.args["state"]:
        abort(500)  # State does not match!

    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=GOOGLE_CLIENT_ID
    )

    session['authenticated'] = True
    condition = True
    letter = 'Successfully Login!'
    return render_template('index.html', contact=letter, condition=condition)
