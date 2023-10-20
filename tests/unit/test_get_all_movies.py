# TODO: Feature 1
from app import app

def test_list_all_movies():
    test_app = app.test_client()
    response = test_app.get('/movies')
    assert response.status_code == 200