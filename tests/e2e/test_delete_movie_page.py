# TODO: Feature 6
from app import app
from app import movie_repository

def test_delete_movie(test_app):
    movie = movie_repository.create_movie('Lego Movie', 'Chris Miller',4)
    response = test_app.post(f'/movies/{movie.movie_id}/delete')
    assert response.status_code == 302

def test_delete_movie_redirect():
    test_app = app.test_client() 
    movie = movie_repository.create_movie('Lego Movie', 'Chris Miller',4)
    response = test_app.post(f'/movies/{movie.movie_id}/delete', follow_redirects=True)
    assert response.status_code == 200
