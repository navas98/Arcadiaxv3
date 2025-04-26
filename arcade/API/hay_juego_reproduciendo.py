import requests
import os
from dotenv import load_dotenv

# Cargar las variables desde el archivo .env
load_dotenv()

# Obtener la IP desde el entorno
ip = os.getenv("IP")

def obtener_estado_juego():
    url = f"http://{ip}:8000/arcade/juego/ejecutando"

    try:
        respuesta = requests.get(url)

        if respuesta.status_code == 200:
            return respuesta.json()
        else:
            print(f"Error en la solicitud: {respuesta.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")
        return False
