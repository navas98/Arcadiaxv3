import React from 'react';
import { useNavigate } from 'react-router-dom';

function ConsolaItem({ consola }) {
  const navigate = useNavigate();

  const handleClick = () => {
    navigate(`/juegos/${consola.toLowerCase()}`);
  };

  // Obtener la imagen correspondiente a cada consola
  const getImageSrc = (consola) => {
    switch (consola.toLowerCase()) {
      case 'psp':
        return '/assets/psp.png';
      case 'nds':
        return '/assets/nds.png';
      case 'nes':
        return '/assets/nes.png';
      case 'sega':
        return '/assets/sega.png';
      case 'game boy':
        return '/assets/gameboy.png';
      default:
        return '/assets/default.png';
    }
  };

  return (
    <button
      onClick={handleClick}
      type="button"
      className="folder-btn w-full max-w-xs flex flex-col items-center p-4 rounded-lg">
      {/* Barra superior de la carpeta */}
      <div className="folder-bar w-full h-2 bg-gray-300 rounded-t-lg"></div>

      <div className="image-container mb-2">
        <img
          src={`/assets/consolas/${encodeURIComponent(consola)}.jpg`}
          alt={consola}
          className="consola-image bg-slate-500 rounded-b-lg"
          onError={(e) => {
            e.target.src = '/assets/consolas/consolas.jpg';
          }}
        />
      </div>

      <span className="text-xl font-bold">{consola.toUpperCase()}</span>
    </button>
  );
}

export default ConsolaItem;
