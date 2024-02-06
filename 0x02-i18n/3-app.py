#!/usr/bin/env python3
"""Use request.accept_languages to determine the best match"""
from flask import Flask, request, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """config available languages in our app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Use request.accept_languages to determine the best match"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def hello_world():
    """renders 3-index.html"""
    return render_template("3-index.html")


if __name__ == '__main__':
    app.run()
