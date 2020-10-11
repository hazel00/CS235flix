from flix_web_app.domainmodel.actor import Actor
from flix_web_app.domainmodel.director import Director
from flix_web_app.domainmodel.genre import Genre
from flix_web_app.domainmodel.movie import Movie


def test_domain_init():
    movie = Movie("Moana", 2018)
    movie.director = Director("Hans Zimmerman")
    movie.id = 4
    movie.description = "hello world"
    assert movie.actors == []
    actor1 = Actor("Jennifer Lawrence")
    actor2 = Actor("James McAvoy")
    movie.add_actor(actor1)
    movie.add_actor(actor2)
    assert movie.actors == [actor1, actor2]
    assert movie.genres == []
    genre1 = Genre('Comedy')
    genre2 = Genre('Romance')
    movie.add_genre(genre1)
    movie.add_genre(genre2)
    assert movie.genres == [genre1, genre2]

