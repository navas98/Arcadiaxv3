import requests
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener la IP desde el entorno
ip = os.getenv("IP")

def obtener_juego_en_reproduccion():
    """
    Realiza una solicitud GET a 'http://<ip>:8000/arcade/juego/en-reproduccion'
    y retorna el objeto JSON obtenido de la respuesta.

    Retorna:
    dict: Datos del juego en reproducción si la solicitud es exitosa.
    None: Si hay un error en la solicitud.
    """
    url = f"http://{ip}:8000/arcade/juego/en-reproduccion"

    try:
        respuesta = requests.get(url)

        if respuesta.status_code == 200:
            return respuesta.json()
        else:
            print(f"Error en la solicitud: {respuesta.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")
        return None
