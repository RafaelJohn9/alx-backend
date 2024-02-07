#!/usr/bin/env python3
"""
a simple api
"""
from flask import Flask, render_template, g, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    this is a class that configures
    app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    uses the local lang of the user settings
    """
    requested_locale = request.args.get('locale')

    if requested_locale and requested_locale in app.config['LANGUAGES']:
        return requested_locale

    user = getattr(g, 'user', None)
    if user is not None:
        return user.locale
    return request.accept_languages.best_match(['en', 'fr'])


@app.route('/')
def homepage():
    """
    home route
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)
