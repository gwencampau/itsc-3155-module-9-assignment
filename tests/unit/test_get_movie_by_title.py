# TODO: Feature 3
from app import app 
from src.models.movie import Movie 
from src.repositories.movie_repository import get_movie_repository 


def test_get_movie_by_title(): 
    movie = get_movie_repository() 
    new_movie = movie.create_movie("movie test", "gavin", 5) 

    movie_info = movie.get_movie_by_title(new_movie.title) 

    assert movie_info.title == "movie test"
    assert movie_info.rating == 5