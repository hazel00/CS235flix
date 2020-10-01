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
    def get_movies_for_browse(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_ids_of_movies(self):
        raise NotImplementedError