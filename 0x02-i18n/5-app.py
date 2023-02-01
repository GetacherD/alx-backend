#!/usr/bin/env python3
"""
flask babel demo i18n
"""

from flask import Flask, g, render_template, request
from flask_babel import Babel, _


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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


def get_user():
    key = request.args.get("login_as")
    if not key and int(key) not in list(users.keys()):
        return None
    return users.get(int(key))


@app.before_request
def before_request():
    g.user = None
    user = get_user()
    if user:
        g.user = user


@app.route("/")
def index():
    """ index page """
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run()
