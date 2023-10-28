# TODO: Feature 2
from app import app
from app import movie_repository



def test_page_exists():
    test_app = app.test_client()
    response = test_app.get('/movies/new')
    assert response.status_code ==200

def test_data_input(test_app):
    response = test_app.post('/movies/new', data={
        'directors':'John Doe',
        'movies':'The unkown man',
        'ratings':5,
    }, follow_redirects=True)
    assert response.status_code == 200
    
    compare = response.data.decode('utf-8')
    assert 'John Doe' in compare
    assert 'The unkown man' in compare
    assert '5' in compare