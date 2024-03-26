class User:
    def __init__(self, email, name):
        self.email = email
        self.name = name
        self.cur_movie = None

    def watch_movie(self, movie):
        self.cur_movie = movie
