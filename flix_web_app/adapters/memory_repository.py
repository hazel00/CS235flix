from bisect import insort_left

from flix_web_app.adapters.repository import AbstractRepository
from flix_web_app.domainmodel.movie import Movie
from flix_web_app.domainmodel.actor import Actor
from flix_web_app.domainmodel.genre import Genre
from flix_web_app.domainmodel.director import Director
from flix_web_app.domainmodel.user import User
from flix_web_app.datafilereaders.movie_file_csv_reader import MovieFileCSVReader


class MemoryRepository(AbstractRepository):
    def __init__(self):
        self.__movies = list()
        self.__movie_index = dict()
        self.__users = [User('richard', 'test1234')]

    def add_user(self, user: User):
        self.__users.append(user)

    def get_user(self, username):
        for user in self.__users:
            if user.user_name == username:
                return user
        return None

    def get_movie(self, id: int):
        if id not in self.__movie_index.keys():
            return None
        else:
            return self.__movie_index[id]

    def add_movie(self, movie: Movie):
        insort_left(self.__movies, movie)
        self.__movie_index[movie.id] = movie

    def get_movies_for_browse(self, id_list):
        real_ids = [id for id in id_list if id in self.__movie_index]
        return [self.__movie_index[id] for id in real_ids]

    def get_ids_of_movies(self):
        return [i for i in self.__movie_index.keys()]

    def get_movies_ids_by_title(self, title: str):
        movies = []
        for movie in self.__movies:
            if movie.title == title:
                movies.append(movie.id)
        if len(movies) != 0:
            return movies
        else:
            return None

    def get_movies_ids_by_actor(self, actor: str):
        movies = []
        actorc = Actor(actor)
        for movie in self.__movies:
            if actorc in movie.actors:
                movies.append(movie.id)
        if len(movies) != 0:
            return movies
        else:
            return None

    def get_movies_ids_by_genre(self, genre: str):
        movies = []
        genrec = Genre(genre)
        for movie in self.__movies:
            if genrec in movie.genres:
                movies.append(movie.id)
        if len(movies) != 0:
            return movies
        else:
            return None

    def get_movies_ids_by_director(self, director: str):
        movies = []
        directorc = Director(director)
        for movie in self.__movies:
            if movie.director == directorc:
                movies.append(movie.id)
        if len(movies) != 0:
            return movies
        else:
            return None

    def get_movies_by_title(self, movie_ids: list):
        real_ids = [id for id in movie_ids if id in self.__movie_index]
        return [self.__movie_index[id] for id in real_ids]

    def get_movies_by_actor(self, movie_ids: list):
        real_ids = [id for id in movie_ids if id in self.__movie_index]
        return [self.__movie_index[id] for id in real_ids]

    def get_movies_by_genre(self, movie_ids: list):
        real_ids = [id for id in movie_ids if id in self.__movie_index]
        return [self.__movie_index[id] for id in real_ids]

    def get_movies_by_director(self, movie_ids: list):
        real_ids = [id for id in movie_ids if id in self.__movie_index]
        return [self.__movie_index[id] for id in real_ids]


def populate(userfilename, moviefilename, repo):
    moviecsv = MovieFileCSVReader(moviefilename)
    moviecsv.read_csv_file()
    usercsv = MovieFileCSVReader(userfilename)
    usercsv.read_user_csv_file()
    for movie in moviecsv.dataset_of_movies:
        repo.add_movie(movie)
    for user in usercsv.dataset_of_users:
        repo.add_user(user)