from flask import Flask, redirect, url_for, session
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.secret_key = 'RANDOM_SECRET_KEY' 
oauth = OAuth(app)

# Example of using Google for OAuth authentication
google = oauth.register(
    name='google',
    client_id='YOUR_GOOGLE_CLIENT_ID',
    client_secret='YOUR_GOOGLE_CLIENT_SECRET',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    client_kwargs={'scope': 'openid profile email'}
)
import os

def add_firewall_rule(ip_address):
    os.system(f"sudo ufw allow from {ip_address}")

def remove_firewall_rule(ip_address):
    os.system(f"sudo ufw delete allow from {ip_address}")

# Example usage
add_firewall_rule('192.168.1.100')
remove_firewall_rule('192.168.1.100')

@app.route('/')
def index():
    return 'Welcome to ID and Firewall Management System'

@app.route('/login')
def login():
    return google.authorize_redirect(url_for('authorize', _external=True))

@app.route('/authorize')
def authorize():
    token = google.authorize_access_token()
    resp = google.parse_id_token(token)
    session['user'] = resp
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    user_info = session.get('user')
    return f'Hello, {user_info["name"]}!'

if __name__ == '__main__':
    app.run(debug=True)

import os

def add_firewall_rule(ip_address):
    os.system(f"sudo ufw allow from {ip_address}")

def remove_firewall_rule(ip_address):
    os.system(f"sudo ufw delete allow from {ip_address}")

# Example usage
add_firewall_rule('192.168.1.100')
remove_firewall_rule('192.168.1.100')
