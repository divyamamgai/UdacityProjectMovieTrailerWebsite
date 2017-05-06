import fresh_tomatoes
import media

# Initialize all the movies by their Titles using APIs.
movies = [
    # For Cars movie trailer path is invalid, instead there is trailer-a, trailer-b and teaser-trailer.
    media.Movie.initialize_from_title("Cars", "trailer-a"),
    media.Movie.initialize_from_title("WALL-E"),
    media.Movie.initialize_from_title("Finding Nemo", "trailer-a"),
    media.Movie.initialize_from_title("Monsters, Inc."),
    media.Movie.initialize_from_title("Toy Story"),
    media.Movie.initialize_from_title("The Incredibles")
]

# Create and Open the movies page.
fresh_tomatoes.open_movies_page(movies)
