#!/usr/bin/env python3
"""
flask babel demo i18n
"""

from flask import Flask, g, render_template, request
from flask_babel import Babel, _
from typing import Union
from pytz import timezone
import pytz
from datetime import datetime


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
def get_locale() -> str:
    """ get locale """
    lang = request.args.get("locale")
    if lang and lang in app.config["LANGUAGES"]:
        return lang
    user = getattr(g, "user", None)
    if user and user.lccale in app.config["LANGUAGES"]:
        return user.locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@babel.timezoneselector
def get_timezone() -> str:
    """ Get time zone """
    tmz = request.args.get("timezone")
    try:
        usrtmz = timezone(tmz).zone
        return usrtmz
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config["BABEL_DEFAULT_TIMEZONE"]


def get_user() -> Union[dict, None]:
    """ Get user from db (mocked)"""
    key = request.args.get("login_as")
    try:
        return users.get(int(key))
    except Exception:
        return None


@app.before_request
def before_request():
    """ execute and set user before any request """
    g.user = get_user()


@app.route("/", methods=["GET"], strict_slashes=False)
def index() -> str:
    """ index page """
    current_time = datetime.utcnow()
    return render_template("index.html", current_time=current_time)


if __name__ == "__main__":
    app.run()
