# TODO: Feature 5
from src.repositories.movie_repository import get_movie_repository
import pytest

movie_repository = get_movie_repository()

def test_update_movie():
    movie_repository.clear_db()
    original_movie = movie_repository.create_movie("Test Title", "Test Director", 5)
    updated_movie = movie_repository.update_movie(original_movie.movie_id, "New title", "New dir", 3)
    assert (movie_repository.get_movie_by_id(original_movie.movie_id)).title == "New title"
    assert (movie_repository.get_movie_by_id(original_movie.movie_id)).director == "New dir"
    assert (movie_repository.get_movie_by_id(original_movie.movie_id)).rating == 3
    assert original_movie.movie_id==updated_movie.movie_id

def test_update_movie_DNE():
    with pytest.raises(ValueError) as info:
        movie_repository.clear_db()
        no_movie = movie_repository.update_movie(12345, "imaginary movie", "imaginary friend", 3)
    assert "not found" in str(info.value)