from flix_web_app.domainmodel.actor import Actor
from flix_web_app.domainmodel.director import Director
from flix_web_app.domainmodel.genre import Genre
from flix_web_app.domainmodel.movie import Movie
from flix_web_app.domainmodel.user import User


def test_get_user(populated_repo):
    user = User('hazel', 'password')
    populated_repo.add_user(user)
    assert populated_repo.get_user('hazel') is user


def test_get_movie(populated_repo):
    movie = Movie('Picnic', 2016)
    movie.id = 1001
    populated_repo.add_movie(movie)
    assert populated_repo.get_movie(1001) is movie


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
    assert populated_repo.get_movies_for_browse([1001, 1002, 1003]) == [movie, movie2, movie3]


def test_get_ids_of_movies(populated_repo):
    li = [i for i in range(1, 1001)]
    assert populated_repo.get_ids_of_movies() == li


def test_get_movie_ids_by_x(populated_repo):
    movie = Movie('Picnic', 2016)
    movie.id = 1001
    movie.add_genre(Genre('Blarg'))
    movie.add_actor(Actor('Glue Stick'))
    movie.director = Director('George Smith')
    populated_repo.add_movie(movie)
    lis = [1001]
    assert populated_repo.get_movies_ids_by_title('Picnic') == lis
    assert populated_repo.get_movies_ids_by_actor('Glue Stick') == lis
    assert populated_repo.get_movies_ids_by_genre('Blarg') == lis
    assert populated_repo.get_movies_ids_by_director('George Smith') == lis


def test_get_movies_by_x(populated_repo):
    movie = Movie('Picnic', 2016)
    movie.id = 1001
    movie.add_genre(Genre('Blarg'))
    movie.add_actor(Actor('Glue Stick'))
    movie.director = Director('George Smith')
    populated_repo.add_movie(movie)
    lis = [movie]
    assert populated_repo.get_movies_by_title([1001]) == lis
    assert populated_repo.get_movies_by_actor([1001]) == lis
    assert populated_repo.get_movies_by_genre([1001]) == lis
    assert populated_repo.get_movies_by_director([1001]) == lis
