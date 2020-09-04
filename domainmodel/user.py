from domainmodel.movie import Movie
from domainmodel.review import Review
from domainmodel.comment import Comment
from domainmodel.watchlist import WatchList


class User:
    def __init__(self, user_name: str, password: str):
        if user_name == "" or type(user_name) is not str:
            self.__user_name = None
        else:
            self.__user_name = user_name.strip().lower()
        self.__password = password
        self.__watched_movies = []
        self.__reviews = []
        self.__comments = []
        self.__time_spent_watching_movies_minutes = 0
        self.__watchlist = None

    @property
    def user_name(self) -> str:
        return self.__user_name

    @property
    def password(self) -> str:
        return self.__password

    @property
    def watched_movies(self) -> list:
        return self.__watched_movies

    @property
    def reviews(self) -> list:
        return self.__reviews

    @property
    def comments(self) -> list:
        return self.__comments

    @property
    def watchlist(self) -> WatchList:
        return self.__watchlist

    @property
    def time_spent_watching_movies_minutes(self) -> int:
        return self.__time_spent_watching_movies_minutes

    def __repr__(self):
        return f"<User {self.user_name}>"

    def __eq__(self, other):
        return self.user_name == other.user_name

    def __lt__(self, other):
        return self.user_name < other.user_name

    def __hash__(self):
        return hash(self.user_name)

    def watch_movie(self, movie: Movie):
        if movie not in self.watched_movies:
            self.__watched_movies.append(movie)
        if movie.runtime_minutes is not None:
            self.__time_spent_watching_movies_minutes += movie.runtime_minutes

    def add_review(self, review: Review):
        if review not in self.reviews:
            self.__reviews.append(review)

    def add_comment(self, comment: Comment):
        if comment not in self.comments:
            self.__comments.append(comment)

    def add_watchlist(self, watchlist: WatchList):
        if self.watchlist is None:
            self.__watchlist = watchlist