import requests
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener la IP desde el entorno
ip = os.getenv("IP")

def reset_arcade():
    """
    Realiza una solicitud PUT a 'http://<ip>:8000/arcade/reset'
    para restablecer el estado de la arcade.

    Retorna:
    dict: Datos de la respuesta si la solicitud es exitosa.
    None: Si hay un error en la solicitud.
    """
    url = f"http://{ip}:8000/arcade/reset"

    try:
        respuesta = requests.put(url)

        if respuesta.status_code == 200:
            print("Solicitud PUT exitosa.")
            return respuesta.json()
        else:
            print(f"Error en la solicitud PUT: {respuesta.status_code}")
            print("Detalle:", respuesta.text)
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")
        return None
