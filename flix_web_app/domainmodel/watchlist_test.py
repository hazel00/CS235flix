import pytest
from flix_web_app.domainmodel.movie import Movie
from flix_web_app.domainmodel.watchlist import WatchList


def test_size():
    watchlist = WatchList()
    assert watchlist.size() == 0
    movie1 = Movie("Moana", 2016)
    movie2 = Movie("Booksmart", 2019)
    movie3 = Movie("School of Rock", 2003)
    movie4 = Movie("Roma", 2018)
    watchlist.add_movie(movie1)
    watchlist.add_movie(movie2)
    watchlist.add_movie(movie3)
    watchlist.add_movie(movie4)
    assert watchlist.size() == 4


def test_adding_and_removing():
    watchlist = WatchList()
    movie1 = Movie("Moana", 2016)
    movie2 = Movie("Booksmart", 2019)
    movie3 = Movie("School of Rock", 2003)
    movie4 = Movie("Roma", 2018)
    watchlist.add_movie(movie1)
    watchlist.add_movie(movie2)
    watchlist.add_movie(movie3)
    watchlist.add_movie(movie4)
    watchlist.add_movie(movie4)
    assert watchlist.size() == 4
    watchlist.remove_movie(movie1)
    assert watchlist.size() == 3
    watchlist.remove_movie(Movie("Juno", 2007))
    assert watchlist.size() == 3


def test_iterator():
    movie1 = Movie("Moana", 2016)
    movie2 = Movie("Booksmart", 2019)
    movie3 = Movie("School of Rock", 2003)
    movie4 = Movie("Roma", 2018)
    watchlist = WatchList()
    watchlist.add_movie(movie1)
    watchlist.add_movie(movie2)
    watchlist.add_movie(movie3)
    watchlist.add_movie(movie4)
    it1 = iter(watchlist)
    assert next(it1) == Movie("Moana", 2016)
    assert next(it1) == Movie("Booksmart", 2019)
    assert next(it1) == Movie("School of Rock", 2003)
    assert next(it1) == Movie("Roma", 2018)
    with pytest.raises(StopIteration):
        next(it1)


def test_select_and_first():
    movie1 = Movie("Moana", 2016)
    movie2 = Movie("Booksmart", 2019)
    movie3 = Movie("School of Rock", 2003)
    movie4 = Movie("Roma", 2018)
    watchlist = WatchList()
    watchlist.add_movie(movie1)
    watchlist.add_movie(movie2)
    watchlist.add_movie(movie3)
    watchlist.add_movie(movie4)
    assert watchlist.select_movie_to_watch(0) == Movie("Moana", 2016)
    assert watchlist.select_movie_to_watch(5) is None
    assert watchlist.first_movie_in_watchlist() == Movie("Moana", 2016)
    watchlist2 = WatchList()
    assert watchlist2.first_movie_in_watchlist() is None
