#!/usr/bin/env python3
"""
flask babel demo i18n
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """ babel config class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ get locale """
    lang = request.args.get("locale")
    if lang and lang in app.config["LANGUAGES"]:
        return lang
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index():
    """ index page """
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run()