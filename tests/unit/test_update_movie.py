# TODO: Feature 5
from app import app
from src.repositories.movie_repository import get_movie_repository

movie_repository = get_movie_repository()

def test_update_movie():
    movie_repository.clear_db()
    original_movie = movie_repository.create_movie("Test Title", "Test Director", 5)
    updated_movie = movie_repository.update_movie(original_movie.movie_id, "New title", "New dir", 3)
    assert (movie_repository.get_movie_by_id(original_movie.movie_id)).title == "New title"
    assert (movie_repository.get_movie_by_id(original_movie.movie_id)).director == "New dir"
    assert (movie_repository.get_movie_by_id(original_movie.movie_id)).rating == 3

def test_update_movie_flask():
    test_app = app.test_client()
    movie_repository.clear_db()
    original_movie = movie_repository.create_movie("Test Title", "Test Director", 5)
    id = original_movie.movie_id
    response = test_app.post(f'/movies/{id}', data={
        "title": "New title",
        "director": "New dir",
        "new_rating": 4
    }, follow_redirects=True)
    
    updated_movie = movie_repository.get_movie_by_id(id)

    assert updated_movie.title=="New title"
    assert updated_movie.director=="New dir"
    assert updated_movie.rating==4
    assert response.status_code==200
    
def test_update_movie_bad():
    test_app = app.test_client()
    movie_repository.clear_db()
    original_movie = movie_repository.create_movie("Test Title", "Test Director", 5)
    bad_id = original_movie.movie_id + 1
    response = test_app.post(f'/movies/{bad_id}', data={
        "title": "New title",
        "director": "New dir",
        "new_rating": 4
    })

    assert response.status_code==500