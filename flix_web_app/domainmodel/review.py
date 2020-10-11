from datetime import datetime

from flix_web_app.domainmodel.movie import Movie


class Review:
    def __init__(self, movie: Movie, review_text: str, rating: int):
        if review_text == "" or type(review_text) is not str:
            self.__review_text = None
        else:
            self.__review_text = review_text.strip()
        if movie is None or type(movie) is not Movie:
            self.__movie = None
        else:
            self.__movie = movie
        if rating is None or type(rating) is not int or rating < 1 or rating > 10:
            self.__rating = None
        else:
            self.__rating = rating
        datetime_object = datetime.now()
        self.__timestamp = datetime_object

    @property
    def movie(self) -> Movie:
        return self.__movie

    @property
    def review_text(self) -> str:
        return self.__review_text

    @property
    def rating(self) -> int:
        return self.__rating

    @property
    def timestamp(self) -> datetime:
        return self.__timestamp

    def __repr__(self):
        return f"<Movie {self.movie}, Review {self.review_text}, Rating {self.rating}, Time {self.timestamp}>"

    def __eq__(self, other):
        return self.movie == other.movie and self.review_text == other.review_text and self.rating == other.rating and self.timestamp == other.timestamp