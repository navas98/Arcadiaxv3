import React, { useEffect, useState } from "react";
import axios from "axios";
import ConsolaItem from "../components/tarjeta_consolas.jsx";
import Navbar from "../components/navbar.jsx";

function Consolas() {
  const [consolas, setConsolas] = useState([]);

  useEffect(() => {
    const fetchConsolas = async () => {
      try {
        const response = await axios.get("http://localhost:8000/arcade/consolas", {
          withCredentials: true,
          headers: {
            "Content-Type": "application/json",
          },
        });
        if (Array.isArray(response.data)) {
          setConsolas(response.data);
        } else {
          console.error("Respuesta inesperada del servidor:", response.data);
        }
      } catch (error) {
        console.error("Error en la solicitud:", error.message);
      }
    };

    fetchConsolas();
  }, []);

  return (
    <div
      className="min-h-screen bg-black"
      style={{
        backgroundImage: `url('/assets/fondo/arcade.jpg')`,
        backgroundSize: "cover",
        backgroundPosition: "center",
        backgroundAttachment: "fixed",
      }}
    >
      {/* Navbar fijo */}
      <div className="fixed top-0 left-0 w-full z-50">
        <Navbar />
      </div>

      {/* Contenido principal */}
      <div className="pt-24 px-4">
        {/* Modo competitivo */}
        <div className="mb-12">
          <div className="flex justify-center items-center">
            <h2
              className="text-red-800 text-2xl sm:text-3xl font-bold text-center mb-8"
              style={{
                textShadow: "2px 2px 4px rgba(0, 0, 0, 0.7)",
                backgroundColor: "rgba(0, 0, 0, 0.5)",
                padding: "0.5rem 1rem",
                borderRadius: "0.5rem",
              }}
            >
              Modo competitivo 💀
            </h2>
          </div>
          <div className="flex justify-center">
            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-8 w-full max-w-7xl">
              {consolas.length > 0 ? (
                consolas.map((consola, index) => (
                  <ConsolaItem key={`competitivo-${index}`} consola={consola} />
                ))
              ) : (
                <p className="text-white text-lg sm:text-xl col-span-full text-center">
                  No hay consolas disponibles
                </p>
              )}
            </div>
          </div>
        </div>

        {/* Modo historia */}
        <div className="mt-12">
          <div className="flex justify-center items-center">
            <h2
              className="text-green-700 text-2xl sm:text-3xl font-bold text-center mb-8"
              style={{
                textShadow: "2px 2px 4px rgba(0, 0, 0, 0.7)",
                backgroundColor: "rgba(0, 0, 0, 0.5)",
                padding: "0.5rem 1rem",
                borderRadius: "0.5rem",
              }}
            >
              Modo historia ⏳
            </h2>
          </div>
          <div className="flex justify-center">
            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-8 w-full max-w-7xl">
              {consolas.length > 0 ? (
                consolas.map((consola, index) => (
                  <ConsolaItem key={`historia-${index}`} consola={consola} />
                ))
              ) : (
                <p className="text-white text-lg sm:text-xl col-span-full text-center">
                  No hay consolas disponibles
                </p>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Consolas;
