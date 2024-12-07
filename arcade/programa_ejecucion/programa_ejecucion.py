import subprocess

def programa_en_ejecucion(nombre_programa: str) -> bool:
    """
    Verifica si un programa está en ejecución en Windows.

    Parámetros:
    nombre_programa (str): Nombre del programa a buscar (ejemplo: 'gameboy.exe').

    Retorna:
    bool: True si el programa está en ejecución, False en caso contrario.
    """
    try:
        # Ejecutar el comando 'tasklist' para obtener la lista de procesos
        resultado = subprocess.run(["tasklist"], capture_output=True, text=True, check=True)

        # Buscar el nombre del programa en la salida (ignorar mayúsculas/minúsculas)
        return nombre_programa.lower() in resultado.stdout.lower()
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar 'tasklist': {e}")
        return False

