from catalogue import Catalogue
from user import User

import random

movie_catalogue = Catalogue()

users = [
    User("user1@gmail.com", "John"),
    User("user2@gmail.com", "Mike"),
    User("user3@gmail.com", "Alice"),
    User("user4@gmail.com", "Alex"),
    User("user5@gmail.com", "Jane"),
]


def simulate_user_behaviour():
    for user in users:
        random_movie_index = random.randint(0, len(movie_catalogue.movies))
        if random_movie_index == len(movie_catalogue.movies):
            user.cur_movie = None
        else:
            user.cur_movie = movie_catalogue.movies[random_movie_index]


def notflix():

    print("Welcome to Notflix!")
    print()

    while True:
        simulate_user_behaviour()

        print("1. List movies")
        print("2. List users")
        user_input = int(input("Select your option: "))
        print()

        if user_input == 1:
            movies = movie_catalogue.get_movies()
            for movie in movies:
                print(f"{movie.name} ({movie.duration} minutes) - {movie.lead_actor}")
        elif user_input == 2:
            for user in users:
                if user.cur_movie:
                    print(f"{user.name} is watching {user.cur_movie.name}")
                else:
                    print(f"{user.name} is not watching anything")
        else:
            print("Thank you for using Notflix!")
            break

        print()


if __name__ == "__main__":

    notflix()
