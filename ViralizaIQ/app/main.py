from flask import Flask, request, redirect, url_for, render_template, session, jsonify
from app.config import config
from utils.api_client import InstagramAPI
import requests

app = Flask(__name__)
app.secret_key = config.SECRET_KEY
app.config.from_object(config)

@app.route('/')
def home():
    return render_template('dashboard.html')

@app.route('/analytics')
def analytics():
    if 'access_token' not in session:
        return redirect(url_for('instagram_login'))
    return render_template('analytics.html')

@app.route('/settings')
def settings():
    if 'access_token' not in session:
        return redirect(url_for('instagram_login'))
    return render_template('settings.html')

@app.route('/instagram_login')
def instagram_login():
    instagram_login_url = (
        "https://api.instagram.com/oauth/authorize"
        "?client_id={app_id}"
        "&redirect_uri={redirect_uri}"
        "&scope=user_profile,user_media"
        "&response_type=code"
    ).format(
        app_id=config.INSTAGRAM_APP_ID,
        redirect_uri=config.REDIRECT_URI
    )
    return redirect(instagram_login_url)

@app.route('/instagram_auth_redirect')
def instagram_auth_redirect():
    code = request.args.get("code")
    if code:
        token_url = "https://api.instagram.com/oauth/access_token"
        response = requests.post(token_url, data={
            "client_id": config.INSTAGRAM_APP_ID,
            "client_secret": config.INSTAGRAM_APP_SECRET,
            "grant_type": "authorization_code",
            "redirect_uri": config.REDIRECT_URI,
            "code": code
        })

        if response.status_code == 200:
            access_token = response.json().get("access_token")
            session['access_token'] = access_token

            instagram_api = InstagramAPI(access_token=access_token)
            user_info = instagram_api.get_user_profile()
            if user_info:
                session['username'] = user_info.get('username')
            return redirect(url_for('home'))
        else:
            return "Error retrieving access token"
    return "No authorization code provided"

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(port=5000, debug=True)
