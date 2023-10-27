# TODO: Feature 5
from app import app
from src.repositories.movie_repository import get_movie_repository

movie_repository = get_movie_repository()

def test_edit_page(test_app):
    movie_repository.clear_db()
    original_movie = movie_repository.create_movie("Test Title", "Test Director", 5)
    id = original_movie.movie_id
    response = test_app.get(f'/movies/{id}/edit')
    assert response.status_code==200

def test_edit_page_DNE(test_app):
    movie_repository.clear_db()
    original_movie = movie_repository.create_movie("Test Title", "Test Director", 5)
    id = original_movie.movie_id
    response = test_app.get(f'/movies/{id+1}/edit')
    assert response.status_code==400

def test_update_movie_flask(test_app):
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