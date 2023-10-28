# TODO: Feature 2
from src.repositories.movie_repository import get_movie_repository
import pytest

movie_repo = get_movie_repository()

def test_create_movie():
    movie = movie_repo.create_movie("Jurassic Park", "Steven Spsdsfjslberg", 5)
    assert movie is not None
    assert movie.movie_id>=0 and movie.movie_id<=100_000
    assert movie.title=="Jurassic Park"
    assert movie.director=="Steven Spsdsfjslberg"
    assert movie.rating==5
    
def test_multiple_movies():
    movie_repo.clear_db()
    movie1 = movie_repo.create_movie("movie1", "d1", 1)
    movie2 = movie_repo.create_movie("movie2", "d2", 2)
    assert movie1.movie_id != movie2.movie_id

def test_bad_movie_params():
    with pytest.raises(TypeError) as info:
        movie_repo.clear_db()
        no_info = movie_repo.create_movie("just this")
    assert "missing" in str(info.value)