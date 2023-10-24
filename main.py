from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional

app = FastAPI()
app.title = "Mi app con Fast API"
app.version = "0.0.1"

class Movie(BaseModel):
    id: Optional[int] = None
    title: str
    overview: str
    year: int
    rating: float
    category: str

movies = [
   {
      "id": 1,
      "title": "Avatar",
      "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
      "year": 2009,
      "rating": 7.8,
      "category": "Acción"
   },
   {
      "id": 2,
      "title": "Avatar 2",
      "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
      "year": 2010,
      "rating": 8.8,
      "category": "Acción"
   }
]

@app.get('/', tags=['Home'])
def message():
    return {"saludo": "Hola mundo con python"}

@app.get('/html', tags=['Home'])
def message():
    return HTMLResponse('<h1> Hola mundo html con python</h1>')

@app.get('/movies', tags=['Movies'])
def get_movies():
    return movies

@app.get('/movies/{id}', tags=['Movies'])
def get_movie(id: int):
    for item in movies:
        if item["id"] == id:
            return item
    return {'El Id ingresado no corresponde con un Id existente.'}

@app.get('/movies/', tags=['Movies'])
def get_movies_by_category(category: str, year: int):
    return list(filter(lambda item: item['category'] == category and
                       item['year'] == year, movies))

@app.post('/movies', tags=['Movies'])
def create_movie(movie: Movie):
    movies.append(movie)
    return movies

@app.put('/movies/{id}', tags=['Movies'])
def update_movie(id: int, movie: Movie):
    for item in movies:
        if item["id"] == id:
            item['title'] = movie.title
            item['year'] = movie.year
            item['overview'] = movie.overview
            item['rating'] = movie.rating
            item['category'] = movie.category
    return item

@app.delete('/movies/{id}', tags=['Movies'])
def delete_movie(id: int):
    for item in movies:
        if item["id"] == id:
            movies.remove(item)
            return movies
    return {'El Id ingresado no corresponde con un Id existente.'}