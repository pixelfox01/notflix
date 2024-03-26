from movie import Movie


class Catalogue:
    def __init__(self):
        self.movies = [
            Movie("Whiplash", 120, "J.K. Simmons"),
            Movie("Interstellar", 180, "Matthew McConaughey"),
            Movie("Kung Fu Panda", 100, "Jack Black"),
            Movie("The Nice Guys", 90, "Ryan Gosling"),
        ]

    def get_movies(self):
        return self.movies

    def get_movie(self, name):
        for movie in self.movies:
            if name.lower() == movie.name.lower():
                return movie
        print(f"{name} does not exist!")
        return None

