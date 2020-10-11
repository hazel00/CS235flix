from datetime import datetime
from flix_web_app.domainmodel.movie import Movie


class Comment:
    def __init__(self, movie: Movie, comment: str):
        if comment == "":
            self.__comment = None
        else:
            self.__comment = comment.strip()
        self.__movie = movie
        self.__replies = []
        datetime_object = datetime.now()
        self.__timestamp = datetime_object
        self.__parent = None

    @property
    def comment(self):
        return self.__comment

    @property
    def movie(self):
        return self.__movie

    @property
    def replies(self):
        return self.__replies

    @property
    def timestamp(self):
        return self.__timestamp

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, parent):
        self.__parent = parent

    def __repr__(self):
        return f"<{self.movie}, Comment {self.comment}, Time {self.timestamp}>"

    def __eq__(self, other):
        return self.__repr__() == other.__repr__()

    def add_reply(self, reply):
        if reply.movie == self.movie and self.parent is None:
            self.__replies.append(reply)
            reply.parent = self
        elif self.parent is not None and reply.movie == self.parent.__movie:
            self.parent.__replies.append(reply)
            reply.parent = self.parent

    def remove_reply(self, reply):
        if reply in self.replies:
            self.__replies.remove(reply)