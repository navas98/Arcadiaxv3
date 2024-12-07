import asyncio
from APIS.hay_pelicula_reproduciendose import obtener_estado_pelicula
from APIS.datos_pelicula_ejecucion import obtener_pelicula_en_reproduccion
from APIS.resetear_pelicula import reset_pelicula
from programa_ejecucion.programa_ejecucion import programa_en_ejecucion
from APIS.abrir_pelicula import actualizar_pelicula_abierto
from  reproductor.abrir_pelicula import abrir_pelicula_vlc

async def main():
    while True:
        # Verificar si hay una película reproduciéndose
        estado = obtener_estado_pelicula()
        if estado:
            # Obtener la película en reproducción
            pelicula = obtener_pelicula_en_reproduccion()
            if pelicula:
                # Verificar si VLC está en ejecución
                vlc_activo = programa_en_ejecucion("vlc.exe")
                
                if not pelicula["abierto"]:
                    if not vlc_activo:
                        # Abrir la película y marcarla como abierta
                        print(f"Abriendo película: {pelicula['nombre']}")
                        actualizar_pelicula_abierto(pelicula["nombre"])
                        abrir_pelicula_vlc(pelicula["ubicacion"])
                    else:
                        print("VLC ya está activo, pero la película no estaba marcada como abierta.")
                else:
                    if not vlc_activo:
                        # Si VLC no está activo, resetear la película
                        print("El reproductor VLC se cerró. Reseteando la película...")
                        reset_pelicula()
            else:
                print("No se encontró ninguna película en reproducción.")
        else:
            print("No hay ninguna película en reproducción.")
        
        # Esperar 1 segundo antes de la siguiente iteración
        await asyncio.sleep(1)

# Ejecutar la función main
if __name__ == "__main__":
    asyncio.run(main())
    
