from flix_web_app.domainmodel.actor import Actor
from flix_web_app.domainmodel.director import Director
from flix_web_app.domainmodel.genre import Genre
from flix_web_app.domainmodel.movie import Movie
from flix_web_app.domainmodel.user import User

import pytest

from flix_web_app.home import services as home_serv
from flix_web_app.logging_in import services as log_serv
from flix_web_app.search import services as search_serv
from flix_web_app.logging_in.services import ValidationException


def test_get_movies_for_browse(populated_repo):
    movie = Movie('Picnic', 2016)
    movie.id = 1001
    populated_repo.add_movie(movie)
    movie2 = Movie('Panadol', 2011)
    movie2.id = 1002
    populated_repo.add_movie(movie2)
    movie3 = Movie('Banana', 2009)
    movie3.id = 1003
    populated_repo.add_movie(movie3)
    assert home_serv.get_movies([1001, 1002, 1003], populated_repo) == [movie, movie2, movie3]


def test_get_ids_of_movies(populated_repo):
    li = [i for i in range(1, 1001)]
    assert home_serv.get_ids_of_movies(populated_repo) == li


def test_get_movie_ids_by_x(populated_repo):
    movie = Movie('Picnic', 2016)
    movie.id = 1001
    movie.add_genre(Genre('Blarg'))
    movie.add_actor(Actor('Glue Stick'))
    movie.director = Director('George Smith')
    populated_repo.add_movie(movie)
    lis = [1001]
    assert search_serv.get_movies_ids_by_title('Picnic', populated_repo) == lis
    assert search_serv.get_movies_ids_by_actor('Glue Stick', populated_repo) == lis
    assert search_serv.get_movies_ids_by_genre('Blarg', populated_repo) == lis
    assert search_serv.get_movies_ids_by_director('George Smith', populated_repo) == lis
    assert search_serv.get_movies_ids_by_title('LOL', populated_repo) is None
    assert search_serv.get_movies_ids_by_actor('LOL', populated_repo) is None
    assert search_serv.get_movies_ids_by_genre('LOL', populated_repo) is None
    assert search_serv.get_movies_ids_by_director('LOL', populated_repo) is None


def test_get_movies_by_x(populated_repo):
    movie = Movie('Picnic', 2016)
    movie.id = 1001
    movie.add_genre(Genre('Blarg'))
    movie.add_actor(Actor('Glue Stick'))
    movie.director = Director('George Smith')
    populated_repo.add_movie(movie)
    lis = [movie]
    assert search_serv.get_movies_by_title([1001], populated_repo) == lis
    assert search_serv.get_movies_by_actor([1001], populated_repo) == lis
    assert search_serv.get_movies_by_genre([1001], populated_repo) == lis
    assert search_serv.get_movies_by_director([1001], populated_repo) == lis
    assert search_serv.get_movies_by_title([1010], populated_repo) == []
    assert search_serv.get_movies_by_actor([1010], populated_repo) == []
    assert search_serv.get_movies_by_genre([1010], populated_repo) == []
    assert search_serv.get_movies_by_director([1010], populated_repo) == []


def test_add_user(populated_repo):
    # add new user
    user = User('Hazel', '12345')
    log_serv.add_user('Hazel', '12345', populated_repo)
    assert log_serv.get_user('Hazel', populated_repo) == user
    # user doesnt exist
    with pytest.raises(log_serv.UnknownUserException):
        log_serv.get_user('Error', populated_repo)
    # username taken
    with pytest.raises(log_serv.NameNotUniqueException):
        log_serv.add_user('Hazel', '12345', populated_repo)
    # invalid password
    with pytest.raises(log_serv.ValidationException):
        log_serv.validate_user('Hazel', "123456", populated_repo)
    #valid password
    try:
        log_serv.validate_user("Hazel", "12345", populated_repo)
    except ValidationException:
        assert False

