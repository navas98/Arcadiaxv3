import React, { useEffect, useState } from "react";
import PeliculaCard from "../components/PeliculaCard.jsx";
import Navbar from "../components/navbar.jsx";
import axios from "axios";

function Netflix() {
  const [peliculas, setPeliculas] = useState([]);

  useEffect(() => {
    const fetchPeliculas = async () => {
      try {
        const response = await axios.get("http://localhost:8000/multimedia/peliculas", {
          headers: {
            "Content-Type": "application/json",
          },
        });
        if (Array.isArray(response.data)) {
          setPeliculas(response.data);
        } else {
          console.error("Respuesta inesperada del servidor:", response.data);
        }
      } catch (error) {
        console.error("Error al obtener las películas:", error.message);
      }
    };

    fetchPeliculas();
  }, []);

  const handlePlayToggle = async (nombre) => {
    const peliculaActual = peliculas.find((p) => p.nombre === nombre);

    if (!peliculaActual) return;

    if (peliculaActual.play) {
      try {
        const response = await axios.put("http://localhost:8000/pelicula/resetear");
        if (response.status === 200) {
          setPeliculas((prevPeliculas) =>
            prevPeliculas.map((p) => ({ ...p, play: false }))
          );
        } else {
          console.error("Error al resetear las películas:", response.data);
        }
      } catch (error) {
        console.error("Error al realizar la petición de reseteo:", error);
      }
    } else {
      const nuevaPelicula = { ...peliculaActual, play: true };
      try {
        const response = await axios.put(`http://localhost:8000/multimedia/pelicula/${nombre}`, {
          play: nuevaPelicula.play,
        });

        if (response.status === 200) {
          setPeliculas((prevPeliculas) =>
            prevPeliculas.map((p) =>
              p.nombre === nombre ? { ...p, play: nuevaPelicula.play } : p
            )
          );
        } else {
          console.error("Error al cambiar el estado de la película:", response.data);
        }
      } catch (error) {
        console.error("Error al realizar la petición:", error);
      }
    }
  };

  return (
    <div
      className="min-h-screen flex flex-col items-center justify-center py-6"
      style={{
        backgroundImage: `url('/assets/fondo/tele.avif')`,
        backgroundSize: "cover",
        backgroundPosition: "center",
      }}
    >
      <Navbar />
  
      {/* Contenedor del grid con espacio adicional */}
      <div className="peliculas-grid grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-8 p-8 mt-4 justify-items-center">
        {peliculas.length > 0 ? (
          peliculas.map((pelicula, index) => (
            <PeliculaCard
              key={index}
              pelicula={pelicula}
              onPlayToggle={handlePlayToggle}
            />
          ))
        ) : (
          <p className="text-center text-xl col-span-full">No hay películas disponibles</p>
        )}
      </div>
    </div>
  );
}

export default Netflix;
