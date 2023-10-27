# TODO: Feature 4
# TODO: Feature 4
from app import app, movie_repository
from src.models.movie import Movie
from src.repositories.movie_repository import get_movie_repository

def test_get_movie_by_id_1():
    test_app = app.test_client()
    # Base movie
    movie1 = movie_repository.create_movie('Scream', 'Wes Craven', 4)
    assert movie1 in movie_repository._db.values()
    m1id = movie1.movie_id
    assert movie_repository._db[m1id] != None
    assert type(movie1) is Movie  
    assert movie1.movie_id == m1id
    assert movie1.title == 'Scream'
    assert movie1.director == 'Wes Craven'
    assert movie1.rating == 4
    
    #Checking if changing a works
    movie2 = movie_repository.create_movie("A", "B", 1)
    assert type(movie2) is Movie 
    assert movie2 in movie_repository._db.values()
    m2id = movie2.movie_id
    movie2b = movie_repository._db.get(m2id)
    assert type(movie2b) is Movie 
    assert movie2b.movie_id == m2id
    assert movie2b.title == 'A'
    assert movie2b.director == 'B'
    assert movie2b.rating == 1
    #Check if making one based on another will stay same after get
    movie2 = movie_repository._db.get(m1id)
    assert type(movie2) != None 
    assert type(movie2) is Movie 
    assert movie2.movie_id == m1id
    assert movie2.title == 'Scream'
    assert movie2.director == 'Wes Craven'
    assert movie2.rating == 4
    assert movie2b.movie_id == m2id
    assert movie2b.title == 'A'
    assert movie2b.director == 'B'
    assert movie2b.rating == 1

    #Checking if the change impacts future ones
    movie3 = movie_repository._db.get(m2id)
    assert type(movie3) is Movie  
    assert movie3.movie_id == m2id
    assert movie2b.title == 'A'
    assert movie2b.director == 'B'
    assert movie2b.rating == 1

    '''Check if movie (variable) is deleted, does not get rid of database 
    ver. Make sure that deleting the movie from the database directly 
    does remove it completely'''
    movie4 = movie_repository._db.get(m2id)
    del movie4
    assert movie_repository._db.get(m2id) in movie_repository._db.values()
    del movie_repository._db[m2id]
    assert movie_repository._db.get(m2id) == None
    
    #Make sure it shows up properly on page
    response = test_app.get('/movies/' + str(movie2.movie_id))
    assert response.status_code == 200
    data = response.data.decode()
    assert 'Scream' in data
    assert 'Rating: 4' in data
    assert '<p>Director: Wes Craven</p>' in data

def test_get_movie_by_id_2():
    test_app = app.test_client()
    movie1 = movie_repository.get_movie_by_id(87654654654)
    assert movie1 is None
    assert type(movie1) is not Movie 
    response = test_app.get('/movies/87654654654')
    assert response.status_code == 400