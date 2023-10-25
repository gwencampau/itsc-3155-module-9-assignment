# TODO: Feature 1
from app import app
from src.models.movie import Movie
from random import randint

def test_list_all_movies():
    test_app = app.test_client()
    response = test_app.get('/movies')
    assert response.status_code == 200
    assert b'<th scope="col">Title</th>' in response.data

def test_list_all_movies2():
    random = randint(0, 100_000)
    movie = Movie(random, 'Monsters Inc', 'Pete Docter', 5)
    assert movie.movie_id == random
    assert movie.title == 'Monsters Inc'
    assert movie.director == 'Pete Docter'
    assert movie.rating == 5