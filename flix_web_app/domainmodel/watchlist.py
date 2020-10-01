from domainmodel.movie import Movie


class WatchList:
    def __init__(self):
        self.__watchlist = []
        self.__index = 0

    @property
    def watchlist(self) -> list:
        return self.__watchlist

    @property
    def index(self) -> int:
        return self.__index

    def add_movie(self, movie: Movie):
        if movie not in self.watchlist:
            self.watchlist.append(movie)

    def remove_movie(self, movie: Movie):
        if movie in self.watchlist:
            self.watchlist.remove(movie)

    def select_movie_to_watch(self, index: int):
        if index < 0 or index > len(self.watchlist) - 1:
            return None
        else:
            return self.watchlist[index]

    def size(self) -> int:
        return len(self.watchlist)

    def first_movie_in_watchlist(self):
        if len(self.watchlist) == 0:
            return None
        else:
            return self.watchlist[0]

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == self.size():
            raise StopIteration
        else:
            item = self.watchlist[self.index]
            self.__index += 1
            return item