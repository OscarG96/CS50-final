import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('main', __name__)

@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/movies", methods=('GET', 'POST'))
def movies():
    if request.method == 'POST':
        searchField = request.form['searchField']
        searchValue = request.form['searchValue']

        print(f"field", searchField)
        print(f"value", searchValue)

    return render_template("movies.html")
    
