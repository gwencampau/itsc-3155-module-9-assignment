# TODO: Feature 4
from app import app, movie_repository

def test_get_single_movie(test_app):
    movie1 = movie_repository.create_movie('Spirited Away', 'Hayao Miyazaki', 4)
    response = test_app.get('/movies/' + str(movie1.movie_id))
    assert response.status_code == 200
    data = response.data.decode()
    assert 'Spirited Away' in data
    assert 'Hayao Miyazaki' in data
    assert '4' in data

def test_get_single_movie_2(test_app):
    response = test_app.get('/movies/')
    assert response.status_code == 404

    response = test_app.get('/movies/865465468')
    assert response.status_code == 400