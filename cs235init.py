<<<<<<< HEAD
from flix_web_app.datafilereaders.movie_file_csv_reader import MovieFileCSVReader
=======
from datafilereaders.movie_file_csv_reader import MovieFileCSVReader
>>>>>>> refs/remotes/origin/master


def main():
    filename = 'datafiles/Data1000Movies.csv'
    movie_file_reader = MovieFileCSVReader(filename)
    movie_file_reader.read_csv_file()



if __name__ == "__main__":
    main()