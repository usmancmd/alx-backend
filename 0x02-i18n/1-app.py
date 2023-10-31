#!/usr/bin/env python3
"""Basic Flask app setup"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

class Config(object):
    """config class"""
    LANGUAGES = ['en', 'es']


app.config.from_object(Config)

@babel.localeselector
def get_locale():
    """Set the default locale"""
    return "en"

@app.route("/")
def index_page() -> str:
    """index route"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
