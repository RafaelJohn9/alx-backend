#!/usr/bin/env python3
"""
a simple api
"""
from flask import Flask, render_template, g, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    it is used to get the user
    """
    login_as = request.args.get("login_as")
    if login_as and int(login_as):
        return users.get(int(login_as), None)


class Config:
    """
    this is a class that configures
    app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.before_request
def before_request():
    """
    gets the user id
    """
    g.user = get_user()


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
        return user['locale']
    return request.accept_languages.best_match(['en', 'fr'])


@app.route('/')
def homepage():
    """
    home route
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(debug=True)
