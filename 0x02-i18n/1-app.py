#!/usr/bin/env python3
""" 1-app module """
from flask import Flask, render_template
from flask_babel import Babel


class Config():
    """ Config class for Babel"""
    LANGUAGE = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = LANGUAGE[0]
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@app.route('/')
def index():
    """ index """
    return render_template("1-index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
