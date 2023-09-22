from fastapi import FastAPI
from fastapi.responses import HTMLResponse

movies = [
   {
      "id": 1,
      "title": "Avatar",
      "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
      "year": 2009,
      "rating": 7.8,
      "category": "Acción"
   }
]

app = FastAPI()
app.title = "Mi app con Fast API"
app.version = "0.0.1"

@app.get('/', tags=['Home'])
def message():
    return {"saludo": "Hola mundo con python"}

@app.get('/html', tags=['Home'])
def message():
    return HTMLResponse('<h1> Hola mundo html con python</h1>')

@app.get('/movies', tags=['Movies'])
def get_movies():
    return movies
