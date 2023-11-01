#!/usr/bin/env python3
"""Basic Flask app setup"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union, Dict

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """get_loacle"""
    if "locale" in request.args:
        locale_request = request.args["locale"]
        if locale_request in app.config["LANGUAGES"]:
            return locale_request

    request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user() -> Union[Dict, None]:
    """get user by its id"""
    if 'login_as' not in request.args.keys():
        return None

    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))


@app.before_request
def before_request():
    """runs before any request"""
    user = get_user()
    g.user = user


@app.route("/")
def index_page() -> str:
    """index route"""
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
