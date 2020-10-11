import abc


from flix_web_app.domainmodel.movie import Movie


repo_instance = None


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def get_movie(self, id: int):
        raise NotImplementedError

    @abc.abstractmethod
    def add_movie(self, movie: Movie):
        raise NotImplementedError

    @abc.abstractmethod
<<<<<<< HEAD
    def get_movies_for_browse(self, id_list):
=======
    def get_movies_for_browse(self):
>>>>>>> refs/remotes/origin/master
        raise NotImplementedError

    @abc.abstractmethod
    def get_ids_of_movies(self):
<<<<<<< HEAD
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies_ids_by_title(self, title: str):
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies_ids_by_actor(self, actor: str):
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies_ids_by_genre(self, genre: str):
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies_ids_by_director(self, director: str):
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies_by_title(self, movie_ids: list):
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies_by_actor(self, movie_ids: list):
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies_by_genre(self, movie_ids: list):
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies_by_director(self, movie_ids: list):
=======
>>>>>>> refs/remotes/origin/master
        raise NotImplementedError