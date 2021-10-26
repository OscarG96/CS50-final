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
        for el in request.form:
            print(f"field", el, request.form[el])
        searchField = request.form['searchField']
        searchValue = request.form['searchValue']
        query = ''
        if searchField == 'movieName':
            query = 'SELECT * FROM movies WHERE title = ?'
        elif searchField == 'cast':
            query = 'SELECT * from movies JOIN stars on movies.id = stars.movie_id WHERE person_id = (SELECT id FROM people WHERE name LIKE ?);'
        else:
            return
        db = get_db("DATABASE_MOVIES")
        error = None
        movies = db.execute(
            query, [searchValue]
        ).fetchall()

        MOVIES.append(movies)
        
        # print(f"field", searchField)
        # print(f"value", searchValue)
        for field in movies:
            print(f"movies sql", field)
        return render_template("movies.html", movies=MOVIES)

    return render_template("movies.html")
    
