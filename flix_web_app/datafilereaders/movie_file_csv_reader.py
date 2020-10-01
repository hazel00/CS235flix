import csv

from flix_web_app.domainmodel.movie import Movie
from flix_web_app.domainmodel.actor import Actor
from flix_web_app.domainmodel.genre import Genre
from flix_web_app.domainmodel.director import Director


class MovieFileCSVReader:

    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__dataset_of_directors = set()
        self.__dataset_of_actors = set()
        self.__dataset_of_movies = []
        self.__dataset_of_genres = set()

    @property
    def dataset_of_actors(self):
        return self.__dataset_of_actors

    @property
    def dataset_of_directors(self):
        return self.__dataset_of_directors

    @property
    def dataset_of_movies(self):
        return self.__dataset_of_movies

    @property
    def dataset_of_genres(self):
        return self.__dataset_of_genres

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)

            for row in movie_file_reader:

                movie_class = Movie(row['Title'], int(row['Year']))
                if movie_class not in self.dataset_of_movies:
                    movie_class.id = row['Rank']
                    director = Director(row['Director'])
                    movie_class.director = director
                    movie_class.description = row['Description']
                    for actor in row['Actors'].split(","):
                        actor_movie = Actor(actor)
                        movie_class.add_actor(actor_movie)
                    for genre in row['Genre'].split(","):
                        genre_movie = Genre(genre)
                        movie_class.add_genre(genre_movie)
                    movie_class.runtime_minutes = int(row['Runtime (Minutes)'])
                    self.dataset_of_movies.append(movie_class)

                for actor in row['Actors'].split(","):
                    actor_class = Actor(actor)
                    if actor_class not in self.dataset_of_actors:
                        self.dataset_of_actors.add(actor_class)

                director_class = Director(row['Director'])
                if director_class not in self.dataset_of_directors:
                    self.dataset_of_directors.add(director_class)

                for genre in row['Genre'].split(","):
                    genre_class = Genre(genre)
                    if genre_class not in self.dataset_of_genres:
                        self.dataset_of_genres.add(genre_class)
