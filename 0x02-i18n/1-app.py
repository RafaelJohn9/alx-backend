#!/usr/bin/env python3
"""instantiate the Babel object in your app"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """config available languages in our app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel.init_app(app)


@app.route('/')
def hello_world():
    """renders 1-index.html"""
    return render_template("1-index.html")


if __name__ == '__main__':
    app.run()
