import os

from flask import Flask, render_template, request
from helpers import get_request_token, get_user_data, get_user_repos,get_repo_languages

app = Flask(__name__)

# CLIENT_ID = "3a4e48c4da253d2caa10"
# CLIENT_SECRET = "aa2d753401adee21f841c376065a859af6bdec22"
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html', client_id=CLIENT_ID), 200
    # return 'Hello World!'


@app.route('/callback')
def callback():
    args = request.args
    request_token = args.get('code')
    # CLIENT_ID = os.getenv('CLIENT_ID')
    # CLIENT_SECRET = os.getenv('CLIENT_SECRET')

    access_token = get_request_token(CLIENT_ID, CLIENT_SECRET, request_token)
    user_data = get_user_data(access_token)
    repos_url = user_data['repos_url']
    repos = get_user_repos(repos_url, access_token)
    repos_langs = get_repo_languages(repos,access_token)
    return repos_langs


if __name__ == '__main__':
    app.run()
