from flask import Blueprint, render_template, url_for, redirect, flash, request
from wtforms import StringField, SelectField, SubmitField
from flask_wtf import FlaskForm
import flix_web_app.search.services as services
import flix_web_app.adapters.repository as repo

search_blueprint = Blueprint('search_bp', __name__)


@search_blueprint.route('/search', methods=['GET', 'POST'])
def search():
    form = MovieSearch()

    cursor = request.args.get('cursor')

    if cursor is None:
        cursor = 0
    else:
        cursor = int(cursor)

    if request.method == 'POST':
        return results(form, cursor)

    return render_template(
            'search.html', form=form,  handler_url=url_for('search_bp.search')
        )


def results(form, cursor):
    movies = None
    if form.selection.data == 'Title':
        movie_ids = services.get_movies_ids_by_title(form.search.data.title(), repo.repo_instance)
        if movie_ids is not None:
            movies = services.get_movies_by_title(movie_ids, repo.repo_instance)

    elif form.selection.data == 'Actor':
        movie_ids = services.get_movies_ids_by_actor(form.search.data.title(), repo.repo_instance)
        if movie_ids is not None:
            movies = services.get_movies_by_actor(movie_ids, repo.repo_instance)

    elif form.selection.data == 'Genre':
        movie_ids = services.get_movies_ids_by_genre(form.search.data.title(), repo.repo_instance)
        if movie_ids is not None:
            movies = services.get_movies_by_genre(movie_ids, repo.repo_instance)

    else:
        movie_ids = services.get_movies_ids_by_director(form.search.data.title(), repo.repo_instance)
        if movie_ids is not None:
            movies = services.get_movies_by_director(movie_ids, repo.repo_instance)

    if movies is None:
        return render_template('search.html', form=form, results=movies, movie_ids=movie_ids,
                               handler_url=url_for('search_bp.search'))
    else:

        return render_template('results.html', form=form, results=movies, movie_ids=movie_ids,
                               handler_url=url_for('search_bp.search'))


class MovieSearch(FlaskForm):
    options = ['Title', 'Actor', 'Genre', 'Director']
    selection = SelectField('Search Movies:', choices=options)
    search = StringField('')
    submit = SubmitField('Search')