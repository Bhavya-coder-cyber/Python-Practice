import os
import json

FILENAME = "movies.json"

def load_movies():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r", encoding="utf-8") as f:
        return json.load(f)

def save_movies(movies):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(movies, f, indent=2)

def add_movies(movies):
    title = input("Enter the movie name: ").lower().strip()
    if any(movie["title"].lower() == title for movie in movies):
        print("Movie already exists")
        return

    genre = input("Enter the genre: ").lower().strip()
    try:
        rating = int(input("Enter the rating out of 10: "))
        if not 0 <= rating <= 10:
            raise ValueError
    except ValueError:
        print("Rating must be between 0 and 10")
        return

    movies.append({"title": title, "genre": genre, "rating": rating})
    save_movies(movies)
    print("Movie added successfully")

def search_movie(movies):
    term = input("Enter the name or genre to search: ").lower().strip()
    results = [
        movie for movie in movies 
        if term in movie["title"].lower() or term in movie["genre"].lower()
    ]

    if not results:
        print("No results found")
        return

    for movie in results:
        print(f"{movie['title']} -- ({movie['genre']}) -- {movie['rating']}")

def view_movies(movies):
    if not movies:
        print("No movies found")
        return

    print("-"*30)
    for movie in movies:
        print(f"{movie['title']} -- ({movie['genre']}) -- {movie['rating']}")
    print("-"*30)

def run_program():
    movies = load_movies()
    while True:
        print("1. Add Movie")
        print("2. View Movies")
        print("3. Search Movie")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        match choice:
            case "1":
                add_movies(movies)
            case "2":
                view_movies(movies)
            case "3":
                search_movie(movies)
            case "4":
                break
            case _:
                print("Invalid choice")

if __name__ == "__main__":
    run_program()
    