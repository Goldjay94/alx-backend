#!/usr/bin/env python3
""" 6-app module"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


def get_locale():
    """ get_locale """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')
    locale = request.headers.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


class Config():
    """ Config class for Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = LANGUAGES[0]
    BABEL_DEFAULT_TIMEZONE = "UTC"
    # BABEL_LOCALE_SELECTOR = get_locale


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)
# Either define it this like  or with it defined in the
# config object
# babel.init_app(app, locale_selector=get_locale)
babel.init_app(app, locale_selector=get_locale)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(login_as):
    """ get_user """
    if login_as and int(login_as) in users:
        return users.get(int(login_as))
    return None


@app.before_request
def before_request():
    """ before_request """
    user = get_user(request.args.get('login_as'))
    if user:
        g.user = user
    else:
        g.user = None


@app.route('/')
def index():
    """ index """
    return render_template("6-index.html", get_locale=get_locale)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
