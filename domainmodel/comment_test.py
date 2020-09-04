from datetime import datetime
from domainmodel.user import User
from domainmodel.movie import Movie
from domainmodel.comment import Comment


def test_comment_init():
    movie = Movie("Her", 2013)
    comment = Comment(movie, "What year was this movie set in?")
    assert comment.movie == movie
    assert comment.comment == "What year was this movie set in?"
    assert comment.timestamp == datetime.now()
    assert comment.parent is None


def test_replies():
    movie = Movie("Her", 2013)
    comment = Comment(movie, "What year was this movie set in?")
    reply = Comment(movie, "Wait nevermind I just Googled it")
    comment.add_reply(reply)
    assert reply in comment.replies
    assert reply.parent == comment
    reply2 = Comment(movie, "haha wow")
    reply.add_reply(reply2)
    assert reply2.parent is comment
    reply3 = Comment(movie, "oh my god")
    reply2.add_reply(reply3)
    assert reply3.parent is comment
    reply4 = Comment(Movie("Kill Bill: Volume 1", 2003), "I hope they make a sequel")
    comment.add_reply(reply4)
    assert reply4.parent is None
    comment.remove_reply(reply)
    assert reply not in comment.replies
    comment.remove_reply(reply4)
    assert reply4 not in comment.replies

