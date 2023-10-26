# TODO: Feature 1
from app import app
from app import movie_repository

def test_list_all_movies(test_app):
    response = test_app.get('/movies')
    assert response.status_code == 200

def test_list_all_movies2(test_app):
    movie_repository.create_movie('Cars', 'John Lasseter', 4)
    response = test_app.get('/movies')
    assert b'Cars' in response.data
    assert b'John Lasseter' in response.data
    assert b'4' in response.data