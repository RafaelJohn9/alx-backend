#!/usr/bin/env python3
"""Use request accept_languages to determine the best match"""
from flask import Flask, request, render_template, g
from flask_babel import Babel, format_datetime, _
import pytz
from datetime import datetime


app = Flask(__name__)
babel = Babel(app)


class Config:
    """config available languages in our app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """gets the user from the dict if available"""
    login_as = request.args.get('login_as')
    if login_as and int(login_as) in users:
        return users[int(login_as)]
    else:
        return None


@app.before_request
def before_request():
    """g user is being set"""
    g.user = get_user()


@babel.localeselector
def get_locale():
    """ detect if the incoming request contains locale argument"""
    if 'locale' in request.args:
        locale = request.args.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale

    if g.user:
        local_user = g.user['locale']
        if local_user in Config.LANGUAGES:
            return local_user

    user_locale = request.accept_languages.best_match(app.config['LANGUAGES'])
    if user_locale:
        return user_locale

    return Config.BABEL_DEFAULT_LOCALE


@babel.timezoneselector
def get_timezone():
    # Check if the timezone is specified in the URL parameters
    if 'timezone' in request.args:
        timezone = request.args.get('timezone')
        try:
            pytz.timezone(timezone)
            return timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    # Check if the user has a preferred timezone set
    if g.user and 'timezone' in g.user:
        timezone = g.user['timezone']
        try:
            pytz.timezone(timezone)
            return timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    # Default to UTC if no valid timezone is found
    return 'UTC'


def get_current_time():
    if g.user and 'timezone' in g.user:
        user_timezone = g.user['timezone']
        try:
            timezone = pytz.timezone(user_timezone)
        except pytz.exceptions.UnknownTimeZoneError:
            timezone = pytz.timezone('UTC')
    else:
        timezone = pytz.timezone('UTC')

    current_time = datetime.now(timezone)
    return current_time

@app.route('/')
def index():
    current_time = get_current_time()
    formatted_time = format_datetime(current_time, "medium")
    message = _('current_time_is', current_time=formatted_time)
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)