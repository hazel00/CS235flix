from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director


class Movie:

    def __init__(self, title: str, release_year: int):
        if title == "" or type(title) is not str:
            self.__title = None
        else:
            self.__title = title.strip()
        if release_year is None or type(release_year) is not int or release_year < 1900:
            self.__release_year = None
        else:
            self.__release_year = release_year
        self.__director = None
        self.__description = None
        self.__actors = []
        self.__genres = []
        self.__runtime_minutes = None

    @property
    def title(self) -> str:
        return self.__title

    @property
    def release_year(self) -> int:
        return self.__release_year

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        if description is "" or type(description) is not str:
            self.__description = None
        else:
            self.__description = description.strip()

    @property
    def director(self) -> Director:
        return self.__director

    @director.setter
    def director(self, director: Director):
        if director is None or type(director) is not Director:
            self.__director = None
        else:
            self.__director = director

    @property
    def genres(self) -> list:
        return self.__genres

    @property
    def actors(self) -> list:
        return self.__actors

    @property
    def runtime_minutes(self) -> int:
        return self.__runtime_minutes

    @runtime_minutes.setter
    def runtime_minutes(self, runtime: int):
        if runtime <= 0:
            raise ValueError
        else:
            self.__runtime_minutes = runtime

    def __repr__(self):
        return f"<Movie {self.title}, {self.release_year}>"

    def __eq__(self, other):
        return self.title == other.title and self.release_year == other.release_year

    def __lt__(self, other):
        return self.__repr__() < other.__repr__()

    def __hash__(self):
        return hash((self.title, self.release_year))

    def add_actor(self, actor: Actor):
        if type(actor) is Actor and actor not in self.actors:
            self.__actors.append(actor)

    def remove_actor(self, actor: Actor):
        if actor in self.__actors:
            self.__actors.remove(actor)

    def add_genre(self, genre: Genre):
        if type(genre) is Genre and genre not in self.genres:
            self.__genres.append(genre)

    def remove_genre(self, genre: Genre):
        if genre in self.__genres:
            self.__genres.remove(genre)