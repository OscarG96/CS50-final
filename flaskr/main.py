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
    MOVIES = []
    if request.method == 'POST':
        searchField = request.form['searchField']
        searchValue = request.form['searchValue']
        db = get_db("DATABASE_MOVIES")
        error = None
        movies = db.execute(
            'SELECT * FROM movies WHERE title = ?', (searchValue,)
        ).fetchone()

        MOVIES.append(movies)
        
        print(f"field", searchField)
        print(f"value", searchValue)
        for field in movies:
            print(f"movies sql", field)
        return render_template("movies.html", movies=MOVIES)

    return render_template("movies.html")
    
