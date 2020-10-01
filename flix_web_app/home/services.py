from flix_web_app.adapters.repository import AbstractRepository


def get_ids_of_movies(repo: AbstractRepository):
    id_list = repo.get_ids_of_movies()
    return id_list


def get_movies(id_list, repo: AbstractRepository):
    movies = repo.get_movies_for_browse(id_list)
    return movies