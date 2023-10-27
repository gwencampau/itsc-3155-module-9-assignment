# TODO: Feature 6
from app import movie_repository
from app import delete_movie
import pytest

def test_movie_deleted_from_repo():
    movie = movie_repository.create_movie('Lego Movie','Chris Miller', 3)
    delete_movie(movie.movie_id)
    assert movie not in movie_repository._db

def test_delete_movie():
     movie = movie_repository.create_movie('Lego Movie','Chris Miller', 3)
     x = movie_repository.delete_movie(movie.movie_id)
     assert x == movie

def test_movie_not_found():
     with pytest.raises(ValueError,match=f"movie with id {1065} not found"):
        movie_repository.delete_movie(1065)
     
    


