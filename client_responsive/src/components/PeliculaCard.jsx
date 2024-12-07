import React from "react";

function PeliculaCard({ pelicula, onPlayToggle }) {
  // Función para manejar el clic y alternar el estado de reproducción
  const handlePlayClick = () => {
    onPlayToggle(pelicula.nombre); // Cambia el estado de la película al hacer clic
  };

  return (
    <div
      onClick={handlePlayClick}
      className={`relative bg-black border-4 rounded-lg w-96 h-56 shadow-lg hover:scale-105 transition-all cursor-pointer ${
        pelicula.play ? "shadow-green-500" : "shadow-red-500"
      }`}
    >
      {/* Ventanas de las bobinas */}
      <div className="absolute top-1/4 left-6 w-24 h-24 bg-gray-600 rounded-full border-4 border-black"></div>
      <div className="absolute top-1/4 right-6 w-24 h-24 bg-gray-600 rounded-full border-4 border-black"></div>

      {/* Imagen de la película centrada */}
      <div className="absolute inset-0 flex items-center justify-center">
        <img
          src={`/assets/netflix/peliculas/${pelicula.imagen}`}
          alt={pelicula.nombre}
          className="w-40 h-32 object-cover rounded-md shadow-inner"
        />
      </div>

      {/* Indicador de reproducción */}
      <div className="absolute bottom-2 left-2 px-2 py-1 bg-black bg-opacity-75 text-white text-sm font-bold rounded">
        {pelicula.play ? "Reproduciendo" : "Disponible"}
      </div>
    </div>
  );
}

export default PeliculaCard;
