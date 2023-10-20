# TODO: Feature 1
from app import app

def test_list_all_movies(test_app):
    response = test_app.get('/movies')

    data = response.data.decode()

    assert response.status_code == 200