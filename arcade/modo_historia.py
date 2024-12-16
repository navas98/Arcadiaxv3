import time
import pyautogui  # Para simular las pulsaciones de teclas
import psutil  # Para comprobar si el emulador está en ejecución

def programa_ejecucion(nombre_programa):
    """
    Verifica si un programa está en ejecución.
    """
    for proc in psutil.process_iter(['name']):
        try:
            if proc.info['name'].lower() == nombre_programa.lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def gestionar_psp_emulador(nombre_programa):
    """
    Gestiona el guardado y carga de partidas en el emulador PSP.
    """
    primera_vez = True

    while True:
        # Comprobar si el emulador está en ejecución
        if programa_ejecucion(nombre_programa):
            print(f"{nombre_programa} detectado en ejecución.")

            # Si es la primera vez, pulsar F4 para cargar la partida después de 5 segundos
            if primera_vez:
                print("Esperando 5 segundos antes de cargar la última partida (F4)...")
                time.sleep(5)  # Esperar 5 segundos
                print("Cargando la última partida (F4)...")
                pyautogui.press('f4')
                primera_vez = False

            # Guardar la partida cada 30 segundos (F2)
            print("Guardando la partida (F2)...")
            pyautogui.press('f2')
            time.sleep(30)
        else:
            # Si el emulador no está en ejecución, esperar 5 segundos y seguir comprobando
            print(f"{nombre_programa} no detectado. Esperando...")
            primera_vez = True  # Resetear para cargar la partida la próxima vez
            time.sleep(5)

if __name__ == "__main__":
    # Cambia 'ppsspp.exe' al nombre del ejecutable de tu emulador PSP
    gestionar_psp_emulador("psp.exe")
