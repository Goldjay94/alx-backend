#!/usr/bin/env python3
"""4-app module"""


from flask import Flask, render_template, request
from flask_babel import Babel

def get_locale():
    """ get_locale """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        print(locale)
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


@app.route('/')
def index():
    """ index """
    return render_template("4-index.html", get_locale=get_locale)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True
