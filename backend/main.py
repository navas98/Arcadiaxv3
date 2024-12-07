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
    allow_origins=["http://localhost:3000"],  # Permitir ambos orígenes
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos los encabezados
)
@app.get("/")
def welcome():
    return {"mensaje":"welcome"}

app.include_router(videojuego)
app.include_router(pelicula)
#python -m uvicorn main:app --reload
#Minuto 102=>https://www.youtube.com/watch?v=7WE6v2EKm7M&t=3024s
