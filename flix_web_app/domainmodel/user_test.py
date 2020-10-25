from flix_web_app.domainmodel.user import User
from flix_web_app.domainmodel.movie import Movie
from flix_web_app.domainmodel.comment import Comment
from flix_web_app.domainmodel.watchlist import WatchList


def test_user_comments():
    user = User("Hazel", "1234")
    movie = Movie("Her", 2013)
    comment = Comment(movie, "What are some similar movies to this?")
    user.add_comment(comment)
    assert comment in user.comments
    user.add_comment(comment)
    assert len(user.comments) == 1


def test_user_watchlist():
    user = User("Hazel", "1234")
    watchlist = WatchList()
    user.add_watchlist(watchlist)
    assert user.watchlist == watchlist
    watchlist2 = WatchList()
    user.add_watchlist(watchlist2)
    assert user.watchlist == watchlist