from flask import Blueprint, render_template, request, url_for
import flix_web_app.adapters.repository as repo
import flix_web_app.home.services as services

home_blueprint = Blueprint('home_bp', __name__)


@home_blueprint.route('/', methods=['GET'])
def home():
    movies_per_page = 3

    cursor = request.args.get('cursor')

    if cursor is None:
        cursor = 0
    else:
        cursor = int(cursor)

    movie_ids = services.get_ids_of_movies(repo.repo_instance)

    movies = services.get_movies(movie_ids[cursor: cursor + movies_per_page], repo.repo_instance)

    first_movie = None
    prev_movie = None
    next_movie = None
    last_movie = None

    if cursor > 0:
        first_movie = url_for('home_bp.home')
        prev_movie = url_for('home_bp.home', cursor=cursor - movies_per_page)

    if cursor + movies_per_page < len(movie_ids):
        next_movie = url_for('home_bp.home', cursor=cursor + movies_per_page)

        last_page = movies_per_page * int(len(movie_ids) / movies_per_page)
        if len(movie_ids) % movies_per_page == 0:
            last_page -= movies_per_page
        last_movie = url_for('home_bp.home', cursor=last_page)

    return render_template(
        'home.html', movie_ids=movie_ids, movies=movies,
        first_movie=first_movie,
        next_movie=next_movie, last_movie=last_movie,
        prev_movie=prev_movie
    )