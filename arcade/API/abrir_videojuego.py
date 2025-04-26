import requests
import os
from dotenv import load_dotenv

# Cargar las variables del archivo .env
load_dotenv()

# Obtener la IP del servidor
ip = os.getenv("IP")

def actualizar_juego_abierto(nombre: str, consola: str):
    """
    Realiza una solicitud PUT a 'http://<ip>:8000/arcade/juego/abrir/{nombre}/{consola}'
    para actualizar el campo 'abierto' a True.
    """
    url = f"http://{ip}:8000/arcade/juego/abrir/{nombre}/{consola}"
    headers = {"Content-Type": "application/json"}
    payload = {
        "abierto": True
    }

    try:
        respuesta = requests.put(url, json=payload, headers=headers)

        if respuesta.status_code == 200:
            print("Solicitud PUT exitosa.")
            return respuesta.json()
        else:
            print(f"Error en la solicitud PUT: {respuesta.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")
        return None
