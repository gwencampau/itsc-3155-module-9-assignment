# TODO: Feature 3

def test_search_movies_page(test_app):
    response = test_app.post('/movies/search', data={'title': 'Cool Movie'}, follow_redirects=True)
    response = test_app.get('/movies/search')

    data = response.data.decode('utf-8')
    
    assert  'title' in data

    response = test_app.post('/movies/search', data={'title': 'Bad Movie'}, follow_redirects=True)
    response = test_app.get('/movies/search')

    data = response.data.decode('utf-8')

    assert not('Some Movie' in data)

    response = test_app.post('/movies/search', data={'title': ''}, follow_redirects=True)
    response = test_app.get('/movies/search')

    data = response.data.decode('utf-8')

    assert '' in data
