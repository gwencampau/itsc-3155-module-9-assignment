# TODO: Feature 3
from src.repositories.movie_repository import get_movie_repository


def test_search_movies(test_app):
    response = test_app.get('/movies/search')
    assert response.status_code == 200

def test_searching(test_app):
    movie = get_movie_repository() 
    movie.create_movie("new movie", "gavin", 3)
    movie_test = movie.get_movie_by_title

    response = test_app.get(f'/movies/{movie_test}', follow_redirects=True)

    assert response.status_code == 200
    assert b'<td>new movie</td>' in response.data
    assert b'<td> gavin </td>' in response.data
    assert b'<td> 3 </td>' in response.data