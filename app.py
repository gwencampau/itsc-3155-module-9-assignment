from flask import Flask, redirect, render_template, request

from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)

# Get the movie repository singleton to use throughout the application
movie_repository = get_movie_repository()

@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    # TODO: Feature 1
    movies = movie_repository.get_all_movies()
    return render_template('list_all_movies.html', movies=movies, list_movies_active=True)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies/new')
def create_movie():
    # TODO: Feature 2
    rating = request.form.get('ratings')
    director = request.form.get('directors')
    movie = request.form.get('movies')
    movie_repository.create_movie(movie, director,rating)
    # After creating the movie in the database, we redirect to the list all movies page
    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    return render_template('search_movies.html', search_active=True)


@app.get('/movies/<int:movie_id>')
def get_single_movie(movie_id: int):
    # TODO: Feature 4
    movie = movie_repository.get_movie_by_id(movie_id)
    id=movie.movie_id
    title=movie.title
    director = movie.director
    rating= movie.rating

    return render_template('get_single_movie.html', id=id, title=title, director=director, rating=rating)


@app.get('/movies/<int:movie_id>/edit')
def get_edit_movies_page(movie_id: int):
    return render_template('edit_movies_form.html', id=movie_id)


@app.post('/movies/<int:movie_id>')
def update_movie(movie_id: int):
    # TODO: Feature 5
    # After updating the movie in the database, we redirect back to that single movie page
    title=request.form.get('title')
    director=request.form.get('director')
    rating=int(request.form.get('new_rating'))
    movie_repository.update_movie(movie_id, title, director, rating)
    return redirect(f'/movies/{movie_id}')

@app.post('/movies/<int:movie_id>/delete')
def delete_movie(movie_id: int):
    # TODO: Feature 6
    pass
