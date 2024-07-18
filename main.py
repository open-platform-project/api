from flask import Flask
from flask import session

app = Flask(__name__)


# Base information about the API

@app.route('/')
def index():  # TODO: should give information about api version and enabled features and paths
    return 'Not yet implemented'


# Account authentication

@app.route('/auth/login', methods=['GET', 'POST'])
def login():  # TODO (LOGIN)
    return 'Not yet implemented'


@app.route('/auth/logout', methods=['GET'])
def logout():  # TODO (LOGOUT)
    return 'Not yet implemented'


@app.route('/auth/check', methods=['GET'])
def check_user_information_self():  # TODO (GET LOGGED IN USER INFORMATION)
    return 'Not yet implemented'
