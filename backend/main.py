from fastapi import FastAPI,HTTPException
from routes.videogames import videojuego
from routes.peliculas import pelicula
#from routes.peliculas import pelicula
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

# Configuración del middleware CORS

from fastapi.middleware.cors import CORSMiddleware


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://192.168.1.79:3000"],  # o ["http://192.168.1.79:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def welcome():
    return {"mensaje":"welcome"}

app.include_router(videojuego)
app.include_router(pelicula)
#python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
#Minuto 102=>https://www.youtube.com/watch?v=7WE6v2EKm7M&t=3024sñ