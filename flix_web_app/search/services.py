from flix_web_app.adapters.repository import AbstractRepository


def get_movies_by_title(movie_ids: list, repo: AbstractRepository):
    movies = repo.get_movies_by_title(movie_ids)
    return movies


def get_movies_by_actor(movie_ids: list, repo: AbstractRepository):
    movies = repo.get_movies_by_actor(movie_ids)
    return movies


def get_movies_by_genre(movie_ids: list, repo: AbstractRepository):
    movies = repo.get_movies_by_genre(movie_ids)
    return movies


def get_movies_by_director(movie_ids: list, repo: AbstractRepository):
    movies = repo.get_movies_by_director(movie_ids)
    return movies


def get_movies_ids_by_title(title, repo: AbstractRepository):
    movie_ids = repo.get_movies_ids_by_title(title)
    return movie_ids


def get_movies_ids_by_actor(actor, repo: AbstractRepository):
    movie_ids = repo.get_movies_ids_by_actor(actor)
    return movie_ids


def get_movies_ids_by_genre(genre, repo: AbstractRepository):
    movie_ids = repo.get_movies_ids_by_genre(genre)
    return movie_ids


def get_movies_ids_by_director(director, repo: AbstractRepository):
    movie_ids = repo.get_movies_ids_by_director(director)
    return movie_ids